import logging

logger = logging.getLogger(__name__)


class Command2(object):
    def __init__(self, opts):
        self.opts = opts

    def exec(self):
        logger.info('The command2 is called')
