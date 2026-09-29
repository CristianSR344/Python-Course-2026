"""Project-safe text file reading and writing."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"


def write_report(lines: list[str], filename: str = "report.txt") -> Path:
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / filename
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def read_report(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


if __name__ == "__main__":
    report_path = write_report(["Active users: 3", "Inactive users: 1"])
    print(*read_report(report_path), sep="\n")

