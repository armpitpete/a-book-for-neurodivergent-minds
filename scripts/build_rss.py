"""Generate a simple RSS feed from clean Markdown exports."""

from __future__ import annotations

from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
import xml.etree.ElementTree as ET


EXPORT_DIR = Path("build/export/markdown-clean")
OUT_PATH = Path("build/export/rss.xml")
SITE_URL = "https://armpitpete.github.io/a-book-for-neurodivergent-minds"


def make_title(path: Path) -> str:
    return path.stem.replace("_", " ").replace("-", " ").strip().title()


def make_link(path: Path) -> str:
    relative = path.relative_to(EXPORT_DIR).as_posix()
    return f"{SITE_URL}/{relative}"


def build_rss() -> ET.ElementTree:
    now = format_datetime(datetime.now(timezone.utc), usegmt=True)

    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "A Book for Neurodivergent Minds"
    ET.SubElement(channel, "description").text = "Release feed for clean Markdown proof exports."
    ET.SubElement(channel, "link").text = SITE_URL
    ET.SubElement(channel, "lastBuildDate").text = now

    for path in sorted(EXPORT_DIR.rglob("*.md")):
        link = make_link(path)

        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = make_title(path)
        ET.SubElement(item, "link").text = link
        ET.SubElement(item, "guid").text = link
        ET.SubElement(item, "pubDate").text = now

    return ET.ElementTree(rss)


def main() -> int:
    if not EXPORT_DIR.exists():
        print(f"FAIL: clean Markdown export directory missing: {EXPORT_DIR}")
        print("Run scripts/export_all_proofs.py before building RSS.")
        return 1

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    build_rss().write(OUT_PATH, encoding="utf-8", xml_declaration=True)

    print(f"RSS feed written: {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
