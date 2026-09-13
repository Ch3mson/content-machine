#!/usr/bin/env python3
"""Cursor sessionStart hook: point the agent at the graphify report when a graph exists."""

import json
import sys
from pathlib import Path

try:
    json.load(sys.stdin)
except json.JSONDecodeError:
    pass

graph = Path("graphify-out") / "graph.json"
if graph.exists():
    print(
        json.dumps(
            {
                "additional_context": (
                    "[graphify] Knowledge graph available. "
                    "Read graphify-out/GRAPH_REPORT.md for god nodes and "
                    "architecture context before searching files."
                )
            }
        )
    )
else:
    print(json.dumps({}))
