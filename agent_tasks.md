# Milestone Tasks
### ***Project Milestones:***

- uuid: accd5429-3d72-456e-a400-82fc9c9ee308
  description: Milestone 1 - Basic INI parsing via sage_ini crate
  why: Enables loading of original SAGE configuration files
  depends_on: []
  priority: 1
  status: [x]

- uuid: 2e183199-ee32-469e-89e8-8a89086fc781
  description: Milestone 2 - ECS architecture and entity manager
  why: Needed to spawn and manage units
  depends_on: [accd5429-3d72-456e-a400-82fc9c9ee308]
  priority: 2
  status: [x]
- uuid: 7c9c38d0-c864-4e87-ac4f-9df7a9e7e9e5
  description: Milestone 3 - Legacy engine function mapping
  why: Generate a comprehensive map of the Generals Zero Hour codebase for future Rust rewrite planning
  depends_on: [2e183199-ee32-469e-89e8-8a89086fc781]
  priority: 3
  status: [ ]
