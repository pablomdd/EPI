import collections

PairedTasks = collections.namedtuple('PairedTask', ('task1', 'task2'))

def task_pairing(task_durations: list[int], ) -> list[PairedTasks]:
    task_durations.sort()

    return [PairedTasks(task_durations[i], task_durations[~i]) for i in range(len(task_durations) // 2)]


tasks = [5, 2, 1, 6, 4, 4]
print(task_pairing(tasks))