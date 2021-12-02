import logging
import os
from logging.handlers import RotatingFileHandler



logFile = os.getcwd() + "\\log\\BO_Aufraeumen.log"
formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')

fh = RotatingFileHandler(logFile, mode='a', maxBytes=5*102*102, 
                                 backupCount=2, encoding=None, delay=0)

logger = logging.getLogger('log.log')
logger.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
fh.setFormatter(formatter)
logger.addHandler(fh)

#while True:
 #   logger.info("data")

# Beispielnachrichten zum testen
#logger.debug('Debug-Nachricht')
#logger.info('Info-Nachricht')
#logger.warning('Warnhinweis')
#logger.error('Fehlermeldung')
#logger.critical('Schwerer Fehler')