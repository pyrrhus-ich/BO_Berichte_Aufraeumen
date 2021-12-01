import os
import shutil
from datetime import datetime, timedelta

'''
Erstellt am 01.12.2021
Räumt das Verzeichnis 'BO_Berichte' auf dem Servicelaufwerk auf. Dabei ist wichtig , das die Zeitgesteuerten Bericht die folgenden Strings im Namen haben
# Tag, Monat, Quartal, Jahr => je nach ausführungsintervall
Anschliessend werden die Files nach ablauf dieser Zeit erst mal in den Archivordner verschoben.
Nach einer gewissen Übergangszeit würde ich das shutil.move ersetzen durch ein delete
'''
workdir = "x:/BO_Berichte/"
maxTimeTgl = datetime.now() - timedelta(days=120)
maxTimeMtl = datetime.now() - timedelta(days=390)
maxTimeJrl = datetime.now() - timedelta(days=1100)
unterVerzeichnisse = os.listdir(workdir)

for verzeichnis in unterVerzeichnisse:
    print("Verzeichnis : {}".format(verzeichnis))
    dateien = os.listdir(workdir + verzeichnis + "/")
    for datei in dateien:
        if datei != "arc":
            datPfad = workdir + verzeichnis + "/" + datei
            archiv = workdir + verzeichnis + "/arc/" + datei
            dateiZeit = datetime.fromtimestamp(os.path.getmtime(datPfad))
            if datei.find("Tag") > 0:
                print("Tag gefunden")
                print(datei)
                if dateiZeit < maxTimeTgl:
                    shutil.move(datPfad, archiv + datei)
            elif datei.find("Monat") > 1 or datei.find("Quartal") > 1:
                print("Monat oder Quartal gefunden")
                if dateiZeit < maxTimeMtl:
                    shutil.move(datPfad, archiv + datei)
            elif datei.find("Jahr") > 1:
                print("Jahr gefunden")
                if dateiZeit < maxTimeJrl:
                    shutil.move(datPfad, archiv + datei)
            else:
                shutil.move(datPfad, archiv)
print("Fertig")
