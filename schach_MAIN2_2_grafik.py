# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 12:42:41 2018

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
status_ablauf = 1 #regelt den Ablauf des Programms

#Vorgang wird ausgeführt, wenn ein Button gedrückt wird
def button_Funktion(y,x):#(fertig)y,x sind columne, row des Buttons
    #GLOBALE VARIABELN WERDEN BENUTZT
    global ya
    global xa
    global farbe
    global status_ablauf
    global spielfeld
    
    #Erster Schritt jedes Zuges 
    if status_ablauf == 1:
        ya = y
        xa = x
        status_ablauf = 2
    #Zweiter Schritt jedes Zuges
    else:
        #Erstellt ein Zugarray mit den notwendigen Informationen für einen Zug
        zugarray4 = [ya,xa,y,x]
        
        #Erstelt das neue Feld nach dem Zug und erstellt eine Variable, die anzeigt, ob der ausgeführt Zug den Schachregeln entspricht
        spielfeld, zugkorrekt = z.zug_grafik(spielfeld,farbe,zugarray4)
        
        #Nächster Zug fängt wieder mit Schritt 1 an
        status_ablauf = 1
        #Ändert die Farbe für den nächsten Zug
        if farbe == "weiß":
            farbe = "schwarz"
        else:
            farbe = "weiß"
        
        #Ändert die Anzeige der Buttons
        config()
        
        
        #Führt einen möglichen Computerzug durch, wenn die Anzahl der Spieler 1 ist
        if einstellungen["AnzahlderSpieler"] == 1:
            spielfeld = cpu.cpu_main(spielfeld,farbe,einstellungen["schwierigkeit"])#als farbe ist gerade nur schwarz möglich
            #Änderung der Farbe nach dem Zug
            if farbe == "weiß":
                farbe = "schwarz"
            else:
                farbe = "weiß"
    
            #Ändert die Anzeige der Buttons
            config()
    
    
    
    
    
    
    
    
    
    
    
    
    
