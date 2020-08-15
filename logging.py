import logging
from datetime import datetime,date

##### logging script
# Gets or creates a logger
logger = logging.getLogger(__name__)  
# set log level
logger.setLevel(logging.INFO)
# define file handler and set formatter
log_file = str(date.today().strftime("%d%m%Y"))
file_handler = logging.FileHandler('Agency_log_'+log_file+'.txt')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
file_handler.setFormatter(formatter)
# add file handler to logger
logger.addHandler(file_handler)



logger.info('Identified and created list of all the folders from csv')