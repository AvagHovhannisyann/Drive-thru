#!/usr/bin/env python3
"""Kept for the documented command; the check now covers every skill pack.

    python3 tools/blender-mcp/check_skills.py   ==   python3 tools/skills/check.py
"""

import runpy
import sys
from pathlib import Path

sys.argv[0] = str(Path(__file__).resolve().parents[1] / "skills" / "check.py")
runpy.run_path(sys.argv[0], run_name="__main__")
