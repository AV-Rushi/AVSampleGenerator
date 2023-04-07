import logging
import os

if not os.path.isdir("Logs"):
    os.makedirs("Logs")

logging.basicConfig(filename="Logfile.log",
                format='%(asctime)s %(message)s',
                filemode='w')
# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
# logger.setLevel(logging.CRITICAL)
# logger.setLevel(logging.ERROR)
# logger.setLevel(logging.WARNING)
