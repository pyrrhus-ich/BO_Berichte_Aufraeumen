Sinn dieses Scriptes ist es den Ordner in dem die BO Berichte abgelegt sind regelmäßig aufzuräumen

Vorbedingungen:
-----------------
- Python 3.xxx ist auf dem Ausführendem Rechner installiert
- path ist gesetzt
- Aufzuräumendes LW ist verknüpft und in 'run.py' als 'startLw' gesetzt
- In 'run.py' sind die Werte für das verschieben und löschen gesetzt. Diese Werte können geändert werden
    ACHTUNG alle Werte sind Tage 
    Werte ab denen die Dateien VERSCHOBEN werden - relevant fuer clearDict()
    cdTag=10 - nach 10 Tagen
    cdMonat=120 - nach 120 Tagen 
    cdJahr=1100 - nach 1200 Tagen
 
    Werte ab denen die Dateien GELOESCHT werden - relevant fuer clearArchiv()
    caTag=120
    caMonat=360
    caJahr=3300

Ablauf:
-------
- Doppelclick auf run.py
- Es öffnet sich die Console
- Schauen was dort steht und dies dann auch machen
- Fenster schliesst sich nicht von alleine, muss manuell geschlossen werden
- Wenn alles fertig ist, kann man sich im Logfile anpassen was passiert ist