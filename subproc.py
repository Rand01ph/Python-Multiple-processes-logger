import logging
import os
logger = logging.getLogger(__name__)


def test(value):
    msg = '[{}] ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff> {}'.format(os.getpid(), value)
    logger.info(msg)
