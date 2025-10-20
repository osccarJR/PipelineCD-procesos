"""Task Manager - A professional task management application."""

__version__ = "1.0.0"
__author__ = "Senior Dev Team"

from .task import Task, TaskStatus, TaskPriority
from .task_manager import TaskManager
from .exceptions import TaskNotFoundError, DuplicateTaskError, ValidationError

__all__ = [
    "Task",
    "TaskStatus",
    "TaskPriority",
    "TaskManager",
    "TaskNotFoundError",
    "DuplicateTaskError",
    "ValidationError",
]
