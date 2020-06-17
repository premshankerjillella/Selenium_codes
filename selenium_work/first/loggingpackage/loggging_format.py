import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("This is an error  message")

