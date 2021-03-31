from . import Recorder as Recorder
from .const import MAX_ROWS_TO_PURGE as MAX_ROWS_TO_PURGE
from .models import Events as Events, RecorderRuns as RecorderRuns, States as States
from .repack import repack_database as repack_database
from .util import session_scope as session_scope
from sqlalchemy.orm.session import Session as Session

def purge_old_data(instance: Recorder, purge_days: int, repack: bool, apply_filter: bool=...) -> bool: ...
