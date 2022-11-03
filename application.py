from tkinter import *
from tkinter import ttk
from google_trans_new import google_translator

# définir les variables globales à utiliser
source  = ""
destination = ""
t = ""

def comboAction(event):  
    global source
    global destination
    source = combo1.get()  
    destination = combo2.get()
    
    
def Traduct(event):
    
    trans  = google_translator()
    global t
    t = ""
    t = T1.get("1.0" , END)
    
    translated = trans.translate(t, lang_src = source, lang_tgt = destination)
    T2.delete('1.0', END)
    T2.insert(END , translated)
    


root = Tk()
root.title='DSBD'
root.geometry("800x300")

#-------------------------------
# Création de la liste combobox
#-------------------------------
labelChooseLang = Label(root, text = "Choose language source") 
labelChooseLang.place(x = 20 , y = 50)

labelLangTraduct = Label(root, text = "Destination language") 
labelLangTraduct.place(x = 430 , y = 50)


# Liste des valeurs d'option de la combobox
languages =['fr' , 'en' , 'es' , 'ar']

# Création des listes combobox
combo1 = ttk.Combobox(root, values = languages )
combo1.place(x = 230 , y = 50)
# Définir l'élément qui s'affiche par défaut
combo1.current(0)
# Associé une bind action à la liste combo
combo1.bind("<<ComboboxSelected>>", comboAction)

combo2 = ttk.Combobox(root, values = languages)
combo2.place(x = 590 , y = 50)
# Définir l'élément qui s'affiche par défaut
combo2.current(0)
# Associé une bind action à la liste combo
combo2.bind("<<ComboboxSelected>>", comboAction)


T1 = Text(root )
T1.place(x = 20 , y = 100 , width = 400 , height = 150)
T1.bind("<Return>" , Traduct)

T2 = Text(root)
T2.place(x = 430 , y = 100 , width = 350 , height = 150)

root.mainloop()