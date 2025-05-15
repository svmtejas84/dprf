def recover_from_deadlock(allocation, available, max_demand=None, strategy="terminate"):
    """
    Recovery strategies:
    - "terminate": Terminate the process holding the most resources.
    - "preempt": Preempt resources from the process holding the most resources (release all its resources).
    - "rollback": Rollback a process to a safe state (simulated as releasing all its resources).
    Returns a dict with victim and released resources.
    """
    if not allocation or not available:
        return None

    num_processes = len(allocation)
    num_resources = len(available)

    # Find the process holding the most resources (exclude terminated processes)
    max_resources = -1
    victim = -1
    for i, alloc in enumerate(allocation):
        total = sum(alloc)
        # Check if process is not already terminated (max_demand all 0)
        if max_demand and all(max_demand[i][j] == 0 for j in range(num_resources)):
            continue
        if total > max_resources:
            max_resources = total
            victim = i

    if victim == -1:
        return None

    released = allocation[victim][:]
    if strategy == "terminate":
        # Terminate the process and release its resources
        for j in range(num_resources):
            available[j] += allocation[victim][j]
            allocation[victim][j] = 0
        # Also set max_demand to 0 if provided (indicating process is out of system)
        if max_demand:
            for j in range(num_resources):
                max_demand[victim][j] = 0
        print(f"Terminated P{victim}. Released: {released}, New Available: {available}")
        return {"victim": victim, "released": released}

    elif strategy == "preempt":
        # Preempt all resources from the victim process
        for j in range(num_resources):
            available[j] += allocation[victim][j]
            allocation[victim][j] = 0
        print(f"Preempted P{victim}. Released: {released}, New Available: {available}")
        return {"victim": victim, "released": released}

    elif strategy == "rollback":
        # Rollback by releasing all resources of the victim process
        for j in range(num_resources):
            available[j] += allocation[victim][j]
            allocation[victim][j] = 0
        print(f"Rolled back P{victim}. Released: {released}, New Available: {available}")
        return {"victim": victim, "released": released}

    return None
