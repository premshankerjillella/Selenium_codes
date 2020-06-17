import logging


class LoggerDemmoConsole():

    def testLog(self):
        logger = logging.getLogger(LoggerDemmoConsole.__name__)
        logger.setLevel(logging.INFO)

        # create console handler and set level to INFO
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
        # add formatter to console handler
        chandler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(chandler)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('Warning message')
        logger.error('error message')
        logger.critical('critical message')

ct = LoggerDemmoConsole()
ct.testLog()
