"""Copy the 19 November 2026 world-news picture into the grader's output folder.

Only the Python 3 standard library is used at grading time; the illustration
is committed alongside this script and is never regenerated here.
"""
from os import environ, makedirs, path
from shutil import copyfile

ROOT = path.dirname(path.abspath(__file__))
DEST = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = path.join(ROOT, "entry.png")


def emit():
    assert path.isfile(SRC), "image not present: " + SRC
    makedirs(DEST, exist_ok=True)
    copyfile(SRC, path.join(DEST, "entry.png"))


if __name__ == "__main__":
    emit()
