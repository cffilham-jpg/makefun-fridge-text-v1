"""Write a smart fridge's 3am text to the configured output directory.
The butter line pairs a concrete fridge staple with one unexplained twist.
"""

import os
from pathlib import Path


LINE = "The butter has seen things."

if not 1 <= len(LINE) <= 140:
    raise ValueError("The entry line must be between 1 and 140 characters.")

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
