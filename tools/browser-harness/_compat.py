"""Windows compatibility shim for browser-harness socket paths.
Replaces Unix socket paths with TCP localhost on Windows."""
import os
import socket
import sys
import tempfile
from pathlib import Path

_IS_WIN = sys.platform == "win32"

NAME = os.environ.get("BU_NAME", "default")

if _IS_WIN:
    _TEMP = Path(tempfile.gettempdir())
    SOCK_PATH = _TEMP / f"bu-{NAME}.port"
    LOG_PATH = _TEMP / f"bu-{NAME}.log"
    PID_PATH = _TEMP / f"bu-{NAME}.pid"
    VERSION_CACHE = _TEMP / "bu-version-cache.json"
else:
    SOCK_PATH = Path(f"/tmp/bu-{NAME}.sock")
    LOG_PATH = Path(f"/tmp/bu-{NAME}.log")
    PID_PATH = Path(f"/tmp/bu-{NAME}.pid")
    VERSION_CACHE = Path("/tmp/bu-version-cache.json")


def _get_port():
    """Return the stored TCP port, or None."""
    try:
        return int(SOCK_PATH.read_text().strip())
    except (FileNotFoundError, ValueError):
        return None


def _store_port(port):
    SOCK_PATH.write_text(str(port))


def _remove_port():
    try:
        SOCK_PATH.unlink()
    except FileNotFoundError:
        pass


def make_client_socket():
    """Create a client socket connected to the daemon."""
    if _IS_WIN:
        port = _get_port()
        if port is None:
            raise FileNotFoundError(f"daemon port file not found: {SOCK_PATH}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect(("127.0.0.1", port))
        return s
    else:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect(str(SOCK_PATH))
        return s


def try_connect_daemon():
    """Best-effort connect to check if daemon is alive. Returns True/False."""
    if _IS_WIN:
        port = _get_port()
        if port is None:
            return False
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect(("127.0.0.1", port))
            s.close()
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False
    else:
        try:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect(str(SOCK_PATH))
            s.close()
            return True
        except (FileNotFoundError, ConnectionRefusedError, socket.timeout):
            return False
