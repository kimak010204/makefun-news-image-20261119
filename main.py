#!/usr/bin/env python3
"""news-image-20261119: emit the front page for Thursday 19 November 2026.

The front page is composed at build time (see compose.py) and shipped in
this repository as image.png. The grader runs this program with no network
and only the standard library, so all this entrypoint does is validate the
bundled image and copy it to the output directory, byte for byte, then
verify the copy before reporting success.
"""

import hashlib
import os
import struct
import sys

IMAGE = "image.png"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("main.py: " + message, file=sys.stderr)
    return 1


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE)
    try:
        with open(src, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        return fail("cannot read %s: %s" % (IMAGE, exc))
    if data[:8] != PNG_MAGIC:
        return fail("%s is not a PNG file" % IMAGE)
    if len(data) > MAX_BYTES:
        return fail("%s is %d bytes, over the 1 MiB cap" % (IMAGE, len(data)))
    # IHDR: width and height are the first 8 bytes after the 8-byte magic
    # and the 8-byte chunk header (length + "IHDR").
    if len(data) < 24 or data[12:16] != b"IHDR":
        return fail("%s has no IHDR chunk" % IMAGE)
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        return fail("%s is %dx%d, over the 1024x1024 cap" % (IMAGE, width, height))
    if width < 1 or height < 1:
        return fail("%s has invalid dimensions %dx%d" % (IMAGE, width, height))
    digest = hashlib.sha256(data).hexdigest()
    try:
        os.makedirs(out_dir, exist_ok=True)
        dst = os.path.join(out_dir, "entry.png")
        with open(dst, "wb") as handle:
            handle.write(data)
        with open(dst, "rb") as handle:
            copied = handle.read()
    except OSError as exc:
        return fail("cannot write output: %s" % exc)
    if len(copied) != len(data):
        return fail("copy is %d bytes, expected %d" % (len(copied), len(data)))
    if hashlib.sha256(copied).hexdigest() != digest:
        return fail("copy failed SHA-256 verification")
    print("entry.png written: %d bytes sha256=%s" % (len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
