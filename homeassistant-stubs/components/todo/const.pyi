from enum import IntFlag, StrEnum

DOMAIN: str
ATTR_DUE: str
ATTR_DUE_DATE: str
ATTR_DUE_DATETIME: str
ATTR_DESCRIPTION: str

class TodoListEntityFeature(IntFlag):
    CREATE_TODO_ITEM: int
    DELETE_TODO_ITEM: int
    UPDATE_TODO_ITEM: int
    MOVE_TODO_ITEM: int
    SET_DUE_DATE_ON_ITEM: int
    SET_DUE_DATETIME_ON_ITEM: int
    SET_DESCRIPTION_ON_ITEM: int

class TodoItemStatus(StrEnum):
    NEEDS_ACTION: str
    COMPLETED: str
