#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time
import sys
import logging

__author__ = "kanrfeh@outlook.com"

TOTAL = 0
MAXTIME = 0
MINTIME = 0
EXCEPT = 0
logger = logging.getLogger(name=__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("/var/log/mathilde/print_debug.log")
#ch = logging.StreamHandler()
logger.addHandler(fh)
#logger.addHandler(ch)


class PrintThread(threading.Thread):

    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.test_count = 0

    def run(self):
        self.test_performance()

    def test_performance(self):
        global TOTAL
        global MAXTIME
        global MINTIME
        global EXCEPT

        try:
            start_time = time.time()
            logger.debug("lalalala")
            sys.stdout.flush()
            time_span = time.time() - start_time

            self.maxtime(time_span)
            self.mintime(time_span)

        except Exception as e:
            print("Error: {}".format(e))
            EXCEPT += 1
        finally:
            TOTAL += 1

    def maxtime(self, time_span):
        global MAXTIME
        if time_span > MAXTIME:
            MAXTIME = time_span

    def mintime(self, time_span):
        global MINTIME
        if time_span < MINTIME:
            MINTIME = time_span


def test(thread_count):
    global TOTAL
    global MAXTIME
    global MINTIME
    global EXCEPT

    TOTAL = 0
    MAXTIME = 0
    MINTIME = 0
    EXCEPT = 0

    print("----------------task start------------------")
    start_time = time.time()
    i = 0
    TOTAL = 0
    while i < thread_count:
        t = PrintThread("thread" + str(i))
        t.start()
        i += 1

    print("----------------task end--------------------")

    print("\n\n\n")
    print("total time: {}".format(time.time()-start_time))
    print("thread_count: {}".format(thread_count))
    print("total: {}, maxtime: {}, mintime: {}, EXCEPT: {}\
    ".format(TOTAL, MAXTIME, MINTIME, EXCEPT))


if __name__ == "__main__":
    while True:
        test(1)
        time.sleep(10)
        print("\n\n\n")
