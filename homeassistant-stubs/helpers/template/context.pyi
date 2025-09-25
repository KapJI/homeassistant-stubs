import jinja2
from _typeshed import Incomplete
from contextlib import AbstractContextManager
from contextvars import ContextVar
from types import TracebackType
from typing import Any

template_cv: ContextVar[tuple[str, str] | None]

class TemplateContextManager(AbstractContextManager):
    def set_template(self, template_str: str, action: str) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...

template_context_manager: Incomplete

def render_with_context(template_str: str, template: jinja2.Template, **kwargs: Any) -> str: ...
