journal = ["task-0"]

def rough_estimate(queue):
    queue = []
    queue.append("task-1")
    return len(queue)

def register(queue):
    queue.append("task-1")
    return len(queue)

def point_fix(queue):
    queue[0] = "task-X"

print(rough_estimate(journal), journal)
print(register(journal), journal)
point_fix(journal)
print("after fix:", journal)
