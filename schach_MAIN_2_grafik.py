# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:04:34 2018

@author: S.H.B
"""

from pylab import *
import schach_ZUG as z
import schach_GRAFIK as grafik
import schach_SETTINGS_SONSTIGES as seso
import schach_CPU as cpu
from tkinter import *

#Erstellung des 8*8 Arrays des Spielfeldes zu Beginn:
spielfeld = np.array(
    [["T","S","L","D","K","L","S","T"],
     ["B","B","B","B","B","B","B","B"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["b","b","b","b","b","b","b","b"],
     ["t","s","l","d","k","l","s","t"]])

#Erstellt ein Dictionary ("Einstellungen" mit den vorgefassten Optionen)
einstellungen = seso.settings() 

#vorgegebene Variabeln die für den Ablauf des Programms benötigt werden
ya = None 
xa = None 
farbe = "weiß" #zeigt die Farbe an,die in diesen Moment an der Reihe ist
a_status_ablauf = 1 #regelt den Ablauf des Programms

#Vorgang wird ausgeführt, wenn ein Button gedrückt wird
def button_Funktion(y,x):#(fertig)y,x sind columne, row des Buttons
    #GLOBALE VARIABELN WERDEN BENUTZT
    global ya
    global xa
    global farbe
    global a_status_ablauf
    global spielfeld
    
    if a_status_ablauf == 1:
        ya = y
        xa = x
        a_status_ablauf = 2
    else:
        zugarray4 = [ya,xa,y,x]
        spielfeld = z.zug_grafik(zugarray4,farbe) #zug_grafik ist die zug - Funktion ohne Eingabe per Konsole und ohne überprüfung der Syntax
        a_status_ablauf = 1
        if farbe == "weiß":
            farbe = "schwarz"
        else:
            farbe = "weiß"
    
#Regelt Hauptablauf des Programms
def main_Funktion():
    #GLOBALE VARIABELN WERDEN BENUTZT
    global ya
    global xa
    global farbe
    global a_status_ablauf
    global spielfeld
    global einstellungen
    
    #!!! Anzeige für den Spieler wer am Zug ist -> muss noch in einen Butten gepackt werden 
    if einstellungen["AnzahlderSpieler"] == 1 or einstellungen["AnzahlderSpieler"] == 2:#nötig um vllt später pc-Spieler gegeneinadner spielen zu lassen
        if farbe == "weiß":
            print ("Weiß ist am Zug")
        else:
            print("Schwarz ist am Zug")
    #!!!EINZELNE BUTTONS
    
    #!!!Buttonanzeige verändern
    
    #Computerzug, falls einer gewünscht ist     
    if einstellungen["AnzahlderSpieler"] == 1:
        spielfeld = cpu.cpu_main(spielfeld,farbe,einstellungen["schwierigkeit"])#als farbe ist gerade nur schwarz möglich
        #Änderung der Farbe nach dem Zug
        if farbe == "weiß":
            farbe = "schwarz"
        else:
            farbe = "weiß"
    #!!!Buttonanzeige verändern
    
    fenster.mainloop
mainFunktion()




