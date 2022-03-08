from scripte.verzeichnisAufraeumen import clearDict
from scripte.archivAufraeumen import clearArchiv
from scripte.loghandler import logger as lg
from scripte.loghandler import logFile
from datetime import date

startLw="x:\\BO_Berichte\\"

# ACHTUNG alle Werte sind Tage 
#Werte ab denen die Dateien VERSCHOBEN werden - relevant fuer clearDict()
cdTag=10
cdMonat=120
cdJahr=1100
 
#Werte ab denen die Dateien GELOESCHT werden - relevant fuer clearArchiv()
caTag=120
caMonat=360
caJahr=3300

input("Wenn es los gehen kann 'ENTER' ==>>>")
lg.info(">>>>>>>> {} Aufräumen gestartet <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<".format(date.today))
clearDict(startLw,cdTag,cdMonat,cdTag)
clearArchiv(startLw,caTag,caMonat,caJahr)
input("Ich bin  FERTIG Das Fenster kann jetzt geschlossen werden")
