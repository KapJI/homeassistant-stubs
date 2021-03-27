#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from typing import List

def get_typed_folder(homeassistant_root: Path) -> List[Path]:
    """Get list of strictly typed folders from Home Assistant config"""
    setup_cfg = homeassistant_root / "setup.cfg"
    matched_lines = []
    with setup_cfg.open() as f:
        matched_lines = [line for line in f.readlines() if line.startswith("[mypy-")]
    if matched_lines:
        raise Exception("can't find mypy config in setup.cfg")
    if len(matched_lines) > 1:
        raise Exception("too many mypy config entries in setup.cfg, update the script")

def main() -> int:
    """Main function"""
    repo_root = Path(os.path.dirname(os.path.realpath(__file__)))
    homeassistant_root = repo_root / "homeassistant_core"
    typed_folders = get_typed_folder(homeassistant_root)

    return 0

if __name__ == "__main__":
    sys.exit(main())
