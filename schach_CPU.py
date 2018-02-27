# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:35:22 2018

@author: S.H.B
"""

from pylab import *
import random as rn
import schach_zugMOEGLICHKEITEN as zm


def cpu_main(feld,farbe,schwierigkeit):
    if schwierigkeit == "leicht":
        None
        #erzeugt array mit positionen von allen figuren
        #geht jede Figur durch und erzeugt ein array mit allen möglichen zügen aller figuren
        #wenn er eine figur schlagen kann macht er dies zuerst (am besten mit niedrigster figur )
            #näheres Vorgehen: sucht jede einzelne figur von vorne nach hinten ab und schaut ob dieses Feld von ihr eingenommen werden kann
    elif schwierigkeit == "normal":
        None
        #Dinge die berücksichtigt werden müssen
        #Schlagmöglichkeiten mit Punkten
        #Deckungsmöglichkeiten mit punkten
        #ist gegner gedeckt mit Punkten 
        #
    elif schwierigkeit == "schwer":
        None
        
#wichtige Funktionen:
def alle_moeglichen_zuege(feld,farbe):#amz_array in Form: yeigen1,xeigen1,yziel1,xziel1,typeigen1,typziel1,bewertung1...
    
    return (amz_array)
    
def alle_eigenen_figuren(feld,farbe):#aef_array in Form y1,x1,typ1,y2,x2,typ2,y3,x3...
    for y in range(0,8): 
        for x in range(0,8): 
            
    return (aef_array)
    











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


