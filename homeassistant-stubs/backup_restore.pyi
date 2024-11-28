from _typeshed import Incomplete
from dataclasses import dataclass
from pathlib import Path

RESTORE_BACKUP_FILE: str
KEEP_PATHS: Incomplete
_LOGGER: Incomplete

@dataclass
class RestoreBackupFileContent:
    backup_file_path: Path
    def __init__(self, backup_file_path) -> None: ...

def restore_backup_file_content(config_dir: Path) -> RestoreBackupFileContent | None: ...
def _clear_configuration_directory(config_dir: Path) -> None: ...
def _extract_backup(config_dir: Path, backup_file_path: Path) -> None: ...
def restore_backup(config_dir_path: str) -> bool: ...
