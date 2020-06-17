# Logging levels:
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
# Thresholf is set only for messages more than warning

import logging

logging.basicConfig(filename="test.log",level=logging.DEBUG)


logging.warning("warning message")
logging.info("info message")
logging.error("This is an error  message")
