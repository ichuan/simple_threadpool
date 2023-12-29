#!/usr/bin/env python
# coding: utf-8
# yc@2014/04/01

'''
A Simple Threadpool
'''

import multiprocessing
from threading import Thread, Lock

try:
    from Queue import Queue
except ModuleNotFoundError:
    from queue import Queue


__all__ = ['ThreadPool']


class ThreadPool(object):
    '''
    A Simple Threadpool
    '''

    def __init__(self, worker, max_workers=None, chunksize=None, result_callback=None):
        if max_workers is None:
            # as concurrent.futures.ThreadPoolExecutor
            max_workers = min(32, multiprocessing.cpu_count() + 4)
        if chunksize is None:
            chunksize = max_workers * 2
        self.max_workers = max_workers
        self.result_callback = result_callback
        self.callback_lock = Lock()
        self.queue = Queue(chunksize)
        self.close_signal = object()
        for i in range(max_workers):
            j = Thread(target=self.worker, args=(worker,))
            j.daemon = True
            j.start()

    def worker(self, worker):
        '''
        worker
        '''
        while True:
            try:
                job = self.queue.get()
                if job is self.close_signal:
                    return
                if self.result_callback:
                    with self.callback_lock:
                        self.result_callback(worker(job))
                else:
                    worker(job)
            finally:
                self.queue.task_done()

    def feed(self, items, wait=True):
        '''
        feeds till done
        '''
        for i in items:
            self.queue.put(i)
        if wait:
            self.queue.join()

    def close(self):
        '''
        explicit close queue
        '''
        for i in range(self.max_workers):
            self.queue.put(self.close_signal)
        self.queue.join()
