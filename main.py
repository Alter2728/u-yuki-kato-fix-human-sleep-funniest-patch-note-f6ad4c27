from pathlib import Path

TEXT = "Fixed: sleep no longer pauses at 3 a.m. for a director's-cut replay of every embarrassing thing you said since 2007."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")
    assert output_path.read_text(encoding="utf-8") == TEXT


if __name__ == "__main__":
    main()
