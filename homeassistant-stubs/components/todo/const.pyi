from enum import IntFlag, StrEnum

DOMAIN: str
ATTR_DUE: str
ATTR_DUE_DATE: str
ATTR_DUE_DATETIME: str
ATTR_DESCRIPTION: str
ATTR_ITEM: str
ATTR_RENAME: str
ATTR_STATUS: str

class TodoServices(StrEnum):
    ADD_ITEM = 'add_item'
    UPDATE_ITEM = 'update_item'
    REMOVE_ITEM = 'remove_item'
    GET_ITEMS = 'get_items'
    REMOVE_COMPLETED_ITEMS = 'remove_completed_items'

class TodoListEntityFeature(IntFlag):
    CREATE_TODO_ITEM = 1
    DELETE_TODO_ITEM = 2
    UPDATE_TODO_ITEM = 4
    MOVE_TODO_ITEM = 8
    SET_DUE_DATE_ON_ITEM = 16
    SET_DUE_DATETIME_ON_ITEM = 32
    SET_DESCRIPTION_ON_ITEM = 64

class TodoItemStatus(StrEnum):
    NEEDS_ACTION = 'needs_action'
    COMPLETED = 'completed'
