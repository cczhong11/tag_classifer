import logging, functools, sys
import json

import os
from pathlib import Path
PATH = str(Path(__file__).parent.absolute())
logging.basicConfig(filename=f"{PATH}/../move.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=logging.DEBUG)
logger = logging.getLogger()

def log_decorator_info(func):
    @functools.wraps(func)
    def log_decorator_wrapper(self, *args, **kwargs):
        try:
            """ log return value from the function """
            value = func(self, *args, **kwargs)
                
            logger.info(f"move file {args[0]} to {args[1]} ")
        except:
            """log exception if occurs in function"""
            logger.error(f"Exception: {str(sys.exc_info()[1])}")
            raise
        return value
    return log_decorator_wrapper


class MoverBase(object):
    base_folder = ""
    def __init__(self, base_folder):
        self.base_folder = base_folder
        
    def move(self, file, tag):
        pass
