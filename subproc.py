import logging
import os
logger = logging.getLogger(__name__)


def test(value):
    msg = '[{}] value 2016-06-23 16:07:26,347 INFO [2435:MainProcess] /home/tan/Hato/trunk/api/event/views.py views views.py list 153 request event list and query_params is <QueryDict:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff> {}'.format(os.getpid(), value)
    logger.info(msg)
