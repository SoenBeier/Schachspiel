import os
from pylab import *
from tkinter import *
from tkinter import messagebox
# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("Schach")

feld = np.array(
    [["T","S","L","D","K","L","S","T"],
     ["B","B","B","B","B","B","B","B"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["b","b","b","b","b","b","b","b"],
     ["t","s","l","d","k","l","s","t"]])

def settings(): #(getestet) die Einstellungen des Spiels werden nach Eingabe in einem Dictionary gespeichert
    Name1,Name2 = spielernamen()
    einstellungen = {"Name1" : Name1, "Name2" : Name2}
    #FEHLT: möglichkeit ohne einschränkungen (wie regeln) zu spielen 
    
    return einstellungen

#erfolgreiches Entry
def evaluate(event):
    res.configure(text = "Ergebnis: " + str(eval(entry.get())))
Label(fenster, text="Your Expression:").place(x = 0, y=600)
entry = Entry(fenster)
entry.bind("<Return>", evaluate)
entry.place(x = 100, y = 600)
res = Label(fenster)
res.place(x = 200, y = 600)


'''def spielernamen(): #(getestet) gibt die Namen der Spieler in 2 Variabeln (Name1, Name2) zurück, welche zuvor vom Benutzer kreiiert worden sind
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
    return (Name1,Name2) #gibt die Namen der Spieler zurück"'''


#sounds

def sound1():
    os.system(r'C:\Users\Julian\Music\Parov_Stelar_The_Invisible_Girl.mp3')

audio = Button(fenster,text = 'Hier spielt die Musik',command = sound1, bg='yellow')
audio.place(x = 500, y =0, width = 150, height = 50)

#funktionen

def button_action():
    anweisungs_label.config(text="Ich wurde geändert!")
def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: Sönke Hendrik und Julian Stähle\n\
Date: 03.18\n\
Version: 1.0\n\
Programm: Schach\n\
Info: https://www.overleaf.com/read/khvkmfqjnnjm\n\
Entwicklung: https://github.com/SoenBeier/Schachspiel/tree/master \n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")
    


def config():
    feld = np.array(
    [["G","S","L","D","K","L","S","T"],
     ["B","B","B","B","B","B","B","B"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["b","b","b","b","b","b","b","b"],
     ["t","s","l","d","k","l","s","t"]])
    button1.config(text = feld[0][0])
    button2.config(text = feld[0][1])
    button3.config(text = feld[0][2])
    button4.config(text = feld[0][3])
    button5.config(text = feld[0][4])
    button6.config(text = feld[0][5])
    button7.config(text = feld[0][6])
    button8.config(text = feld[0][7])
    button9.config(text = feld[1][0])
    button10.config(text = feld[1][1])
    button11.config(text = feld[1][2])
    button12.config(text = feld[1][3])
    button13.config(text = feld[1][4])
    button14.config(text = feld[1][5])
    button15.config(text = feld[1][6])
    button16.config(text = feld[1][7])
    button17.config(text = feld[2][0])
    button18.config(text = feld[2][1])
    button19.config(text = feld[2][2])
    button20.config(text = feld[2][3])
    button21.config(text = feld[2][4])
    button22.config(text = feld[2][5])
    button23.config(text = feld[2][6])
    button24.config(text = feld[2][7])
    button25.config(text = feld[3][0])
    button26.config(text = feld[3][1])
    button27.config(text = feld[3][2])
    button28.config(text = feld[3][3])
    button29.config(text = feld[3][4])
    button30.config(text = feld[3][5])
    button31.config(text = feld[3][6])
    button32.config(text = feld[3][7])
    button33.config(text = feld[4][0])
    button34.config(text = feld[4][1])
    button35.config(text = feld[4][2])
    button36.config(text = feld[4][3])
    button37.config(text = feld[4][4])
    button38.config(text = feld[4][5])
    button39.config(text = feld[4][6])
    button40.config(text = feld[4][7])
    button41.config(text = feld[5][0])
    button42.config(text = feld[5][1])
    button43.config(text = feld[5][2])
    button44.config(text = feld[5][3])
    button45.config(text = feld[5][4])
    button46.config(text = feld[5][5])
    button47.config(text = feld[5][6])
    button48.config(text = feld[5][7])
    button49.config(text = feld[6][0])
    button50.config(text = feld[6][1])
    button51.config(text = feld[6][2])
    button52.config(text = feld[6][3])
    button53.config(text = feld[6][4])
    button54.config(text = feld[6][5])
    button55.config(text = feld[6][6])
    button56.config(text = feld[6][7])
    button57.config(text = feld[7][0])
    button58.config(text = feld[7][1])
    button59.config(text = feld[7][2])
    button60.config(text = feld[7][3])
    button61.config(text = feld[7][4])
    button62.config(text = feld[7][5])
    button63.config(text = feld[7][6])
    button64.config(text = feld[7][7])
    





# Label und Buttons erstellen.
change_button = Button(fenster, text="Ändern", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)

#Randbuchstaben und Zahlen:
A = Label(fenster, text = 'A') 
B = Label(fenster, text = 'B')
C = Label(fenster, text = 'C')
D = Label(fenster, text = 'D')
E = Label(fenster, text = 'E')
F = Label(fenster, text = 'F')
G = Label(fenster, text = 'G')
H = Label(fenster, text = 'H')
I = Label(fenster, text = '1')
J = Label(fenster, text = '2')
K = Label(fenster, text = '3')
L = Label(fenster, text = '4')
M = Label(fenster, text = '5')
N = Label(fenster, text = '6')
O = Label(fenster, text = '7')
P = Label(fenster, text = '8')
I.place(x = 400, y=15)
J.place(x = 400, y=65)
K.place(x = 400, y=115)
L.place(x = 400, y=165)
M.place(x = 400, y=215)
N.place(x = 400, y=265)
O.place(x = 400, y=315)
P.place(x = 400, y=365)
A.place(x = 17, y= 400)
B.place(x = 67, y=400)
C.place(x = 117, y=400)
D.place(x = 167, y=400)
E.place(x = 217, y=400)
F.place(x = 267, y=400)
G.place(x = 317, y=400)
H.place(x = 367, y=400)
anweisungs_label = Label(fenster, text="Ich bin eine Anweisung:\n\
Klicke auf 'Ändern'.")

def aufgeben():
    text = 'Sie haben Aufgegeben.'
    messagebox.showinfo(message=text, title = "Aufgeben")
    fenster.after(1, sys.exit)
Aufgeben = Button(fenster, text='Aufgeben', command = aufgeben)


Patt = Button(fenster,text='Patt anbieten',)

info_label = Label(fenster, text="Ich bin eine Info:\n\
Der Beenden Button schliesst das Programm.")
#Zeile 1
button1 = Button(fenster, text=feld[0][0],bg='white',fg='black',command = config)
button2 = Button(fenster, text=feld[0][1],bg='black',fg='white',command = config)
button3 = Button(fenster, text=feld[0][2],bg='white',fg='black',command = config)
button4 = Button(fenster, text=feld[0][3],bg='black',fg='white',command = config)
button5 = Button(fenster, text=feld[0][4],bg='white',fg='black',command = config)
button6 = Button(fenster, text=feld[0][5],bg='black',fg='white',command = config)
button7 = Button(fenster, text=feld[0][6],bg='white',fg='black',command = config)
button8 = Button(fenster, text=feld[0][7],bg='black',fg='white',command = config)
#Zeile 2
button9 = Button(fenster, text=feld[1][0],bg='black',fg='white',command = config)
button10 = Button(fenster, text=feld[1][1],bg='white',fg='black',command = config)
button11 = Button(fenster, text=feld[1][2],bg='black',fg='white',command = config)
button12 = Button(fenster, text=feld[1][3],bg='white',fg='black',command = config)
button13 = Button(fenster, text=feld[1][4],bg='black',fg='white',command = config)
button14 = Button(fenster, text=feld[1][5],bg='white',fg='black',command = config)
button15 = Button(fenster, text=feld[1][6],bg='black',fg='white',command = config)
button16 = Button(fenster, text=feld[1][7],bg='white',fg='black',command = config)
#Zeile 3
button17 = Button(fenster, text=feld[2][0],bg='white',fg='black',command = config)
button18 = Button(fenster, text=feld[2][1],bg='black',fg='white',command = config)
button19 = Button(fenster, text=feld[2][2],bg='white',fg='black',command = config)
button20 = Button(fenster, text=feld[2][3],bg='black',fg='white',command = config)
button21 = Button(fenster, text=feld[2][4],bg='white',fg='black',command = config)
button22 = Button(fenster, text=feld[2][5],bg='black',fg='white',command = config)
button23 = Button(fenster, text=feld[2][6],bg='white',fg='black',command = config)
button24 = Button(fenster, text=feld[2][7],bg='black',fg='white',command = config)
#Zeile 4
button25 = Button(fenster, text=feld[3][0],bg='black',fg='white',command = config)
button26 = Button(fenster, text=feld[3][1],bg='white',fg='black',command = config)
button27 = Button(fenster, text=feld[3][2],bg='black',fg='white',command = config)
button28 = Button(fenster, text=feld[3][3],bg='white',fg='black',command = config)
button29 = Button(fenster, text=feld[3][4],bg='black',fg='white',command = config)
button30 = Button(fenster, text=feld[3][5],bg='white',fg='black',command = config)
button31 = Button(fenster, text=feld[3][6],bg='black',fg='white',command = config)
button32 = Button(fenster, text=feld[3][7],bg='white',fg='black',command = config)
#Zeile 5
button33 = Button(fenster, text=feld[4][0],bg='white',fg='black',command = config)
button34 = Button(fenster, text=feld[4][1],bg='black',fg='white',command = config)
button35 = Button(fenster, text=feld[4][2],bg='white',fg='black',command = config)
button36 = Button(fenster, text=feld[4][3],bg='black',fg='white',command = config)
button37 = Button(fenster, text=feld[4][4],bg='white',fg='black',command = config)
button38 = Button(fenster, text=feld[4][5],bg='black',fg='white',command = config)
button39 = Button(fenster, text=feld[4][6],bg='white',fg='black',command = config)
button40 = Button(fenster, text=feld[4][7],bg='black',fg='white',command = config)
#Zeile 6
button41 = Button(fenster, text=feld[5][0],bg='black',fg='white',command = config)
button42 = Button(fenster, text=feld[5][1],bg='white',fg='black',command = config)
button43 = Button(fenster, text=feld[5][2],bg='black',fg='white',command = config)
button44 = Button(fenster, text=feld[5][3],bg='white',fg='black',command = config)
button45 = Button(fenster, text=feld[5][4],bg='black',fg='white',command = config)
button46 = Button(fenster, text=feld[5][5],bg='white',fg='black',command = config)
button47 = Button(fenster, text=feld[5][6],bg='black',fg='white',command = config)
button48 = Button(fenster, text=feld[5][7],bg='white',fg='black',command = config)
#Zeile 7
button49 = Button(fenster, text=feld[6][0],bg='white',fg='black',command = config)
button50 = Button(fenster, text=feld[6][1],bg='black',fg='white',command = config)
button51 = Button(fenster, text=feld[6][2],bg='white',fg='black',command = config)
button52 = Button(fenster, text=feld[6][3],bg='black',fg='white',command = config)
button53 = Button(fenster, text=feld[6][4],bg='white',fg='black',command = config)
button54 = Button(fenster, text=feld[6][5],bg='black',fg='white',command = config)
button55 = Button(fenster, text=feld[6][6],bg='white',fg='black',command = config)
button56 = Button(fenster, text=feld[6][7],bg='black',fg='white',command = config)
#Zeile 8
button57 = Button(fenster, text=feld[7][0],bg='black',fg='white',command = config)
button58 = Button(fenster, text=feld[7][1],bg='white',fg='black',command = config)
button59 = Button(fenster, text=feld[7][2],bg='black',fg='white',command = config)
button60 = Button(fenster, text=feld[7][3],bg='white',fg='black',command = config)
button61 = Button(fenster, text=feld[7][4],bg='black',fg='white',command = config)
button62 = Button(fenster, text=feld[7][5],bg='white',fg='black',command = config)
button63 = Button(fenster, text=feld[7][6],bg='black',fg='white',command = config)
button64 = Button(fenster, text=feld[7][7],bg='white',fg='black',command = config)


# Menüleiste erstellen 
menuleiste = Menu(fenster)

# Menü Datei und Help erstellen
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
datei_menu.add_command(label="Datei Speichern", command=button_action)
datei_menu.add_separator() # Fügt eine Trennlinie hinzu
datei_menu.add_command(label="Exit", command=fenster.quit)

help_menu.add_command(label="Schachregeln", command=action_get_info_dialog)
help_menu.add_command(label="About...", command=action_get_info_dialog)

# Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
# "Drop-Down-Menü" hinzu
menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

# Die Menüleiste mit den Menüeinrägen noch dem Fenster übergeben und fertig.
fenster.config(menu=menuleiste)    

#Hintergrundbild

#a = PhotoImage(file=r"C:\Users\Julian\Pictures\Camera Roll\Feuermikro.gif")
#imagelabel= Label(fenster, image = a)
#imagelabel.place(x=500, y=500, width =160, height=90)


'''#Namen eingeben
Namen = Button(fenster, text = 'Start', command=spielernamen())
Namen.place(x = 400, y = 600, width = 150, height = 50)
#erfolgreiches Namensentry
namen = Label(fenster, text ='Willkommen '+ Namen.invoke())
namen.place(x = 400, y = 600)'''

# Nun fügen wir die Komponenten unserem Fenster 
# in der gwünschten Reihenfolge hinzu.
anweisungs_label.place()
change_button.place()
info_label.place()
exit_button.place(x = 50, y = 50, width = 50, height = 50)
#Zeile 1
button1.place(x=0, y=0, width=50, height= 50)
button2.place(x=50, y=0, width=50, height= 50)
button3.place(x=100, y=0, width=50, height= 50)
button4.place(x=150, y=0, width=50, height= 50)
button5.place(x=200, y=0, width=50, height= 50)
button6.place(x=250, y=0, width=50, height= 50)
button7.place(x=300, y=0, width=50, height= 50)
button8.place(x=350, y=0, width=50, height= 50)
#Zeile 2
button9.place(x=0, y=50, width=50, height= 50)
button10.place(x=50, y=50, width=50, height= 50)
button11.place(x=100, y=50, width=50, height= 50)
button12.place(x=150, y=50, width=50, height= 50)
button13.place(x=200, y=50, width=50, height= 50)
button14.place(x=250, y=50, width=50, height= 50)
button15.place(x=300, y=50, width=50, height= 50)
button16.place(x=350, y=50, width=50, height= 50)
#Zeile 3
button17.place(x=0, y=100, width=50, height= 50)
button18.place(x=50, y=100, width=50, height= 50)
button19.place(x=100, y=100, width=50, height= 50)
button20.place(x=150, y=100, width=50, height= 50)
button21.place(x=200, y=100, width=50, height= 50)
button22.place(x=250, y=100, width=50, height= 50)
button23.place(x=300, y=100, width=50, height= 50)
button24.place(x=350, y=100, width=50, height= 50)
#Zeile 4
button25.place(x=0, y=150, width=50, height= 50)
button26.place(x=50, y=150, width=50, height= 50)
button27.place(x=100, y=150, width=50, height= 50)
button28.place(x=150, y=150, width=50, height= 50)
button29.place(x=200, y=150, width=50, height= 50)
button30.place(x=250, y=150, width=50, height= 50)
button31.place(x=300, y=150, width=50, height= 50)
button32.place(x=350, y=150, width=50, height= 50)
#Zeile 5
button33.place(x=0, y=200, width=50, height= 50)
button34.place(x=50, y=200, width=50, height= 50)
button35.place(x=100, y=200, width=50, height= 50)
button36.place(x=150, y=200, width=50, height= 50)
button37.place(x=200, y=200, width=50, height= 50)
button38.place(x=250, y=200, width=50, height= 50)
button39.place(x=300, y=200, width=50, height= 50)
button40.place(x=350, y=200, width=50, height= 50)
#Zeile 6
button41.place(x=0, y=250, width=50, height= 50)
button42.place(x=50, y=250, width=50, height= 50)
button43.place(x=100, y=250, width=50, height= 50)
button44.place(x=150, y=250, width=50, height= 50)
button45.place(x=200, y=250, width=50, height= 50)
button46.place(x=250, y=250, width=50, height= 50)
button47.place(x=300, y=250, width=50, height= 50)
button48.place(x=350, y=250, width=50, height= 50)
#Zeile 7
button49.place(x=0, y=300, width=50, height= 50)
button50.place(x=50, y=300, width=50, height= 50)
button51.place(x=100, y=300, width=50, height= 50)
button52.place(x=150, y=300, width=50, height= 50)
button53.place(x=200, y=300, width=50, height= 50)
button54.place(x=250, y=300, width=50, height= 50)
button55.place(x=300, y=300, width=50, height= 50)
button56.place(x=350, y=300, width=50, height= 50)
#Zeile 8
button57.place(x=0, y=350, width=50, height= 50)
button58.place(x=50, y=350, width=50, height= 50)
button59.place(x=100, y=350, width=50, height= 50)
button60.place(x=150, y=350, width=50, height= 50)
button61.place(x=200, y=350, width=50, height= 50)
button62.place(x=250, y=350, width=50, height= 50)
button63.place(x=300, y=350, width=50, height= 50)
button64.place(x=350, y=350, width=50, height= 50)



#andere buttons
Patt.place(x=500,y=150,width = 150, height = 50)
Aufgeben.place(x=500,y=250,width = 150, height = 50)
# In der Ereignisschleife auf Eingabe des Benutzers warten.

fenster.mainloop()