import json
import re
from datetime import datetime, timezone
from pathlib import Path

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.benchmark import print_benchmark, run_benchmark
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.export import to_html, to_json
from graphify.report import generate

ROOT = Path.cwd()
SRC = ROOT / "references" / "creative-dna"
OUT = ROOT / "graphify-out" / "creative-dna"
OUT.mkdir(parents=True, exist_ok=True)


def rel(path):
    path = Path(path)
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except Exception:
        return str(path).replace("\\", "/")


def slug(value):
    value = re.sub(r"[`*_\[\]()]", "", str(value).strip().lower())
    value = value.replace("→", " to ").replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return re.sub(r"_+", "_", value).strip("_") or "unknown"


nodes = {}
edges = []
hyperedges = []


def node(node_id, label, source_file, **attrs):
    if node_id not in nodes:
        nodes[node_id] = {
            "id": node_id,
            "label": label,
            "file_type": "document",
            "source_file": source_file,
            "source_location": attrs.pop("source_location", None),
            "source_url": None,
            "captured_at": None,
            "author": None,
            "contributor": None,
        }
    for k, v in attrs.items():
        if v not in (None, ""):
            nodes[node_id][k] = v
    return node_id


def edge(source, target, relation, source_file, confidence="EXTRACTED", score=1.0, weight=1.0, loc=None):
    if source == target or source not in nodes or target not in nodes:
        return
    edges.append({
        "source": source,
        "target": target,
        "relation": relation,
        "confidence": confidence,
        "confidence_score": score,
        "source_file": source_file,
        "source_location": loc,
        "weight": weight,
    })


def section(text, title):
    match = re.search(rf"(?ms)^## {re.escape(title)}\s*\n(.*?)(?=^## |\Z)", text)
    return match.group(1).strip() if match else ""


def kv(block):
    out = {}
    for line in block.splitlines():
        match = re.match(r"^-\s*([^:]+):\s*(.*)$", line.strip())
        if match:
            out[match.group(1).strip()] = match.group(2).strip()
    return out


def table_rows(block):
    for line in block.splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        yield [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]


system = node("creative_dna_memory_system", "Creative DNA Memory System", rel(SRC / "README.md"))
reference_layer = node("layer_viral_reference_posts", "Viral Reference Posts Layer", "curated:creative-dna")
principle_layer = node("layer_reusable_principles", "Reusable Principles Layer", "curated:creative-dna")
account_layer = node("layer_owned_account_profiles", "Owned Account Profiles Layer", "curated:creative-dna")
concept_layer = node("layer_possible_post_concepts", "Possible Post Concepts Layer", "curated:creative-dna")
workflow_layer = node("layer_workflow_routes", "Workflow Routes Layer", "curated:creative-dna")
for layer in [reference_layer, principle_layer, account_layer, concept_layer, workflow_layer]:
    edge(system, layer, "implements", "curated:creative-dna", "INFERRED", 0.9)

workflow_nodes = {}
for label, path in {
    "Hook Idea Extraction": "references/skills/hook-idea-extraction/SKILL.md",
    "Angle Variants": "references/skills/angle-variants/SKILL.md",
    "Post Concept Flow": "references/skills/post-concept-flow/SKILL.md",
    "Workflow B New Post": "workflows/workflow-b-new-post.md",
    "Stop Slop QA": "references/skills/stop-slop/SKILL.md",
    "Workflow A3 Quality Gate": "workflows/workflow-a3-writing-design-quality-gate.md",
}.items():
    wid = node(f"workflow_{slug(label)}", label, path, category="workflow_or_skill")
    workflow_nodes[label] = wid
    edge(workflow_layer, wid, "references", path)

# Keep workflow downstream and sparse: sequence only, not every concept to every workflow.
for before, after in zip(["Hook Idea Extraction", "Angle Variants", "Post Concept Flow", "Workflow B New Post", "Stop Slop QA"], ["Angle Variants", "Post Concept Flow", "Workflow B New Post", "Stop Slop QA", "Workflow A3 Quality Gate"]):
    edge(workflow_nodes[before], workflow_nodes[after], "references", "references/creative-dna/creative-dna-workflow-router.md", "INFERRED", 0.84)

account_ids = {}
profile_ids = {}
concept_bank_ids = {}
account_fit_ids = {}


def ensure_account_fit(account, family_id, source_file):
    key = (account, family_id)
    if key not in account_fit_ids:
        family_label = family_labels.get(family_id, family_id)
        fit_id = node(
            f"account_fit_{slug(account)}_{slug(family_id)}",
            f"{account} fit: {family_label}",
            source_file,
            category="account_mechanism_fit",
            account=account,
            mechanism_family=family_id,
        )
        account_fit_ids[key] = fit_id
        bank = concept_bank_ids.get(account)
        if bank:
            edge(bank, fit_id, "groups", source_file, "EXTRACTED", 1.0, 1.1)
    return account_fit_ids[key]


for account in ["athlete-max", "athlete-stories", "Athlete-user-soccer"]:
    aid = node(f"target_account_{slug(account)}", account, f"accounts/{account}/post-status.md", category="owned_account")
    account_ids[account] = aid
    edge(account_layer, aid, "references", f"accounts/{account}/post-status.md")
    profile_path = SRC / "account-profiles" / f"{account}.md"
    if profile_path.exists():
        pid = node(f"account_profile_{slug(account)}", f"Account Profile: {account}", rel(profile_path), category="account_profile")
        profile_ids[account] = pid
        edge(aid, pid, "references", rel(profile_path))
        bank = node(f"concept_bank_{slug(account)}", f"Concept Bank: {account}", rel(profile_path), category="account_concept_bank")
        concept_bank_ids[account] = bank
        edge(pid, bank, "suggests", rel(profile_path), "EXTRACTED", 1.0, 1.2)
    for doc, label in [("account-brief.md", "Account Brief"), ("writing.md", "Writing Rules"), ("design.md", "Design Rules"), ("image.md", "Image Rules"), ("presets.md", "Angle Presets")]:
        p = ROOT / "accounts" / account / doc
        if p.exists():
            cid = node(f"constraint_{slug(account)}_{slug(label)}", f"{account} {label}", rel(p), category="account_constraint")
            edge(aid, cid, "constrained_by", rel(p))
            if account in profile_ids:
                edge(profile_ids[account], cid, "constrained_by", rel(p))

cross = SRC / "cross-niche-principle-map.md"
cross_text = cross.read_text(encoding="utf-8")
families = {}
family_labels = {}
for row in table_rows(section(cross_text, "Canonical Mechanism Matrix")):
    if len(row) < 9 or row[0] == "family_id":
        continue
    family_id, family_label = row[0], row[1]
    fid = node(f"principle_{slug(family_id)}", family_label, rel(cross), category="mechanism_family", core_mechanism=row[3], primary_lever=row[4], proof_surface=row[5], transfer_condition=row[6], strongest_target_fit=row[8])
    families[family_id] = fid
    family_labels[family_id] = family_label
    edge(principle_layer, fid, "references", rel(cross), weight=1.5)
    for src in [s.strip() for s in row[2].split(",") if s.strip()]:
        sid = node(f"reference_post_{slug(src)}", src, rel(cross), category="viral_reference_post")
        edge(sid, fid, "expresses", rel(cross), "EXTRACTED", 1.0, 1.7)
    for acct in [a.strip() for a in row[8].split(",") if a.strip()]:
        if acct in concept_bank_ids:
            fit = ensure_account_fit(acct, family_id, rel(cross))
            edge(fid, fit, "transferable_to", rel(cross), "INFERRED", 0.88, 1.3)

edge_block = re.search(r"(?ms)^## Explicit Cross-Niche Edges For Graphify\s*\n```text\n(.*?)\n```", cross_text)
if edge_block:
    for line in edge_block.group(1).splitlines():
        parts = [p.strip() for p in line.split("→")]
        if len(parts) == 3 and parts[0] in families and parts[2] in families:
            edge(families[parts[0]], families[parts[2]], parts[1], rel(cross), "INFERRED", 0.82, 1.4)

router_text = (SRC / "owned-account-idea-router.md").read_text(encoding="utf-8")
workflow_by_family = {}
for row in table_rows(section(router_text, "Workflow Routing By Mechanism")):
    if len(row) >= 2 and row[0] != "family_id":
        workflow_by_family[row[0]] = row[1]
for fam, workflow_name in workflow_by_family.items():
    if fam in families:
        for label, wid in workflow_nodes.items():
            if label.lower().replace(" ", "-") in workflow_name.lower() or workflow_name.lower() in label.lower().replace(" ", "-"):
                edge(families[fam], wid, "maps_to", "references/creative-dna/owned-account-idea-router.md", "EXTRACTED", 1.0, 0.9)

for path in sorted((SRC / "extractions").glob("2026-05-01-*.md")):
    text = path.read_text(encoding="utf-8")
    r = rel(path)
    g = kv(section(text, "Graphify Nodes To Create"))
    sid = g.get("Viral Reference Post", path.stem)
    s_node = node(f"reference_post_{slug(sid)}", sid, r, category="viral_reference_post")
    edge(reference_layer, s_node, "references", r)
    fam = g.get("Reusable Principle")
    f_node = families.get(fam) or node(f"principle_{slug(fam)}", fam, r, category="mechanism_family")
    edge(s_node, f_node, "expresses", r, "EXTRACTED", 1.0, 2.0)
    for key, relation, cat in [
        ("Psychological Mechanism", "uses", "psychological_mechanism"),
        ("Emotional Lever", "relies_on", "emotional_lever"),
        ("Hook Archetype", "uses", "hook_archetype"),
        ("Proof Pattern", "proves_with", "proof_pattern"),
        ("Transformation Arc", "follows", "transformation_arc"),
        ("Slide Sequence", "follows", "slide_sequence"),
        ("Visual Pattern", "demonstrates", "visual_pattern"),
        ("Curiosity Gap", "creates", "curiosity_gap"),
        ("VOC Pattern", "references", "voc_pattern"),
    ]:
        val = g.get(key)
        if val:
            nid = node(f"{cat}_{slug(val)[:80]}", val, r, category=cat)
            edge(s_node, nid, relation, r)
            if key in {"Psychological Mechanism", "Emotional Lever", "Hook Archetype", "Proof Pattern"}:
                edge(f_node, nid, relation, r, "INFERRED", 0.84, 1.2)
    transfer = g.get("Transfer Opportunity", "")
    if transfer:
        tid = node(f"transfer_{slug(sid)}", transfer, r, category="transfer_opportunity")
        edge(f_node, tid, "suggests", r, "INFERRED", 0.84, 1.2)
        for acct in ["athlete-max", "athlete-stories"]:
            if acct in transfer and acct in concept_bank_ids:
                target = ensure_account_fit(acct, fam, r) if fam in families else concept_bank_ids[acct]
                edge(tid, target, "transferable_to", r, "INFERRED", 0.86, 1.1)
    for concept in [c.strip() for c in g.get("Possible Post Concept", "").split(";") if c.strip()]:
        cid = node(f"possible_concept_{slug(concept)[:90]}", concept, r, category="possible_post_concept")
        edge(concept_layer, cid, "references", r)
        edge(f_node, cid, "suggests", r, "INFERRED", 0.88, 1.5)
    for row in table_rows(section(text, "Cross-Niche Connections")):
        if len(row) >= 4 and row[0] != "Related source" and row[0].lower() != "n/a":
            rid = node(f"reference_post_{slug(row[0])}", row[0], r, category="viral_reference_post")
            edge(s_node, rid, "shares_mechanism_with", r, "INFERRED", 0.78, 1.1)

for path in sorted((SRC / "account-profiles").glob("*.md")):
    if path.name == "README.md":
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    r = rel(path)
    account = path.stem
    pid = profile_ids.get(account)
    if not pid:
        continue
    for fam, fid in families.items():
        if fam in text:
            fit = ensure_account_fit(account, fam, r)
            edge(fid, fit, "transferable_to", r, "EXTRACTED", 1.0, 1.3)
    for line in re.findall(r"(?m)^\d+\. \*\*(.*?)\*\* \| `([^`]+)` \| (.*?) \| (.*?) \| (.*?) \| (.*?)$", text):
        title, fam, hook, desire, proof, workflow = line
        cid = node(f"account_concept_{slug(account)}_{slug(title)[:80]}", title, r, category="account_specific_concept", account=account, mechanism_family=fam, hook_direction=hook, desire=desire, proof_surface=proof, workflow_entry=workflow)
        bank = concept_bank_ids.get(account, pid)
        if fam in families:
            fit = ensure_account_fit(account, fam, r)
            edge(fit, cid, "suggests", r, "EXTRACTED", 1.0, 1.6)
        else:
            edge(bank, cid, "suggests", r, "EXTRACTED", 1.0, 1.2)

router = node("owned_account_idea_router", "Owned Account Idea Router", rel(SRC / "owned-account-idea-router.md"), category="idea_router")
edge(system, router, "implements", rel(SRC / "owned-account-idea-router.md"), "EXTRACTED", 1.0)
for layer in [principle_layer, account_layer, concept_layer, workflow_layer]:
    edge(router, layer, "references", rel(SRC / "owned-account-idea-router.md"))

hyperedges.append({"id": "owned_account_creative_dna_idea_flow", "label": "Owned Account Creative DNA Idea Flow", "nodes": [reference_layer, principle_layer, account_layer, concept_layer, workflow_layer], "relation": "form", "confidence": "INFERRED", "confidence_score": 0.9, "source_file": rel(SRC / "owned-account-idea-router.md")})
hyperedges.append({"id": "cross_niche_mechanism_families", "label": "Cross-Niche Mechanism Families", "nodes": list(families.values()), "relation": "form", "confidence": "EXTRACTED", "confidence_score": 1.0, "source_file": rel(cross)})

deduped, seen = [], set()
for e in edges:
    key = (e["source"], e["target"], e["relation"], e["source_file"])
    if key not in seen:
        seen.add(key)
        deduped.append(e)
edges = deduped

files = [SRC / "README.md", SRC / "graphify-instructions.md", SRC / "creative-dna-workflow-router.md", SRC / "owned-account-idea-router.md", SRC / "inferred-edge-qa.md", cross, SRC / "account-profiles/README.md"]
files += sorted((SRC / "templates").glob("*.md")) + sorted((SRC / "extractions").glob("*.md")) + sorted((SRC / "account-profiles").glob("*.md"))
for extra in ["accounts/athlete-max/writing.md", "accounts/athlete-max/design.md", "accounts/athlete-max/image.md", "accounts/athlete-max/presets.md", "accounts/athlete-stories/writing.md", "accounts/athlete-stories/design.md", "accounts/athlete-stories/image.md", "accounts/athlete-stories/presets.md"]:
    p = ROOT / extra
    if p.exists():
        files.append(p)
files = [f for i, f in enumerate(files) if f.exists() and f not in files[:i]]
words = sum(len(re.findall(r"\w+", f.read_text(encoding="utf-8", errors="ignore"))) for f in files)
extraction = {"nodes": list(nodes.values()), "edges": edges, "hyperedges": hyperedges, "input_tokens": 0, "output_tokens": 0}
detection = {"total_files": len(files), "total_words": words, "needs_graph": True, "warning": None, "files": {"document": [rel(f) for f in files]}}
(OUT / "extract.json").write_text(json.dumps(extraction, indent=2), encoding="utf-8")
(OUT / "detect.json").write_text(json.dumps(detection, indent=2), encoding="utf-8")
G = build_from_json(extraction)
communities = cluster(G)
cohesion = score_all(G, communities)
gods = god_nodes(G)
surprises = surprising_connections(G, communities)

labels = {}
node_labels = {n["id"]: n["label"] for n in extraction["nodes"]}
used = set()
family_label_values = list(family_labels.values())
family_node_labels = {families[fam]: label for fam, label in family_labels.items() if fam in families}
for cid, members in communities.items():
    member_labels = [node_labels.get(m, m) for m in members]
    text = " ".join(member_labels).lower()
    label = None
    member_set = set(members)
    for family_node, fam_label in family_node_labels.items():
        if family_node in member_set:
            label = f"{fam_label} Ideas"
            break
    for fam_label in family_label_values:
        if not label and fam_label.lower() in text:
            label = f"{fam_label} Ideas"
            break
    if not label:
        if "athlete-max" in text and "athlete-stories" not in text:
            label = "Athlete-Max Concepts"
        elif "athlete-stories" in text and "athlete-max" not in text:
            label = "Athlete-Stories Concepts"
        elif "account profile" in text or "owned account" in text:
            label = "Account Fit Layer"
        elif "workflow" in text or "post concept flow" in text or "angle variants" in text:
            label = "Workflow Routing"
        elif "possible concept" in text or "habit" in text:
            label = "Post Concept Seeds"
        else:
            label = "Creative Mechanisms"
    base = label
    if label in used:
        label = f"{base} {cid}"
    used.add(label)
    labels[cid] = label

questions = suggest_questions(G, communities, labels)
report = generate(G, communities, cohesion, labels, gods, surprises, detection, {"input": 0, "output": 0}, "Creative DNA Graph with Owned Accounts", suggested_questions=questions)
(OUT / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
to_json(G, communities, str(OUT / "graph.json"))
to_html(G, communities, str(OUT / "graph.html"), community_labels=labels)
(OUT / "cost.json").write_text(json.dumps({"runs": [{"date": datetime.now(timezone.utc).isoformat(), "input_tokens": 0, "output_tokens": 0, "files": len(files)}], "total_input_tokens": 0, "total_output_tokens": 0}, indent=2), encoding="utf-8")
if words > 5000:
    print_benchmark(run_benchmark(str(OUT / "graph.json"), corpus_words=words))
print(f"Creative DNA Graph with Owned Accounts: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, {len(communities)} communities")
print(f"Corpus: {len(files)} curated docs · ~{words} words")
print(f"Outputs: {OUT}")
