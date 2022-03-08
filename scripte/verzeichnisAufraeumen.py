import os
import shutil
from datetime import date, datetime, timedelta
from .loghandler import logger as lg
from.loghandler import logFile

'''
Erstellt am 01.12.2021
Räumt das Verzeichnis 'BO_Berichte' auf dem Servicelaufwerk auf. Dabei ist wichtig , das die Zeitgesteuerten Bericht die folgenden Strings im Namen haben
# Tag, Monat, Quartal, Jahr => je nach ausführungsintervall
Anschliessend werden die Files nach ablauf dieser Zeit erst mal in den Archivordner verschoben.
Nach einer gewissen Zeit werden die Dateien dann aus den Archivordnern gelöscht
'''


def clearDict(startverzeichnis, Tgl, Mtl, Jrl):
    print("Starte Verarbeitung")
    aktuellesDatum = date.today()
    lg.info("------- {} ---- Aufraeumen des Verzeichnis gestartet ----".format(aktuellesDatum))
    workdir = startverzeichnis
    lg.info("Einlesevorgang begonnen Arbeitsverzeichnis ist :{}".format(workdir))
    maxTimeTgl = datetime.now() - timedelta(days=Tgl)
    maxTimeMtl = datetime.now() - timedelta(days=Mtl)
    maxTimeJrl = datetime.now() - timedelta(days=Jrl)
    unterVerzeichnisse = os.listdir(workdir)
    cnt=0
    #lg.info("Die folgenden Verzeichnisse werden gelesen :")
    for verzeichnis in unterVerzeichnisse:
        #lg.info("Verzeichnis : {}".format(verzeichnis))
        dateien = os.listdir(workdir + verzeichnis + "/")
        #Hier beginnt die Prüfung auf das Archiv Verzeichnis
        if not os.path.exists(workdir + verzeichnis + "/arc/"):
            os.makedirs(workdir + verzeichnis + "/arc/")
        # Ende Prüfung Archivverzeichnis
        for datei in dateien: 
            if datei != "arc":                                       # der Archivordner soll erst mal noch nicht beachtet werden
                datName = workdir + verzeichnis + "/" + datei        #dateiname jede reinzelnen Datei incl. Verzeichnispfad
                arcDatName = workdir + verzeichnis + "/arc/" + datei #dateiname im Archivordner incl. Verzeichnispfad
                dateiZeit = datetime.fromtimestamp(os.path.getmtime(datName)) 
                if datei.find("Tag") > 0: # prüft ob der jeweilige Dateiname Tag|Monat|Quartal|Jahr enthält und verschiebt dann entsprechend der festlegung
                    #lg.info('Datei {} gefunden'.format(datei))
                    if dateiZeit < maxTimeTgl:
                        shutil.move(datName, arcDatName + datei)
                        cnt+=1
                        #lg.info("{} wurde verschoben nach {}".format(datei, arcDatName))
                elif datei.find("Monat") > 1 or datei.find("Quartal") > 1:
                    #lg.info('Datei {} gefunden'.format(datei))
                    if dateiZeit < maxTimeMtl:
                        shutil.move(datName, arcDatName + datei)
                        cnt+=1
                        #lg.info("{} wurde verschoben nach {}".format(datei, arcDatName))
                elif datei.find("Jahr") > 1:
                    #lg.info('Datei {} gefunden'.format(datei))
                    if dateiZeit < maxTimeJrl:
                        shutil.move(datName, arcDatName + datei)
                        cnt+=1
                        #lg.info("{} wurde verschoben nach {}".format(datei, arcDatName))
    if cnt==0:
        lg.info("Keine Datei zum Verschieben gefunden") 
    else:
        lg.info("Insgesamt wurden {} Dateien verschoben".format(cnt))
    print("Verarbeitung beendet. Das Logfile ist im Ordner {}".format(logFile))
