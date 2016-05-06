import logging


def getlogger(name):
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s] [%(module)s]  %(message)s")
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("example.log")
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(logging.INFO)
    logger.addHandler(consoleHandler)
    return logger
