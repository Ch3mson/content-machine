"""
Windows bootstrap for browser-harness.

Finds Chrome, starts it with remote-debugging on a dedicated profile if needed,
and ensures the daemon is running.
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

# Add browser-harness to path
_bh = Path(__file__).parent
sys.path.insert(0, str(_bh))

from _compat import LOG_PATH, PID_PATH, _remove_port


def find_chrome():
    """Find chrome.exe or msedge.exe on Windows."""
    candidates = [
        Path(os.environ.get("PROGRAMFILES", "C:/Program Files")) / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", "C:/Program Files (x86)")) / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("PROGRAMFILES", "C:/Program Files")) / "Microsoft/Edge/Application/msedge.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", "C:/Program Files (x86)")) / "Microsoft/Edge/Application/msedge.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft/Edge/Application/msedge.exe",
    ]
    for c in candidates:
        if c.exists():
            return str(c)
    # Try where command
    for name in ("chrome.exe", "msedge.exe"):
        try:
            out = subprocess.check_output(["where", name], text=True, timeout=5).strip().splitlines()[0]
            if out:
                return out
        except Exception:
            pass
    return None


def chrome_running():
    try:
        out = subprocess.check_output(["tasklist", "/FI", "IMAGENAME eq chrome.exe"], text=True, timeout=5)
        return "chrome.exe" in out.lower()
    except Exception:
        return False


def start_chrome_with_debugging(chrome_path, profile_dir, port=9222):
    """Start Chrome with remote debugging on a specific profile."""
    cmd = [
        chrome_path,
        f"--remote-debugging-port={port}",
        f"--user-data-dir={profile_dir}",
        "--no-first-run",
        "--no-default-browser-check",
        "--window-size=1280,800",
    ]
    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Started Chrome with remote debugging on port {port}")
    print(f"Profile: {profile_dir}")


def wait_for_devtools_port(profile_dir, port=9222, timeout=30):
    """Wait for Chrome remote debugging to be live on the TCP port.
    On Windows with explicit --remote-debugging-port, Chrome may not write
    DevToolsActivePort, so we probe the TCP port directly."""
    import socket
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect(("127.0.0.1", port))
            s.close()
            return port, None
        except (ConnectionRefusedError, socket.timeout, OSError):
            pass
        time.sleep(0.5)
    return None, None


def main():
    print("browser-harness Windows Bootstrap")
    print("-" * 40)

    chrome = find_chrome()
    if not chrome:
        print("ERROR: Could not find Chrome or Edge.")
        print("Please install Google Chrome or Microsoft Edge.")
        sys.exit(1)
    print(f"Found browser: {chrome}")

    # Use a dedicated profile in the project dir
    profile_dir = Path(__file__).parent / ".chrome-harness-profile"
    profile_dir.mkdir(exist_ok=True)

    # Use a dedicated profile in the project dir
    profile_dir = Path(__file__).parent / ".chrome-harness-profile"
    profile_dir.mkdir(exist_ok=True)

    # Probe if our Chrome is already listening on 9222
    existing_port = None
    import socket, urllib.request
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect(("127.0.0.1", 9222))
        s.close()
        existing_port = 9222
        print("Chrome already listening on port 9222")
        # Fetch WS URL
        req = urllib.request.Request("http://127.0.0.1:9222/json/version")
        data = json.loads(urllib.request.urlopen(req, timeout=5).read())
        os.environ["BU_CDP_WS"] = data.get("webSocketDebuggerUrl", "ws://127.0.0.1:9222/devtools/browser")
    except Exception:
        existing_port = None

    if not existing_port:
        # Kill any existing Chrome using this profile to avoid lock issues
        # (We only kill Chrome instances with our profile dir in the command line)
        start_chrome_with_debugging(chrome, profile_dir)
        port, _ = wait_for_devtools_port(profile_dir)
        if not port:
            print("ERROR: Chrome did not start remote debugging in time.")
            sys.exit(1)
        print(f"Remote debugging active on port {port}")

        # Fetch the WebSocket debugger URL from Chrome directly
        import urllib.request
        req = urllib.request.Request(f"http://127.0.0.1:{port}/json/version")
        try:
            data = json.loads(urllib.request.urlopen(req, timeout=5).read())
            ws_url = data.get("webSocketDebuggerUrl")
            if not ws_url:
                print("ERROR: Could not get webSocketDebuggerUrl from Chrome.")
                sys.exit(1)
            # Replace localhost/127.0.0.1 to be consistent
            os.environ["BU_CDP_WS"] = ws_url
        except Exception as e:
            print(f"ERROR: Could not fetch debugger info: {e}")
            sys.exit(1)

    # Start daemon
    print("\nStarting browser-harness daemon...")
    from admin import ensure_daemon
    try:
        ensure_daemon(wait=15)
        print("Daemon is up and running!")
    except RuntimeError as e:
        print(f"Daemon failed to start: {e}")
        sys.exit(1)

    print("\nBrowser harness is ready.")
    print("You can now run image sourcing or other browser-harness commands.")


if __name__ == "__main__":
    main()
