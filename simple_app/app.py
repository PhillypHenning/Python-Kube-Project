from time import sleep
import logging
count=0
max_count=120

def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

if __name__ == "__main__":

    lh = get_module_logger(__name__)
    lh.info("APPLICATION STARTED!")
    while count < max_count:
        count += 1
        lh.info(f"COUNT AT: {count}")
        sleep(1)
    lh.info("APPLICATION ENDED!")