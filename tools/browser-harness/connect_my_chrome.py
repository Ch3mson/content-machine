#!/usr/bin/env python3
"""
Connect browser-harness to your EXISTING Chrome profile.

This restarts Chrome with remote-debugging enabled while preserving your
bookmarks, logins, cookies, and Pinterest sessions.

Usage:
    python tools/browser-harness/connect_my_chrome.py

On first run it will close and reopen Chrome. After that, the daemon connects
instantly until you reboot or fully close Chrome.
"""
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def find_chrome():
    """Find chrome.exe on Windows."""
    candidates = [
        Path(os.environ.get("PROGRAMFILES", "C:/Program Files")) / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", "C:/Program Files (x86)")) / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Google/Chrome/Application/chrome.exe",
    ]
    for c in candidates:
        if c.exists():
            return str(c)
    try:
        out = subprocess.check_output(["where", "chrome.exe"], text=True, timeout=5).strip().splitlines()[0]
        if out:
            return out
    except Exception:
        pass
    return None


def chrome_has_debugging_port(port=9222):
    """Check if something is already listening on the debug port."""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect(("127.0.0.1", port))
        s.close()
        return True
    except (ConnectionRefusedError, socket.timeout, OSError):
        return False


def get_ws_url(port=9222):
    """Fetch the WebSocket URL from Chrome's debug endpoint."""
    req = urllib.request.Request(f"http://127.0.0.1:{port}/json/version")
    data = json.loads(urllib.request.urlopen(req, timeout=5).read())
    return data.get("webSocketDebuggerUrl")


def restart_chrome_with_debugging(chrome_path, port=9222):
    """Close existing Chrome and reopen it with remote debugging."""
    print("Closing existing Chrome...")
    subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], capture_output=True)
    time.sleep(2)

    print(f"Restarting Chrome with remote-debugging-port={port}...")
    # Start Chrome with the user's DEFAULT profile + remote debugging
    # We do NOT pass --user-data-dir so it uses the normal profile
    cmd = [
        chrome_path,
        f"--remote-debugging-port={port}",
        "--no-first-run",
        "--no-default-browser-check",
    ]
    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Chrome restarted. Waiting for it to come up...")

    # Wait for port to be live
    deadline = time.time() + 20
    while time.time() < deadline:
        if chrome_has_debugging_port(port):
            return True
        time.sleep(0.5)
    return False


def main():
    print("Browser Harness — Connect My Chrome")
    print("=" * 40)

    chrome = find_chrome()
    if not chrome:
        print("ERROR: Chrome not found.")
        sys.exit(1)
    print(f"Chrome: {chrome}")

    if chrome_has_debugging_port(9222):
        print("Chrome already has remote debugging on port 9222.")
    else:
        print("\nYour Chrome needs to be restarted with remote debugging enabled.")
        print("This preserves all your logins, bookmarks, and Pinterest sessions.")
        ans = input("Restart Chrome now? [Y/n] ").strip().lower()
        if ans and ans not in ("y", "yes"):
            print("Cancelled. Run this again when you're ready.")
            sys.exit(0)

        if not restart_chrome_with_debugging(chrome):
            print("ERROR: Chrome did not start remote debugging in time.")
            sys.exit(1)

    # Set the WS URL
    try:
        ws_url = get_ws_url(9222)
        os.environ["BU_CDP_WS"] = ws_url
        print(f"Debug WS: {ws_url}")
    except Exception as e:
        print(f"ERROR: Could not fetch debug URL: {e}")
        sys.exit(1)

    # Start daemon
    print("\nStarting browser-harness daemon...")
    from admin import ensure_daemon
    try:
        ensure_daemon(wait=15)
        print("Daemon is up!")
    except RuntimeError as e:
        print(f"Daemon failed: {e}")
        sys.exit(1)

    print("\nYour Chrome is connected.")
    print("You can now run image sourcing or other browser-harness commands.")
    print("\nQuick test:")
    print('  python -c "from helpers import page_info; print(page_info())"')


if __name__ == "__main__":
    main()
