# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:46:56 2018

@author: S.H.B
"""



from pylab import*
import schach_CPU as cpu
import random as rn
import schach_zugMOEGLICHKEITEN as s
import schach_GRAFIK as g
from tkinter import *
import copy


spielfeld = np.array(
    [["T","S","L","D","K","L","S","T"],#0
     ["B","B","B","0","B","B","B","0"],#1
     ["0","0","0","0","0","0","0","0"],#2
     ["0","0","0","0","0","0","0","0"],#3
     ["0","0","0","0","0","0","0","0"],#4
     ["0","0","0","0","0","0","0","0"],#5
     ["b","b","b","b","b","b","b","b"],#6
     ["t","s","l","d","k","l","s","t"]])#7
#      0   1   2   3   4   5   6   7
farbe = "schwarz"
i = 0
ya = 1
xa = 0
ye = 5
xe = 2


def zug_bewertung_entscheider(ya,xa,ye,xe,feld):#gibt die Bewertung für einen Zug im normalen Spielmodus zurück
    bewertung = 0
    figur_typ = feld[ya][xa] #Typ der eigenen Figur 
    sF = ["T","S","L","D","K","B"]
    wF = ["t","s","l","d","k","b"]
    #Dictionary mit den Bewertungen der Figuren 
    wertung_figur = {"b" : 1 ,"B" : 1 ,"k" : 2 ,"K" : 2 ,"s" : 3 ,"S" : 3 ,"l" : 3 ,"L" : 3 ,"t" : 5 ,"T" : 5 ,"d" : 8 , "D" : 8}

    
    
    #gegner Figuren werden festgelegt/ eigene Farbe wird festgestellt
    if feld[ya][xa] in sF:
        gF = wF #gF = gegnerFiguren
        vF = sF #vF = verbündeteFiguren
        eigene_farbe = "schwarz"
        gegner_farbe = "weiß"
    elif feld[ya][xa] in wF:
        gF = sF
        vF = wF
        eigne_farbe = "weiß"
        gegner_farbe = "schwarz"
    #Fehlermeldung, falls die Figur nicht erkannt wird
    else:
        print(feld[ya][xa])
        raise NameError("Error - Schwerwiegender Fehler in zug_bewertung_entscheider - Figur nicht erkannt")
    
    
    #Bewertung aufgrund eines Gegners, der geschlagen werden kann (wichtig gegner Figur und Deckung der anderen Figur -> Vergleich mit eigener Wertung )
    if feld[ye][xe] in gF:
        bewertung = bewertung + 1 #bewertet den Zug automatisch höher
        bewertung = bewertung + wertung_figur[feld[ye][xe]] #bewertet den Zug relativ zur geschlagenen Person höher
        
        
        
    #Verringerung der Bewertung des Zuges, wenn die Figur auf ein Feld zieht, welches vom Gegner im Visier ist    
    #Lädt sich Informationen über die Art der Deckung der gegnerischen Figuren in die 3 folgenden Variabeln
    gegner_status_deckung, gegner_vielfachheit_deckung, gegner_art_deckung = feld_gedeckt(ye,xe,feld,gegner_farbe)
        #Abziehen von Bewertungs-Punkten für den Zug, wenn das Ziel gut gedeckt ist
    if gegner_status_deckung == True:
        bewertung = bewertung - 1
            
        
    #Erhöhung der Bewertung des Zuges, wenn die Figur auf ein Feld zieht, welche von Verbündeten im Visier ist
    eigene_status_deckung, eigene_vielfachheit_deckung, eigene_art_deckung = feld_gedeckt(ye,xe,feld,eigene_farbe)
    print(feld_gedeckt(ye,xe,feld,eigene_farbe))
    if eigene_status_deckung == True:
        bewertung = bewertung - 1
        
    #erstellt Variabel für die Abbruchbedingung der while Schleife
    evd_schleife = copy.deepcopy(eigene_vielfachheit_deckung)
    #vergleicht die Deckungen des Zielfelds -> Zieht von der Wertung Punkte ab - wenn die Abdeckung des Gegners besser ist
    print(gegner_vielfachheit_deckung, evd_schleife)
    while gegner_vielfachheit_deckung > evd_schleife:
        bewertung = bewertung - 1
        evd_schleife = evd_schleife + 1
        #!!! weiter mit Bezug auf den Wert der Figuren, die an der Deckung beteiligt sind
        
            
    
    
    
    #Bewertung aufgrund von Deckung gegenüber einer anderen verbündeten Figur(wichtig: Wertung einge Figur und eigene verbündete Figur)
     
    
    #Erhöhung der Bewertung, falls ein Bauer 2 Züge machen kann
    
    
    #Verringerung der Bewertung, wenn die Figur aus einer Deckung rausgeht(wichtig: Wertung eigener Figur)
    
    
    #Verringerung der Bewertung, wenn die Figur aus eine Position, in der sie jemanden Schlagen könnte verlässt(wichtig: Wertung der gegnerFigur)
    
    
    
    return bewertung

def feld_gedeckt(y,x,feld,farbe):#gibt Informationen zur Deckung der abgefragten Figur zurück /farbe = verbündete Farbe
    
    #Initialisierung der benötigten Variabeln   
    #Variabeln, die später zurückgegeben werden
    status = False
    vielfachheit = 0
    art = []
    
    #schwarze und weiße Figuren
    sF = ["T","S","L","D","K","B"]
    wF = ["t","s","l","d","k","b"]
    
    #benötigte Arrays
    arbeits_feld = copy.deepcopy(feld) #aufgrund von Problemen mit globalen Variabeln
    arbeits_feld[y][x] = "0" #Figur auf der gefragten Position wird gelöscht, damit später mit der moeglichezuege() Methode gearbeitet werden kann
    eigene_Figuren, eigene_Figuren_typ = cpu.alle_eigenen_figuren(arbeits_feld, farbe)
    
    
    for i in range(0,int(len(eigene_Figuren) / 2)):
        #Erstellt in jedem Iterationsschritt ein Array mit den möglichen Zügen einer Figur..dabei verläuft die for-Schleife über jede Figur
        
        mz = (s.moeglichezuege(eigene_Figuren[i * 2],eigene_Figuren[i * 2 + 1],arbeits_feld,farbe))
        
        #Vergleicht die Koordinaten im Array mit den möglichen Zügen mit der y und x Koordinate, für welches Feld die Deckung überprüft werden soll
        for j in range(0,int(len(mz) / 2)):
            if y == mz[j * 2]:
                if x == mz[j * 2 + 1]:
                    #wenn y und x Koordinate übereinstimmen:
                    #erhöht die Anzahl der Deckungen der Figur
                    vielfachheit = vielfachheit + 1
                    #Hängt den Typen der Figur an das Array "art" an, wenn diese Figur das Feld[y][x] schlagen kann
                    art.append(arbeits_feld[eigene_Figuren[i * 2]][eigene_Figuren[i * 2 + 1]])
    
    
    if vielfachheit > 0:
        #wenn es eine Person gibt, die das Feld[y][x] deckt:
        status = True
    
    return(status, vielfachheit, art)
    


    
for y in range(0,8):
    for x in range(0,8):
        print(feld_gedeckt(y,x,spielfeld,"weiß"))









