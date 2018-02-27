# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:35:22 2018

@author: S.H.B
"""

from pylab import *
import random as rn
import schach_zugMOEGLICHKEITEN as zm

sF = ["T","S","L","D","K","B"]
wF = ["t","s","l","d","k","b"]
aF = sF + wF


def cpu_main(feld,farbe,schwierigkeit):
    amz_array = alle_moeglichen_zuege(feld,farbe,schwierigkeit)# amz_array in Form: yeigen1,xeigen1,yziel1,xziel1,typeigen1,typziel1,bewertung1...
    print(amz_array)
    #greift auf Bewertungen der züge zu und fasst sie im Array b zusammen(getestet)
    b = []
    for i in range (0,int((len(amz_array))/7)):
        b.append(amz_array[i * 7 + 6])
    
    #erzeugt ein array index_maxb, in dem die Indizes der Elemente gespeichert werden, wenn diese max(b) groß sind
    index_maxb = []
    for j in range(0,len(b)):
        if b[j] == max(b):
            index_maxb.append(b[j])
    
    #ermittelt zufälligerweise einen Index, welcher im array index_maxb benutzt wird
    i = rn.randint(0,len(index_maxb))
    print(i)
    
    #findet nun die y und x-Werte aus dem amz_array herraus, die zum Index in index_maxb passen
    ya = amz_array[i * 7]
    xa = amz_array[i * 7 + 1]
    ye = amz_array[i * 7 + 2]
    xe = amz_array[i * 7 + 3]
    
    #Führt den Zug durch und ändert die Werte der einzelnen Felder
    feld[ye][xe] = feld[ya][xa]
    feld[ya][xa] = "0"

        

        
        
        
        
#wichtige Funktionen:
    
    
def zug_bewertung(ya,xa,ye,xe,feld,schwierigkeit): #yeigen,xeigen,yziel,xziel,typeigen,typziel,bewertung
    if schwierigkeit == "leicht":
        bewertung = 0
        zb = [ya,xa,ye,xe,feld[ya][xa],feld[ye][xe],bewertung]#alle Züge sind mit 1 gleich bewertet
        
    if schwierigkeit == "normal":
        bewertung = 0
#!!!!!!! hier weiter
        zb = [ya,xa,ye,xe,feld[ya][xa],feld[ye][xe],bewertung]
        
    if schwierigkeit == "schwer":
        bewertung = 0
        zb = [ya,xa,ye,xe,feld[ya][xa],feld[ye][xe],bewertung]
        
    return (zb)


def alle_moeglichen_zuege(feld,farbe,schwierigkeit): #amz_array in Form: yeigen1,xeigen1,yziel1,xziel1,typeigen1,typziel1,bewertung1...
    aef, aeft = alle_eigenen_figuren(feld,farbe)
    print(aeft)
    amz_array = []
    
    for i in range(0,int(len(aef) / 2)): #geht jede einzelne eigene Figur durch und erzeugt ein Array mit den möglichen Zügen
        mz = zm.moeglichezuege(aef[i * 2], aef[i * 2 + 1], feld, farbe)
        print(mz)
        for j in range(0,int(len(mz)/2)):#geht jede Zugmöglichkeit einer Figur durch und lässt sie bewerten
            zb = zug_bewertung(aef[i * 2], aef[i * 2 + 1], mz[j * 2], mz[j * 2 + 1], feld, schwierigkeit)
            
            amz_array = amz_array + zb#Informationen werden nun nacheinander an das anz_array angeheftet
    
    return (amz_array)#zur Erinnerung:  7. stelle im Array (beginn bei 0 .. also 6)
            

def alle_eigenen_figuren(feld,farbe):#(getestet)aef_typ_array in Form y1,x1,typ1,y2,x2,typ2,y3,x3.../aef_array in Form y1,x1,y2,x2,....

    aef_array = []
    aef_typ_array = []
    
    
    for y in range(0,8): 
        for x in range(0,8): 
            #wenn alle weißen Figuren gefragt sind:
            if (farbe == "weiß" and feld[y][x] in wF):
                    aef_array.append(y)
                    aef_array.append(x)
                    
                    aef_typ_array.append(y)
                    aef_typ_array.append(x)
                    aef_typ_array.append(feld[y][x])
            
            #wenn alle schwarzen Figuren gefragt sind:
            elif (farbe == "schwarz" and feld[y][x] in sF):
                    aef_array.append(y)
                    aef_array.append(x)
                
                    aef_typ_array.append(y)
                    aef_typ_array.append(x)
                    aef_typ_array.append(feld[y][x])
                    
    return (aef_array, aef_typ_array)
    


def figur_deckung(feld,y,x):#gibt Informationen zur Deckung der abgefragten Figur zurück
    
    status = None
    vielfachheit = None
    art = None
    
    return(status , vielfachheit , art)

def figuren_schlagen(feld,y,x):#gibt mögliche Züge zum Schlagen zurück
    s = [None] #Form: [y1,x1,typ1,y2,x2,typ2....]
    return(s)

def schachmatt_moeglichkeiten(feld,farbe):
    #jede Möglichkeiten der Figuren durchprobieren
    #feld Damit erzeugen 
    #auf schachmattfunktion in Sonstiges zurückgreifen
    status = None
    sm = [None]# Form (yeigen1,xeigen1,yziel1,xziel1)
    return(status, sm)


