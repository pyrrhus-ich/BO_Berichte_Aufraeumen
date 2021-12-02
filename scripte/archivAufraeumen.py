import os
from datetime import date, datetime, timedelta
from .loghandler import logger as lg
from.loghandler import logFile

'''
Erstellt am 0.12.2021
Räumt die Archivordner auf dem Servicelaufwerk auf. Dabei ist wichtig , das die Zeitgesteuerten Bericht die folgenden Strings im Namen haben
# Tag, Monat, Quartal, Jahr => je nach ausführungsintervall
Anschliessend werden die Files nach ablauf dieser Zeit geloescht.
'''


def clearArchiv(startverzeichnis, Tgl, Mtl, Jrl):
    print("Starte Verarbeitung der überprüfung der Archivdateien")
    aktuellesDatum = date.today()
    lg.info("------- {} ---- Loeschvorgang im Archivordner gestartet ----".format(aktuellesDatum))
    workdir = startverzeichnis
    lg.info("Einlesevorgang begonnen Arbeitsverzeichnis ist :{}".format(workdir))
    maxTimeTgl = datetime.now() - timedelta(days=Tgl)
    maxTimeMtl = datetime.now() - timedelta(days=Mtl)
    maxTimeJrl = datetime.now() - timedelta(days=Jrl)
    cnt=0
    unterVerzeichnisse = os.listdir(workdir)
    lg.info("Die folgenden Verzeichnisse werden gelesen :")
    for verzeichnis in unterVerzeichnisse:
        lg.info("Verzeichnis : {}".format(verzeichnis))
        dateien = os.listdir(workdir + verzeichnis + "\\arc")
        for datei in dateien:
            datName = workdir + verzeichnis + "\\arc\\" + datei #dateiname jede reinzelnen Datei incl. Verzeichnispfad
            dateiZeit = datetime.fromtimestamp(os.path.getmtime(datName)) 
            if datei.find("Tag") > 0: # prüft ob der jeweilige Dateiname Tag|Monat|Quartal|Jahr enthält und verschiebt dann entsprechend der festlegung
                lg.info('Datei {} gefunden'.format(datei))
                if dateiZeit < maxTimeTgl:
                    os.remove(datName)
                    cnt+=1
                    lg.info("{} wurde geloescht".format(datei))
            elif datei.find("Monat") > 1 or datei.find("Quartal") > 1:
                lg.info('Datei {} gefunden'.format(datei))
                if dateiZeit < maxTimeMtl:
                    os.remove(datName)
                    cnt+=1
                    lg.info("{} wurde geloescht".format(datei))
            elif datei.find("Jahr") > 1:
                lg.info('Datei {} gefunden'.format(datei))
                if dateiZeit < maxTimeJrl:
                    os.remove(datName)
                    cnt+=1
                    lg.info("{} wurde geloescht".format(datei))          
    if cnt==0:
        lg.info("Keine Datei gefunden, die den Loeschkriterien entsprach - Es wurde also auch keine Datei geloescht") 
    else:
        lg.info("Insgesamt wurden {} Dateien geloescht".format(cnt))        
    print("Loeschen der Archivdateien beendet. Das Logfile ist im Ordner {}".format(logFile))

