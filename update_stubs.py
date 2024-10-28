#!/usr/bin/env python3
"""Fetch the latest homeassistant tag and generate typing stubs for it."""

from __future__ import annotations

import argparse
import json
import logging
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
from typing import TYPE_CHECKING
from urllib.request import urlopen

from awesomeversion.awesomeversion import AwesomeVersion
from awesomeversion.strategy import AwesomeVersionStrategy
from github import Auth, Github

if TYPE_CHECKING:
    from github.Repository import Repository

FIRST_SUPPORTED_VERSION = AwesomeVersion("2021.4.0b3")
LOGGER = logging.getLogger(__name__)


def main() -> int:
    """Run main function."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(asctime)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    parser = argparse.ArgumentParser(description="Generate typing stubs.")
    parser.add_argument(
        "--dry-run",
        default=False,
        action="store_true",
        help="generate but do not publish anything",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    homeassistant_root = repo_root / "homeassistant_core"

    # Find which versions are missing
    available_versions = get_available_versions(repo_root)
    # For dry run, re-generate the last version
    if args.dry_run:
        available_versions = available_versions[:-1]
    current_versions = set(available_versions)
    homeassistant_versions = get_available_versions(homeassistant_root)
    available_pypi_versions = set(get_pypi_versions())
    missing_versions = [
        version
        for version in homeassistant_versions
        if version not in current_versions and version in available_pypi_versions
    ]
    for version in missing_versions:
        LOGGER.info("Missing version: %s", version)

    # Create new packages
    for version in missing_versions:
        create_package(
            version,
            repo_root,
            homeassistant_root,
            args.dry_run,
        )
    return 0


def get_pypi_versions() -> list[str]:
    """Get list of available versions on PyPI."""
    url = "https://pypi.org/pypi/homeassistant/json"
    with urlopen(url) as response:
        data = json.loads(response.read())
    return list(data["releases"].keys())


def get_available_versions(git_root: Path) -> list[str]:
    """Get list of available versions from git tags."""
    LOGGER.info("Getting list of available versions in %s...", git_root)
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
    for version in versions[-10:]:
        LOGGER.info("Available version: %s", version.string)
    return [version.string for version in versions]


def get_github_repo(token_name: str) -> Repository:
    """Return Github repository to use its APIs."""
    github_token = os.environ.get(token_name)
    assert github_token is not None, f"{token_name} is not set"
    github = Github(auth=Auth.Token(github_token))
    return github.get_repo("KapJI/homeassistant-stubs")


def create_package(
    version: str,
    repo_root: Path,
    homeassistant_root: Path,
    dry_run: bool,
) -> None:
    """Create package for given version and upload it to PyPI."""
    LOGGER.info("Creating package for %s...", version)
    update_dependency(repo_root, version)
    checkout_version(homeassistant_root, version)
    typed_paths = get_typed_paths(homeassistant_root)
    generate_stubs(typed_paths, repo_root)
    if not dry_run:
        create_commit(repo_root, version)
        gh_repo = get_github_repo("GITHUB_TOKEN")
        gh_admin_repo = get_github_repo("ADMIN_TOKEN")
        push_commit(repo_root, gh_admin_repo)
        create_github_release(version, gh_repo)
        build_package(repo_root, version)
        publish_package(repo_root)


def update_dependency(repo_root: Path, version: str) -> None:
    """Update version of homeassistant dependency."""
    subprocess.run(
        ["uv", "add", f"homeassistant=={version}"], cwd=repo_root, check=True
    )


def checkout_version(homeassistant_root: Path, version: str) -> None:
    """Checkout required version of Home Assistant repo."""
    subprocess.run(["git", "checkout", version], cwd=homeassistant_root, check=True)


def build_package(repo_root: Path, version: str) -> None:
    """Build new package with uv."""
    LOGGER.info("Building package...")
    subprocess.run(["git", "tag", version], cwd=repo_root, check=True)
    subprocess.run(["uv", "build"], cwd=repo_root, check=True)
    subprocess.run(["git", "tag", "--delete", version], cwd=repo_root, check=True)


def create_commit(repo_root: Path, version: str) -> None:
    """Create local commit."""
    LOGGER.info("Creating commit for %s...", version)
    subprocess.run(
        [
            "git",
            "add",
            "homeassistant_core",
            "homeassistant-stubs",
            "pyproject.toml",
            "uv.lock",
        ],
        cwd=repo_root,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", f"Generate v{version}"], cwd=repo_root, check=True
    )


def push_commit(repo_root: Path, gh_admin_repo: Repository) -> None:
    """Push commit to Github."""
    LOGGER.info("Disabling branch protection...")
    branch = gh_admin_repo.get_branch("main")
    required_checks = branch.get_required_status_checks()
    branch.edit_required_status_checks(required_checks.strict, [])

    LOGGER.info("Pushing new commit...")
    subprocess.run(["git", "push"], cwd=repo_root, check=True)

    LOGGER.info("Re-enabling branch protection...")
    branch.edit_required_status_checks(required_checks.strict, required_checks.contexts)


def create_github_release(version: str, gh_repo: Repository) -> None:
    """Create new release on Github."""
    LOGGER.info("Creating release...")
    gh_repo.create_git_release(
        tag=version,
        name=version,
        target_commitish="main",
        message=f"Generated for `homeassistant {version}`.",
        prerelease=AwesomeVersion(version).modifier is not None,
    )


def publish_package(repo_root: Path) -> None:
    """Publish new package on PyPI."""
    LOGGER.info("Publishing package...")
    subprocess.run(
        [
            "uvx",
            "twine",
            "upload",
            "--non-interactive",
            "--disable-progress-bar",
            "--skip-existing",
            "dist/*",
        ],
        cwd=repo_root,
        check=True,
    )
    LOGGER.info("Removing all files in dist...")
    shutil.rmtree("dist")


def get_typed_paths(homeassistant_root: Path) -> list[Path]:
    """Get list of strictly typed paths from Home Assistant config."""
    strict_path = homeassistant_root / ".strict-typing"
    if strict_path.is_file():
        LOGGER.info("Use modern typed paths")
        return get_modern_typed_paths(homeassistant_root, strict_path)
    LOGGER.info("Use old style typed paths")
    return get_old_typed_paths(homeassistant_root)


def module_to_path(homeassistant_root: Path, module: str) -> Path:
    """Convert module name to Path."""
    if module.endswith(".*"):
        typed_path = homeassistant_root / Path(module[:-2].replace(".", os.path.sep))
        assert typed_path.is_dir(), typed_path
    else:
        module = module.replace(".", os.path.sep)
        typed_path = homeassistant_root / (module + ".py")
        if not typed_path.is_file():
            typed_path = homeassistant_root / module
            assert typed_path.is_dir()
            typed_path = typed_path / "__init__.py"
    return typed_path


def get_modern_typed_paths(homeassistant_root: Path, strict_path: Path) -> list[Path]:
    """Get list of strictly typed paths after configuration was moved to mypy.ini."""
    package_root = homeassistant_root / "homeassistant"
    core_paths = [
        path
        for path in package_root.iterdir()
        if path.name != "components"
        and (
            (path.is_dir() and (path / "__init__.py").is_file())
            or path.name.endswith(".py")
        )
    ]

    with strict_path.open() as fp:
        lines = [line.strip() for line in fp.readlines()]
    strict_modules = [
        line
        for line in lines
        if line != ""
        and not line.startswith("#")
        and line.startswith("homeassistant.components")
    ]
    components_paths = [
        module_to_path(homeassistant_root, module) for module in strict_modules
    ]
    return core_paths + components_paths


def get_old_typed_paths(homeassistant_root: Path) -> list[Path]:
    """Get list of strictly typed paths before configuration was moved to mypy.ini."""
    cfg_path = homeassistant_root / "setup.cfg"
    matched_lines: list[str] = []
    with cfg_path.open() as fp:
        matched_lines = [line for line in fp.readlines() if line.startswith("[mypy-")]
    if not matched_lines:
        raise ValueError("can't find mypy config in setup.cfg")
    expected_matched_lines = 2
    if len(matched_lines) > expected_matched_lines:
        raise ValueError("too many mypy entries in setup.cfg, update the script")
    mypy_config = matched_lines[0][len("[mypy-") : -len("]\n")]
    typed_paths: list[Path] = []
    mypy_entries = mypy_config.split(",")
    for item in mypy_entries:
        if not item.startswith("homeassistant."):
            continue
        # Skip if module is already added as module.*
        if item + ".*" in mypy_entries:
            continue
        typed_paths.append(module_to_path(homeassistant_root, item))
    return typed_paths


def generate_stubs(typed_paths: list[Path], repo_root: Path) -> None:
    """Use stubgen to generate typing stubs for all typed paths."""
    LOGGER.info("Generating stubs...")
    with tempfile.NamedTemporaryFile("w", delete_on_close=False) as f:
        f.write("\n".join(map(str, typed_paths)))
        f.close()
        command_args: list[str] = [
            "uv",
            "run",
            "stubgen",
            "--include-private",
            "-o",
            str(repo_root),
            f"@{f.name}",
        ]
        LOGGER.info("Running: %s", " ".join(command_args))
        subprocess.run(command_args, cwd=repo_root, check=True)
    stubs_folder = repo_root / "homeassistant"
    new_stubs_folder = repo_root / "homeassistant-stubs"
    if new_stubs_folder.is_dir():
        shutil.rmtree(new_stubs_folder)
    stubs_folder.rename(new_stubs_folder)
    stubs_fixup(new_stubs_folder)


def stubs_fixup(stubs_folder: Path) -> None:
    """Fix invalid syntax in generated files."""
    LOGGER.info("Fixing stubs...")

    # Run the 'find' command and capture the output
    find_command = ["find", str(stubs_folder), "-name", "*.pyi", "-print0"]
    sed_command = ["xargs", "-0", "sed", "-i"]

    # MacOS needs an additional empty argument
    if platform.system() == "Darwin":
        sed_command.append("")
    sed_command.append("/def __mypy-replace/d")

    with subprocess.Popen(find_command, stdout=subprocess.PIPE) as find_process:
        # Pipe the output of 'find' into 'xargs sed'
        subprocess.run(sed_command, stdin=find_process.stdout, check=True)


if __name__ == "__main__":
    sys.exit(main())
