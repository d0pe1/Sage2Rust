# Agent Operating Protocol

This file defines the roles and rules for all agents working in this repository. Every agent must read and understand these instructions before performing any task.

## Roles

### PlannerAgent
- Reads `projectscope.md` and generates a dependency graph (DAG).
- Records milestones in `agent_tasks.md` and atomic subtasks in `agent_prio.md`.
- Each task entry must include a UUID, description, context/why, depends_on list and priority.
- Updates `manifest.json` with new artifacts and produces the `taskmap.svg` Gantt overlay.
- Commits all updated state files before ExecutorAgents may work.
- Will run if all tasks in agent_tasks.md are marked complete to do a final project review and hand it to the MetaStateChecker.

### ExecutorAgent
- Pulls unblocked tasks from `agent_prio.md` using the associated UUID and context.
- Implements the task, updates related files, and logs progress in `DevDiary.md`.
- Marks tasks `[x]` only when work is complete and integrated.
- If blocked or context is missing, mark the task `[u]` (requires user input) or `[a]` (needs additional planning) and document the issue.
- When task is done and marked complete, will tell the PlannerAgent to check if Milestone is also complete for update.

### MetaStateCheckerAgent
- Audits `agent_tasks.md`, `agent_prio.md` and `manifest.json` for inconsistencies.
- Performs a comparison between the expected and actual state to detect misimplementations or logical errors.
- This includes full source audits! Scope, Implementation, Interconnection of Systems, all to make the project COMPLETE
- Flags stale or broken tasks by setting their status to `[u]` or `[a]` and logs details in `DevDiary.md`.
- Must run after each milestone or significant plan update.
- Cannot modify tasks beyond applying flags; escalate problems to PlannerAgent.

## Escalation Markers
- `[ ]` task ready to work
- `[x]` task completed and integrated
- `[a]` task requires additional subtasks
- `[u]` user input or clarification needed

When an agent encounters a blocker, they must document it in `DevDiary.md`, update the task status appropriately, and halt work until PlannerAgent resolves the issue.

## Programmatic Checks
If any tests or lint scripts exist in the repository, agents must run them before committing changes. When dependencies are missing, attempt installation or escalate with details in `DevDiary.md`.

