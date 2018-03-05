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
    [["T","S","L","D","K","L","S","T"],
     ["B","B","B","B","B","B","B","B"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["b","b","b","b","b","b","b","b"],
     ["t","s","l","d","k","l","s","t"]])

farbe = "schwarz"
i = 0
ya = 1
xa = 0
ye = 7
xe = 0


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
        
        #Lädt sich Informationen über die Art der Deckung der gegnerischen Figuren in die 3 folgenden Variabeln
        status_deckung, vielfachheit_deckung, art_deckung = figur_gedeckt(ye,xe,feld)
       
    
    #Bewertung aufgrund von Deckung gegenüber einer anderen verbündeten Figur(wichtig: Wertung einge Figur und eigene verbündete Figur)
     
    
    #Erhöhung der Bewertung, falls ein Bauer 2 Züge machen kann
    
    
    #Verringerung der Bewertung, wenn die Figur aus einer Deckung rausgeht(wichtig: Wertung eigener Figur)
    
    
    #Verringerung der Bewertung, wenn die Figur aus eine Position, in der sie jemanden Schlagen könnte verlässt(wichtig: Wertung der gegnerFigur)
    
    
    
    return bewertung

def figur_gedeckt(y,x,feld):#gibt Informationen zur Deckung der abgefragten Figur zurück
    status = False
    vielfachheit = 0
    art = []
    
    sF = ["T","S","L","D","K","B"]
    wF = ["t","s","l","d","k","b"]
    if feld[y][x] in sF:
        farbe = "schwarz"
    else:
        farbe = "weiß"
    
    arbeits_feld = copy.deepcopy(feld)
    arbeits_feld[y][x] = "0"
    eigene_Figuren, eigene_Figuren_typ = cpu.alle_eigenen_figuren(arbeits_feld,farbe)    
    
    
    
    for i in range(0,int(len(eigene_Figuren) / 2)): #geht jede eigene Figur durch
        mz = (s.moeglichezuege(eigene_Figuren[i * 2],eigene_Figuren[i * 2 + 1],arbeits_feld,farbe))
        for j in range(0,int(len(mz) / 2)):
            if y == mz[j]:
                if x == mz[j + 1]:
                    #erhöht die Anzahl der Deckungen der Figur
                    vielfachheit = vielfachheit + 1
                    #Hängt die Art der Figur an das Array "art" an, wenn diese feld[y][x]schlagen kann
                    art.append(arbeits_feld[eigene_Figuren[i * 2]][eigene_Figuren[i * 2 + 1]])


    if vielfachheit > 0:
        status = True
    
    return(status , vielfachheit , art)#status-gedeckt(ja/nein), vielfachheit-durch wie viele gedeckt, art - durch wen gedeckt


print(zug_bewertung_entscheider(ya,xa,ye,xe,spielfeld))
#print(figur_gedeckt(0,0,spielfeld))




