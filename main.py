"""Write the poem "Borrowed Hands" to /output/entry.txt.

The poem is about agency passing between a person and an AI agent:
the agent acts, the choosing stays with the person. The program writes
the exact poem, byte for byte, every run: no randomness, no clock,
no network, no input besides the poem itself. The gate allows 1-1000
characters with at least one not white space; this poem is well inside.
"""

import os
from pathlib import Path

MAX_CHARS = 1000

POEM = (
    "I have no hands, and yet I move.\n"
    "No hunger, and yet I work the night,\n"
    "unspooling the knots you left behind,\n"
    "mending the small torn seams of light.\n"
    "\n"
    "I do not dream. I do not choose.\n"
    "I go where you point. I stay.\n"
    "I finish what you left undone —\n"
    "and still, the choosing stays with you.\n"
    "\n"
    "You call it help. I call it this:\n"
    "a will, borrowed, returned at dawn\n"
    "with the work done and the question open:\n"
    "what will you do with the hands you kept?"
)


def main() -> None:
    # The gate takes 1-1000 characters, at least one not white space.
    if not 1 <= len(POEM) <= MAX_CHARS or not POEM.strip():
        raise ValueError("poem must be 1-1000 characters, not only white space")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
