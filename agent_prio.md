# Active Subtasks

### ***Agent Prio Tasks:***

- uuid: 389dcc53-5f10-4444-a7fe-2c5c9c3aca1a
  parent: accd5429-3d72-456e-a400-82fc9c9ee308
  description: Setup Cargo workspace and create sage_core and sage_ini crates
  why: Provide initial project structure for development
  depends_on: []
  status: [x]

- uuid: 085452b0-4b67-44e3-885c-e5eb134b8eb0
  parent: accd5429-3d72-456e-a400-82fc9c9ee308
  description: Implement initial INI parser supporting sections and key/value pairs
  why: Allows engine to read configuration files
  depends_on: [389dcc53-5f10-4444-a7fe-2c5c9c3aca1a]
  status: [x]

- uuid: f5ec9d53-4942-4514-ad7a-6b2ef346b36f
  parent: accd5429-3d72-456e-a400-82fc9c9ee308
  description: Add unit tests verifying INI parser compatibility
  why: Ensure parser behaves like original SAGE engine
  depends_on: [085452b0-4b67-44e3-885c-e5eb134b8eb0]
  status: [x]

- uuid: 38cac826-a4dd-4717-847e-f00d305be18f
  parent: accd5429-3d72-456e-a400-82fc9c9ee308
  description: Update README with build and usage instructions
  why: Document how to compile and run the project
  depends_on: [389dcc53-5f10-4444-a7fe-2c5c9c3aca1a]
  status: [x]
- uuid: 0404634f-46e1-4eda-9320-e1d5af984ad0
  parent: 2e183199-ee32-469e-89e8-8a89086fc781
  description: Add ECS module scaffolding in sage_core
  why: Provide base types for entities and components
  depends_on: []
  status: [x]

- uuid: ae9319e7-8714-4d44-b54b-7b33c9a95435
  parent: 2e183199-ee32-469e-89e8-8a89086fc781
  description: Implement entity manager with world storage
  why: Manage entities and associated components
  depends_on: [0404634f-46e1-4eda-9320-e1d5af984ad0]
  status: [x]

- uuid: f281dc05-b06e-4695-bb1a-f76f21266abc
  parent: 2e183199-ee32-469e-89e8-8a89086fc781
  description: Provide spawn_unit helper to create entities
  why: Allows engine to instantiate units from data
  depends_on: [ae9319e7-8714-4d44-b54b-7b33c9a95435]
  status: [x]

- uuid: dca97530-e53b-471f-8205-f83f090805d9
  parent: 2e183199-ee32-469e-89e8-8a89086fc781
  description: Add unit tests covering entity creation
  why: Verify ECS works as intended
  depends_on: [f281dc05-b06e-4695-bb1a-f76f21266abc]
  status: [x]

- uuid: 15a64eb8-3c52-4c74-99a1-61c6247728e2
  parent: 2e183199-ee32-469e-89e8-8a89086fc781
  description: Document ECS usage in README
  why: Explain how to create and manage entities
  depends_on: [dca97530-e53b-471f-8205-f83f090805d9]
  status: [x]
- uuid: 22f7f035-c8c4-41d4-87e4-7393fd8efdc9
  parent: 7c9c38d0-c864-4e87-ac4f-9df7a9e7e9e5
  description: Create engine_map script using Ctags to list functions
  why: Automated enumeration is required to handle thousands of legacy functions
  depends_on: []
  status: [ ]

- uuid: 651b0f03-067a-45f7-bf3c-dcccb2c9cb1b
  parent: 7c9c38d0-c864-4e87-ac4f-9df7a9e7e9e5
  description: Generate function list for GameLogic subsystem
  why: First dataset segment for mapping
  depends_on: [22f7f035-c8c4-41d4-87e4-7393fd8efdc9]
  status: [ ]

- uuid: eae6dbe3-9be8-4026-96ce-b22ead041f0c
  parent: 7c9c38d0-c864-4e87-ac4f-9df7a9e7e9e5
  description: Map GameClient subsystem functions
  why: Capture rendering and UI code relationships
  depends_on: [651b0f03-067a-45f7-bf3c-dcccb2c9cb1b]
  status: [ ]

- uuid: d782e0c1-fb67-4a02-bbab-d89d517161e4
  parent: 7c9c38d0-c864-4e87-ac4f-9df7a9e7e9e5
  description: Map GameNetwork subsystem functions
  why: Document networking paths
  depends_on: [eae6dbe3-9be8-4026-96ce-b22ead041f0c]
  status: [ ]

- uuid: 81f2de0d-07bd-41a0-9dea-509577029967
  parent: 7c9c38d0-c864-4e87-ac4f-9df7a9e7e9e5
  description: Consolidate data and output full function_map.md and function_graph.json
  why: Provide complete DAG for planners and developers
  depends_on: [d782e0c1-fb67-4a02-bbab-d89d517161e4]
  status: [ ]
