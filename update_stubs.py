#!/usr/bin/env python3
"""Fetch the latest homeassistant tag and generate typing stubs for it."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

import requests
from awesomeversion import AwesomeVersion
from awesomeversion.strategy import AwesomeVersionStrategy

FIRST_SUPPORTED_VERSION = AwesomeVersion("2021.4.0b3")


def main() -> int:
    """Main function."""
    repo_root = Path(os.path.dirname(os.path.realpath(__file__)))
    homeassistant_root = repo_root / "homeassistant_core"

    # Find which versions are missing
    current_versions = set(get_available_versions(repo_root))
    homeassistant_versions = get_available_versions(homeassistant_root)
    missing_versions = [
        version for version in homeassistant_versions if version not in current_versions
    ]
    for version in missing_versions:
        print(f"Missing version: {version}")

    # Create new packages
    create_package(missing_versions[0], repo_root, homeassistant_root)
    # for version in missing_versions:
    #     create_package(version, repo_root, homeassistant_root)
    return 0


def get_available_versions(git_root: Path) -> list[str]:
    """Get list of available versions from git tags."""
    print(f"Getting list of available versions in {git_root}...")
    subprocess.run(["git", "fetch", "origin"], cwd=git_root, check=True)
    result = subprocess.run(
        ["git", "tag"],
        cwd=git_root,
        check=True,
        capture_output=True,
        text=True,
    )
    versions = [AwesomeVersion(tag) for tag in result.stdout.split()]
    versions = sorted(
        [
            version
            for version in versions
            if version.strategy == AwesomeVersionStrategy.CALVER
            and version >= FIRST_SUPPORTED_VERSION
        ]
    )
    return [version.string for version in versions]


def create_package(version: str, repo_root: Path, homeassistant_root: Path) -> None:
    """Create package for given version and upload it to PyPI."""
    print(f"Creating package for {version}...")
    subprocess.run(["git", "checkout", version], cwd=homeassistant_root, check=True)
    typed_paths = get_typed_paths(homeassistant_root)
    generate_stubs(typed_paths, repo_root)

    print("Building package...")
    subprocess.run(["poetry", "version", version], cwd=repo_root, check=True)
    subprocess.run(
        ["poetry", "add", f"homeassistant@{version}"], cwd=repo_root, check=True
    )
    subprocess.run(["poetry", "build"], cwd=repo_root, check=True)

    print(f"Creating commit for {version}...")
    subprocess.run(
        [
            "git",
            "add",
            "homeassistant_core",
            "homeassistant-stubs",
            "pyproject.toml",
            "poetry.lock",
        ],
        cwd=repo_root,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", f"Generate v{version}"], cwd=repo_root, check=True
    )
    subprocess.run(["git", "push"], cwd=repo_root, check=True)
    create_github_release(version)

    print("Publishing package...")
    pypi_token = os.environ.get("PYPI_TOKEN")
    if pypi_token is None:
        raise RuntimeError("PYPI_TOKEN is not set")
    subprocess.run(
        ["poetry", "config", "pypi-token.pypi", pypi_token],
        cwd=repo_root,
        check=True,
    )
    subprocess.run(["poetry", "publish"], cwd=repo_root, check=True)


def create_github_release(version: str) -> None:
    """Create new release on Github."""
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token is None:
        raise RuntimeError("GITHUB_TOKEN is not set")
    url = "https://api.github.com/repos/KapJI/homeassistant-stubs/releases"
    headers: dict[str, str] = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {github_token}",
    }
    data = {
        "tag_name": version,
        "target_commitish": "main",
        "name": version,
        "body": f"Generated for `homeassitant {version}`.",
        "draft": False,
        "prerelease": AwesomeVersion(version).modifier is not None,
    }
    result = requests.post(url, headers=headers, json=data)
    if result.status_code != 201:
        raise RuntimeError(f"Request failed {result.status_code}: {result.text}")


def get_typed_paths(homeassistant_root: Path) -> list[Path]:
    """Get list of strictly typed paths from Home Assistant config."""
    cfg_path = homeassistant_root / "mypy.ini"
    if not cfg_path.is_file():
        cfg_path = homeassistant_root / "setup.cfg"
    matched_lines: list[str] = []
    with cfg_path.open() as fp:
        matched_lines = [line for line in fp.readlines() if line.startswith("[mypy-")]
    if not matched_lines:
        raise Exception("can't find mypy config in setup.cfg")
    if len(matched_lines) > 2:
        raise Exception("too many mypy entries in setup.cfg, update the script")
    mypy_config = matched_lines[0][len("[mypy-") : -len("]\n")]
    typed_paths: list[Path] = []
    mypy_entries = mypy_config.split(",")
    for item in mypy_entries:
        if not item.startswith("homeassistant."):
            continue
        if item.endswith(".*"):
            typed_path = homeassistant_root / Path(
                item[: -len(".*")].replace(".", os.path.sep)
            )
            assert typed_path.is_dir(), typed_path
        else:
            # Skip if module is already added as module.*
            if item + ".*" in mypy_entries:
                continue
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


def generate_stubs(typed_paths: list[Path], repo_root: Path) -> None:
    """Use stubgen to generate typing stubs for all typed paths."""
    print("Generating stubs...")
    command_args: list[str] = [
        "poetry",
        "run",
        "stubgen",
        "--include-private",
        "-o",
        str(repo_root),
    ] + [str(folder) for folder in typed_paths]
    subprocess.run(command_args, cwd=repo_root, check=True)
    stubs_folder = repo_root / "homeassistant"
    new_stubs_folder = repo_root / "homeassistant-stubs"
    if new_stubs_folder.is_dir():
        shutil.rmtree(new_stubs_folder)
    stubs_folder.rename(new_stubs_folder)


if __name__ == "__main__":
    sys.exit(main())
