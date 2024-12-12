def schedule_tasks(task_hierarchy):
    if not task_hierarchy:
        return []

    sorted_tasks = sorted(
        task_hierarchy,
        key=lambda task: (-task.get("priority", 0), task["id"])
    )

    scheduled_tasks = []

    for task in sorted_tasks:
        scheduled_tasks.append(task["id"])
        if "subtasks" in task and task["subtasks"]:
            scheduled_tasks.extend(schedule_tasks(task["subtasks"]))

    return scheduled_tasks


if __name__ == "__main__":
    tasks = [
        {"id": 1, "name": "Task A", "priority": 2, "subtasks": [
            {"id": 2, "name": "Task A1", "priority": 3},
            {"id": 3, "name": "Task A2", "priority": 1}
        ]},
        {"id": 4, "name": "Task B", "priority": 1}
    ]

    print(schedule_tasks(tasks))

    tasks = [
        {"id": 1, "name": "Task A", "subtasks": [
            {"id": 2, "name": "Task A1"},
            {"id": 3, "name": "Task A2"}
        ]},
        {"id": 4, "name": "Task B"}
    ]

    print(schedule_tasks(tasks))

    tasks = [
        {"id": 1, "name": "Root Task", "priority": 5, "subtasks": [
            {"id": 2, "name": "Subtask 1", "priority": 3, "subtasks": [
                {"id": 3, "name": "Subtask 1.1", "priority": 2},
                {"id": 4, "name": "Subtask 1.2", "priority": 4}
            ]},
            {"id": 5, "name": "Subtask 2", "priority": 1}
        ]}
    ]

    print(schedule_tasks(tasks))
