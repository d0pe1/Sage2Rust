"""
DAG Parser Skeleton for SelfPlanner Agents.

This module provides basic utilities to read task definitions from
`agent_tasks.md` and `agent_prio.md` and construct in-memory 
representations of the dependency graph. Future PlannerAgent implementations 
can extend this module with more sophisticated parsing and validation logic.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


# ------------------------------
# Data Structures
# ------------------------------

@dataclass
class Task:
    """Represents a single milestone task node in the dependency graph."""
    uuid: str
    description: str
    depends_on: List[str] = field(default_factory=list)


@dataclass
class SubTask:
    """Represents a single atomic subtask node in the dependency graph."""
    uuid: str
    parent: str
    description: str
    depends_on: List[str] = field(default_factory=list)


# ------------------------------
# Parsers
# ------------------------------

def parse_agent_tasks(path: Path) -> Dict[str, Task]:
    """Parse tasks from `agent_tasks.md` into Task objects."""
    tasks: Dict[str, Task] = {}
    current: Dict[str, str] = {}

    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("- uuid:"):
            # Finish the previous task if one is being built
            if current:
                tasks[current["uuid"]] = Task(
                    uuid=current["uuid"],
                    description=current.get("description", ""),
                    depends_on=current.get("depends_on", []),
                )
                current = {}
            current["uuid"] = line.split("uuid:", 1)[1].strip()
        elif line.startswith("description:"):
            current["description"] = line.split("description:", 1)[1].strip()
        elif line.startswith("depends_on:"):
            deps = line.split("depends_on:", 1)[1].strip().strip("[]")
            current["depends_on"] = [d.strip() for d in deps.split(",") if d.strip()]

    # Add last task if any
    if current:
        tasks[current["uuid"]] = Task(
            uuid=current["uuid"],
            description=current.get("description", ""),
            depends_on=current.get("depends_on", []),
        )

    return tasks


def parse_agent_prio(path: Path) -> Dict[str, SubTask]:
    """Parse subtasks from `agent_prio.md` into SubTask objects."""
    subtasks: Dict[str, SubTask] = {}
    current: Dict[str, str] = {}

    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("- uuid:"):
            if current:
                subtasks[current["uuid"]] = SubTask(
                    uuid=current["uuid"],
                    parent=current.get("parent", ""),
                    description=current.get("description", ""),
                    depends_on=current.get("depends_on", []),
                )
                current = {}
            current["uuid"] = line.split("uuid:", 1)[1].strip()
        elif line.startswith("parent:"):
            current["parent"] = line.split("parent:", 1)[1].strip()
        elif line.startswith("description:"):
            current["description"] = line.split("description:", 1)[1].strip()
        elif line.startswith("depends_on:"):
            deps = line.split("depends_on:", 1)[1].strip().strip("[]")
            current["depends_on"] = [d.strip() for d in deps.split(",") if d.strip()]

    if current:
        subtasks[current["uuid"]] = SubTask(
            uuid=current["uuid"],
            parent=current.get("parent", ""),
            description=current.get("description", ""),
            depends_on=current.get("depends_on", []),
        )

    return subtasks


# ------------------------------
# DAG Builder
# ------------------------------

def build_dag(tasks: Dict[str, Task], subtasks: Dict[str, SubTask]) -> Dict[str, List[str]]:
    """Build a simple adjacency list representing the DAG (tasks + subtasks)."""
    graph: Dict[str, List[str]] = {}

    # Add milestones
    for uuid, task in tasks.items():
        graph.setdefault(uuid, [])
        for dep in task.depends_on:
            graph.setdefault(dep, [])
            graph[dep].append(uuid)

    # Add subtasks
    for uuid, subtask in subtasks.items():
        graph.setdefault(uuid, [])
        if subtask.parent:
            graph.setdefault(subtask.parent, [])
            graph[subtask.parent].append(uuid)
        for dep in subtask.depends_on:
            graph.setdefault(dep, [])
            graph[dep].append(uuid)

    return graph


# ------------------------------
# Main (Debug Run)
# ------------------------------

def main() -> None:
    root = Path(__file__).resolve().parent.parent
    tasks_file = root / "agent_tasks.md"
    prio_file = root / "agent_prio.md"

    tasks = parse_agent_tasks(tasks_file)
    subtasks = parse_agent_prio(prio_file)
    graph = build_dag(tasks, subtasks)

    print("\n--- DAG Adjacency List ---")
    for node, edges in graph.items():
        print(f"{node}: {', '.join(edges) if edges else '[]'}")


if __name__ == "__main__":
    main()
