from scripte.verzeichnisAufraeumen import clearDict
from scripte.archivAufraeumen import clearArchiv

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
clearDict("x:\\BO_Berichte\\",cdTag,cdMonat,cdTag)
clearArchiv("x:\\BO_Berichte\\",caTag,caMonat,caJahr)
input("Ich bin  FERTIG Das Fenster kann jetzt geschlossen werden")
