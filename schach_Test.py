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

spielfeld = np.array(
    [["T","S","L","D","K","L","S","T"],
     ["B","B","B","B","B","B","B","B"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["b","b","b","b","b","b","b","b"],
     ["t","s","l","d","k","l","s","t"]])

farbe = "weiß"

#cpu.cpu_main(spielfeld,farbe,"leicht")
#print(cpu.alle_moeglichen_zuege(spielfeld,farbe,"leicht"))
print("NÄCHSTE AUSGABE")
g.brettzeichnen(cpu.cpu_main(spielfeld,farbe,"leicht"))