# Active Subtasks

- uuid: ST-0001
  parent: TSK-0001
  description: Write README and agent protocol
  depends_on: []
  status: [x]

- uuid: ST-0002
  parent: TSK-0001
  description: Scaffold state files with example content
  depends_on: [ST-0001]
  status: [x]

- uuid: ST-0003
  parent: TSK-0002
  description: Create DAG parser skeleton
  depends_on: [ST-0002]
  status: [x]
