from pylab import *
from tkinter import *
from tkinter import messagebox
# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("Nur ein Fenster")

feld = np.array(
    [["T","S","L","D","K","L","S","T"],
     ["B","B","B","B","B","B","B","B"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["0","0","0","0","0","0","0","0"],
     ["b","b","b","b","b","b","b","b"],
     ["t","s","l","d","k","l","s","t"]])

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
************************"
	messagebox.showinfo(message=m_text, title = "Infos")
    


# Label und Buttons erstellen.
change_button = Button(fenster, text="Ändern", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)

anweisungs_label = Label(fenster, text="Ich bin eine Anweisung:\n\
Klicke auf 'Ändern'.")

Aufgeben = Button(fenster, text='Aufgeben')
Patt = Button(fenster,text='Patt anbieten')

info_label = Label(fenster, text="Ich bin eine Info:\n\
Der Beenden Button schliesst das Programm.")
#Zeile 1
button1 = Button(fenster, text=feld[0][0],bg='white',fg='black')
button2 = Button(fenster, text=feld[0][1],bg='black',fg='white')
button3 = Button(fenster, text=feld[0][2],bg='white',fg='black')
button4 = Button(fenster, text=feld[0][3],bg='black',fg='white')
button5 = Button(fenster, text=feld[0][4],bg='white',fg='black')
button6 = Button(fenster, text=feld[0][5],bg='black',fg='white')
button7 = Button(fenster, text=feld[0][6],bg='white',fg='black')
button8 = Button(fenster, text=feld[0][7],bg='black',fg='white')
#Zeile 2
button9 = Button(fenster, text=feld[1][0],bg='black',fg='white')
button10 = Button(fenster, text=feld[1][1],bg='white',fg='black')
button11 = Button(fenster, text=feld[1][2],bg='black',fg='white')
button12 = Button(fenster, text=feld[1][3],bg='white',fg='black')
button13 = Button(fenster, text=feld[1][4],bg='black',fg='white')
button14 = Button(fenster, text=feld[1][5],bg='white',fg='black')
button15 = Button(fenster, text=feld[1][6],bg='black',fg='white')
button16 = Button(fenster, text=feld[1][7],bg='white',fg='black')
#Zeile 3
button17 = Button(fenster, text=feld[2][0],bg='white',fg='black')
button18 = Button(fenster, text=feld[2][1],bg='black',fg='white')
button19 = Button(fenster, text=feld[2][2],bg='white',fg='black')
button20 = Button(fenster, text=feld[2][3],bg='black',fg='white')
button21 = Button(fenster, text=feld[2][4],bg='white',fg='black')
button22 = Button(fenster, text=feld[2][5],bg='black',fg='white')
button23 = Button(fenster, text=feld[2][6],bg='white',fg='black')
button24 = Button(fenster, text=feld[2][7],bg='black',fg='white')
#Zeile 4
button25 = Button(fenster, text=feld[3][0],bg='black',fg='white')
button26 = Button(fenster, text=feld[3][1],bg='white',fg='black')
button27 = Button(fenster, text=feld[3][2],bg='black',fg='white')
button28 = Button(fenster, text=feld[3][3],bg='white',fg='black')
button29 = Button(fenster, text=feld[3][4],bg='black',fg='white')
button30 = Button(fenster, text=feld[3][5],bg='white',fg='black')
button31 = Button(fenster, text=feld[3][6],bg='black',fg='white')
button32 = Button(fenster, text=feld[3][7],bg='white',fg='black')
#Zeile 5
button33 = Button(fenster, text=feld[4][0],bg='white',fg='black')
button34 = Button(fenster, text=feld[4][1],bg='black',fg='white')
button35 = Button(fenster, text=feld[4][2],bg='white',fg='black')
button36 = Button(fenster, text=feld[4][3],bg='black',fg='white')
button37 = Button(fenster, text=feld[4][4],bg='white',fg='black')
button38 = Button(fenster, text=feld[4][5],bg='black',fg='white')
button39 = Button(fenster, text=feld[4][6],bg='white',fg='black')
button40 = Button(fenster, text=feld[4][7],bg='black',fg='white')
#Zeile 6
button41 = Button(fenster, text=feld[5][0],bg='black',fg='white')
button42 = Button(fenster, text=feld[5][1],bg='white',fg='black')
button43 = Button(fenster, text=feld[5][2],bg='black',fg='white')
button44 = Button(fenster, text=feld[5][3],bg='white',fg='black')
button45 = Button(fenster, text=feld[5][4],bg='black',fg='white')
button46 = Button(fenster, text=feld[5][5],bg='white',fg='black')
button47 = Button(fenster, text=feld[5][6],bg='black',fg='white')
button48 = Button(fenster, text=feld[5][7],bg='white',fg='black')
#Zeile 7
button49 = Button(fenster, text=feld[6][0],bg='white',fg='black')
button50 = Button(fenster, text=feld[6][1],bg='black',fg='white')
button51 = Button(fenster, text=feld[6][2],bg='white',fg='black')
button52 = Button(fenster, text=feld[6][3],bg='black',fg='white')
button53 = Button(fenster, text=feld[6][4],bg='white',fg='black')
button54 = Button(fenster, text=feld[6][5],bg='black',fg='white')
button55 = Button(fenster, text=feld[6][6],bg='white',fg='black')
button56 = Button(fenster, text=feld[6][7],bg='black',fg='white')
#Zeile 8
button57 = Button(fenster, text=feld[7][0],bg='black',fg='white')
button58 = Button(fenster, text=feld[7][1],bg='white',fg='black')
button59 = Button(fenster, text=feld[7][2],bg='black',fg='white')
button60 = Button(fenster, text=feld[7][3],bg='white',fg='black')
button61 = Button(fenster, text=feld[7][4],bg='black',fg='white')
button62 = Button(fenster, text=feld[7][5],bg='white',fg='black')
button63 = Button(fenster, text=feld[7][6],bg='black',fg='white')
button64 = Button(fenster, text=feld[7][7],bg='white',fg='black')

# Menüleiste erstellen 
menuleiste = Menu(fenster)

# Menü Datei und Help erstellen
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
datei_menu.add_command(label="Anwenden", command=button_action)
datei_menu.add_separator() # Fügt eine Trennlinie hinzu
datei_menu.add_command(label="Exit", command=fenster.quit)

help_menu.add_command(label="Info!", command=action_get_info_dialog)

# Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
# "Drop-Down-Menü" hinzu
menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

# Die Menüleiste mit den Menüeinrägen noch dem Fenster übergeben und fertig.
fenster.config(menu=menuleiste)    



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