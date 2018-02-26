# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:31:59 2018

@author: S.H.B
"""

def settings(): #(getestet) die Einstellungen des Spiels werden nach Eingabe in einem Dictionary gespeichert
    Name1,Name2 = spielernamen()
    einstellungen = {"Name1" : Name1, "Name2" : Name2}
    #FEHLT: möglichkeit ohne einschränkungen (wie regeln) zu spielen 
    
    return einstellungen


def spielernamen(): #(getestet) gibt die Namen der Spieler in 2 Variabeln (Name1, Name2) zurück, welche zuvor vom Benutzer kreiiert worden sind
    # Spieleranzahlabfrage
    AnzahlderSpieler = 0
    while AnzahlderSpieler != "1" and AnzahlderSpieler != "2":
        AnzahlderSpieler = (input("Anzahl der Spieler? "))
        if AnzahlderSpieler == "1":
            Name1 = input("Ich bin ",)
            Name2 = "CPU"
            print("Hallo",Name1,"und viel Spaß beim Spielen ")
        elif AnzahlderSpieler == "2":
            Name1 = input("Spieler 1 heißt ")
            Name2 = input("Spieler 2 heißt ")
            print("Hallo",Name1,"und",Name2,". Viel Spaß beim Spielen")
        else :
            print("Bitte eine gültige Anzahl an Spielern eintragen(1 oder 2 )")
    return (Name1,Name2) #gibt die Namen der Spieler zurück

def schachmatt():
    return False

def bauerumwandlung(feld):#Wandelt Bauern um, wenn diese das Ende des Spielfelds erreicht haben
    korrekt = False
    efw = ['t','d','s','l'] #erlaubte Figuren zum ziehen für Weiß
    efs = ['T','D','S','L'] #erlaubte Figuren zum ziehen für Schwarz
    for i in range(0,8):
        y = 0
        if feld[y][i] == 'b':
            while korrekt == False:
                c = input("Geben sie eine Figur ihrer Wahl ein (t,d,...) ") # c entspricht dem neuen Wert des Feldes
                if c in efw:
                    korrekt = True
                    feld[y][i] = c
                else:
                    print('Falsche Eingabe. Bitte geben sie erneut eine Figur ein die sie haben möchten')
        
    
    for i in range(0,8):
        y = 7
        if feld[y][i] == 'B':
            while korrekt == False:
                r = input("Geben sie eine Figur ein (T,D,...) ")  
                if r in efs:
                    korrekt = True
                    feld[y][i] = r
                else:
                    print('Falsche Eingabe. Bitte geben sie erneut eine Figur ein die sie haben möchten')
    return feld