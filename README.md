# Intro
simple\_threadpool: a simple threadpool


# Install

```bash
pip install simple_threadpool
```

# Usage

```python
import random, time
from threading import current_thread
from simple_threadpool import ThreadPool


def my_worker(arg):
  '''
  custom worker
  '''
  time.sleep(random.random())
  print '%s: ' % current_thread().name, arg + 1


# create a ThreadPool instance with 4 Threads and a callback
tp = ThreadPool(4, my_worker)

# produce and send some data to the pool
print 'First round:'
tp.feed([1, 2, 3, 4, 5])

# you can feed any times
print 'Second round:'
tp.feed([6, 7, 8, 9, 0])

# close the queue
tp.close()
```
