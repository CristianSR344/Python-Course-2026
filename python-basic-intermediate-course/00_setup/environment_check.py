"""Check that the course runtime and core dependencies are available."""

from importlib.util import find_spec
import platform
import sys


REQUIRED_MODULES = ("fastapi", "sqlalchemy", "pydantic", "jinja2", "pytest")


def check_environment() -> bool:
    print(f"Python: {platform.python_version()}")
    print(f"Executable: {sys.executable}")
    version_ok = sys.version_info >= (3, 11)
    print(f"Python 3.11+: {'OK' if version_ok else 'UPDATE REQUIRED'}")
    missing = [name for name in REQUIRED_MODULES if find_spec(name) is None]
    print("Dependencies:", "OK" if not missing else f"missing {', '.join(missing)}")
    return version_ok and not missing


if __name__ == "__main__":
    raise SystemExit(0 if check_environment() else 1)

