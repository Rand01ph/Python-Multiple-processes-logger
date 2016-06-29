import logging
from multiprocessing import Pool
import os
from datetime import datetime
from cloghandler import ConcurrentRotatingFileHandler
from subproc import test

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    import logging.config
    import yaml

    path = 'logging.yaml'
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)

    test_list = []

    test('begin')

    p = Pool(4)

    p.map(test, range(100000))

    test('end')
