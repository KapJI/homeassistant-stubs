#!/usr/bin/env python3
"""Fetch the latest homeassistant tag and generate typing stubs for it."""

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List


def main() -> int:
    """Main function"""
    repo_root = Path(os.path.dirname(os.path.realpath(__file__)))
    homeassistant_root = repo_root / "homeassistant_core"
    typed_paths = get_typed_paths(homeassistant_root)
    generate_stubs(typed_paths, repo_root)
    return 0


def get_typed_paths(homeassistant_root: Path) -> List[Path]:
    """Get list of strictly typed paths from Home Assistant config"""
    setup_cfg = homeassistant_root / "setup.cfg"
    matched_lines: List[str] = []
    with setup_cfg.open() as fp:
        matched_lines = [line for line in fp.readlines() if line.startswith("[mypy-")]
    if not matched_lines:
        raise Exception("can't find mypy config in setup.cfg")
    if len(matched_lines) > 1:
        raise Exception("too many mypy entries in setup.cfg, update the script")
    mypy_config = matched_lines[0][len("[mypy-") : -len("]\n")]
    typed_paths: List[Path] = []
    for item in mypy_config.split(","):
        if not item.startswith("homeassistant."):
            continue
        if item.endswith(".*"):
            typed_path = homeassistant_root / Path(
                item[: -len(".*")].replace(".", os.path.sep)
            )
            assert typed_path.is_dir(), typed_path
        else:
            item = item.replace(".", os.path.sep)
            typed_path = homeassistant_root / (item + ".py")
            if not typed_path.is_file():
                typed_path = homeassistant_root / item
                if typed_path.is_dir():
                    typed_path = typed_path / "__init__.py"
                else:
                    continue
        typed_paths.append(typed_path)
    return typed_paths


def generate_stubs(typed_paths: List[Path], output_folder: Path) -> None:
    """Use stubgen to generate typing stubs for all typed paths"""
    print("Generating stubs...")
    command_args: List[str] = [
        "poetry",
        "run",
        "stubgen",
        "-o",
        str(output_folder),
    ] + [str(folder) for folder in typed_paths]
    subprocess.run(command_args, check=True)
    stubs_folder = output_folder / "homeassistant"
    new_stubs_folder = output_folder / "homeassistant-stubs"
    if new_stubs_folder.is_dir():
        shutil.rmtree(new_stubs_folder)
    stubs_folder.rename(new_stubs_folder)


if __name__ == "__main__":
    sys.exit(main())
