#!/usr/bin/env python
# coding: utf-8
# yc@2014/04/01

'''
A Simple Threadpool
'''

from Queue import Queue, Empty
from threading import Thread


__all__ = ['ThreadPool']


class ThreadPool(object):
  '''
  A Simple Threadpool
  '''
  def __init__(self, size, worker):
    self.queue = Queue()
    self.closed = False
    for i in range(size):
      j = Thread(target=self.worker, args=(worker,))
      #j.daemon = True
      j.start()

  def worker(self, worker):
    '''
    worker
    '''
    while True:
      try:
        if self.closed:
          return
        worker(self.queue.get(timeout=1))
      except Empty:
        continue
      except:
        self.queue.task_done()
        raise
      self.queue.task_done()

  def feed(self, items):
    '''
    feeds till done
    '''
    map(self.queue.put, iter(items))
    self.queue.join()

  def close(self):
    '''
    explicit close queue
    '''
    self.closed = True
