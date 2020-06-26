'''
I don’t think I was ever taught or tasked to implement a deadlock. But I can proudly say that I have successfully managed to implement them quite a few times.
This series should be for fun, so why not to implement one more today?
I will run a certain number of workers in a separate threads. Imagine the workers are arranged in a circle and there is a single resource to be acquired between each pair of workers.
The worker is identified by its #pid and to be able to do its task, it has to acquire an exclusive access to resources #pid and #pid-1.
How can a deadlock happen?
each worker W[pid] acquires resource R[pid]
each worker W[pid] is waiting for resource R[pid-1] to be released
quiz time
Here’s the expected behaviour of my program:
N workers are repeatedly acquiring and releasing shared resources
main thread is waiting for deadlock
once deadlock is detected, main thread releases all locks causing RuntimeError in each thread
Implementation note: any thread can release any previously acquired Lock since the lock is not reentrant; but attempt to release free lock results in RuntimeError
My question for you: Are you able to find and identify a bug in my program without running it? Consider bug any behaviour that deviates from the three bullets above.
'''
from collections import defaultdict
from time import sleep
from threading import Thread, Lock

#shared state
class SharedState:
    def __init__(self, n):
        self._lock = Lock()
        self._state = defaultdict(int)
        self._resources = [Lock() for _ in range(n)]
    def atomic(self, key, value=0):
        with self._lock:
            self._state[key] += value
            return self._state[key]
    def resource(self, i):
        return self._resources[i]
    def kill(self):
        resources = self._resources
        self._resources = None
        for i in resources:
            i.release()
# Algorithm
def worker(pid, state):
    try:
        while True:
            state.atomic('waiting', 1)
            with state.resource(pid):
                state.atomic('waiting', 1)
                with state.resource(pid - 1):
                    state.atomic('waiting', -2)
                    state.atomic('tasks', 1)
    except RuntimeError:
        pass
def deadlock(n):
    state = SharedState(n)
    for i in range(n):
        Thread(target=worker, args=(i, state)).start()
    while state.atomic('waiting') < 2 * n:
        sleep(1)
    print(n, 'workers; deadlock after', \
          state.atomic('tasks'), 'tasks')
    state.kill()

# Run
for i in range(1, 10):
    deadlock(10 * i)
