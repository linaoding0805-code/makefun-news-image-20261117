#!/usr/bin/env python3
"""Entry for news-image-20261117 (Python 3.13, standard library only).

Copies the front-page image to /output/entry.png. The copy is byte for byte,
so two runs write identical bytes. The image
(entry.png, 1024x1024, under 1 MiB) sums up Tuesday 17 November 2026 in
four stories: the Kerch Bridge span collapsing after a Ukrainian strike,
tankers mined in the Strait of Hormuz, the Xi-Trump-Putin meeting set for
Thursday in Shenzhen, and the Vulcan failure that lost 40 Amazon satellites.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )

if __name__ == "__main__":
    main()
