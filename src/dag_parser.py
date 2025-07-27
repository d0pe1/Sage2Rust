"""DAG Parser Skeleton for SelfPlanner Agents.

This module provides basic utilities to read task definitions from
`agent_tasks.md` and construct an in-memory representation of the
dependency graph. Future PlannerAgent implementations can extend this
module with more sophisticated parsing and validation logic.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


@dataclass
class Task:
    """Represents a single task node in the dependency graph."""

    uuid: str
    description: str
    depends_on: List[str] = field(default_factory=list)


def parse_agent_tasks(path: Path) -> Dict[str, Task]:
    """Parse tasks from `agent_tasks.md` into Task objects.

    The parser expects a simplified YAML-like format used in this project.
    Only the fields required for constructing the DAG are extracted.
    """
    tasks: Dict[str, Task] = {}
    current: Dict[str, str] = {}

    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("- uuid:"):
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

    if current:
        tasks[current["uuid"]] = Task(
            uuid=current["uuid"],
            description=current.get("description", ""),
            depends_on=current.get("depends_on", []),
        )

    return tasks


def build_dag(tasks: Dict[str, Task]) -> Dict[str, List[str]]:
    """Build a simple adjacency list representing the DAG."""
    graph: Dict[str, List[str]] = {uuid: [] for uuid in tasks}
    for task in tasks.values():
        for dep in task.depends_on:
            graph.setdefault(dep, [])
            graph[dep].append(task.uuid)
    return graph


def main() -> None:
    tasks_file = Path(__file__).resolve().parent.parent / "agent_tasks.md"
    tasks = parse_agent_tasks(tasks_file)
    graph = build_dag(tasks)
    for node, edges in graph.items():
        print(f"{node}: {', '.join(edges) if edges else '[]'}")


if __name__ == "__main__":
    main()
