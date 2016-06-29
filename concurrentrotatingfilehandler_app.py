from logging import getLogger, INFO
from multiprocessing import Pool
from cloghandler import ConcurrentRotatingFileHandler
import os
from subproc_concurrent import test

log = getLogger()
# Use an absolute path to prevent file rotation trouble.
logfile = os.path.abspath("mylogfile.log")
# Rotate log after reaching 512K, keep 5 old copies.
rotateHandler = ConcurrentRotatingFileHandler(logfile, "a", 512*1024, 5)
log.addHandler(rotateHandler)
log.setLevel(INFO)

if __name__ == '__main__':

    test('begin')
    p = Pool(4)
    p.map(test, range(100000))
    test('end')
