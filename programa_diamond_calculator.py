from tkinter import *
import logging

logging.basicConfig(
    level=logging.DEBUG, 
    filename="error_failas.log", 
    encoding="UTF-8", 
    format="%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s"
) 

langas = Tk()
langas.title("Diamond calculator")
langas.geometry("425x540")
langas.iconphoto(False, PhotoImage(file='diamond-13459.png'))

kiekis = IntVar()

def apskaiciuoti_briliantu_kieki():
    try:
        ivestas_ziedo_dydis = float(e_ziedo_dydis.get())
        ivestas_ziedo_aukstis = float(e_ziedo_aukstis.get())
        ivestas_brilianto_dydis = float(e_brilianto_dydis.get())
        if ivestas_brilianto_dydis <= 1.65:
            tarpelis = 0.1
        elif 1.65 < ivestas_brilianto_dydis <= 2.5:
            tarpelis = 0.15
        elif 2.5 < ivestas_brilianto_dydis <= 3.0:
            tarpelis = 0.2
        elif 3.0 < ivestas_brilianto_dydis:
            tarpelis = 0.25    
        try:
            kiekis_vnt = int((ivestas_ziedo_dydis + 2*ivestas_ziedo_aukstis)* 3.14)/(ivestas_brilianto_dydis + tarpelis)//rb_variable.get()
            l_rezultatas_kiekis_vnt["text"] = f"Reikės {kiekis_vnt} vnt. briliantų"
            kiekis.set(kiekis_vnt)
        except Exception as e_error:
            l_error["text"] = "Būtina pasirinkti"
            logging.exception(f'Vykdant funkcija {apskaiciuoti_briliantu_kieki.__name__}, ivyko klaida {e_error.__class__.__name__}: {e_error}')
    except ValueError as v_error:
        l_tarpas["text"] = "Įveskite skaičius"
        logging.exception(f'Vykdant funkcija {apskaiciuoti_briliantu_kieki.__name__}, ivyko klaida {v_error.__class__.__name__}: {v_error}')

def skaiciuoti_briliantu_kaina():
    try:
        ivestas_brilianto_dydis_ct = float(e_brilianto_dydis_ct.get())
        ivesta_briliantu_kaina = float(e_briliantu_kaina.get())
        kaina = ivestas_brilianto_dydis_ct*ivesta_briliantu_kaina*kiekis.get()
        l_rezultatas_kaina_eur["text"] = f"{kaina} Eur"
        l_tarpas2["text"] = ""
    except ValueError as v_error:
        l_tarpas2["text"] = "Įveskite skaičius"
        logging.exception(f'Vykdant funkcija {skaiciuoti_briliantu_kaina.__name__}, ivyko klaida {v_error.__class__.__name__}: {v_error}')

def skaiciuoti_inkrustavimo_kaina():
    try:
        ivesta_inkrustavimo_kaina = float(e_inkrustavimo_kaina.get())
        kaina = ivesta_inkrustavimo_kaina*kiekis.get()
        l_rezultatas_inkrustavimo_kaina_eur["text"] = f"{kaina} Eur"
        l_tarpas4["text"] = ""
    except ValueError as v_error:
        l_tarpas4["text"] = "Įveskite skaičių"
        logging.exception(f'Vykdant funkcija {skaiciuoti_inkrustavimo_kaina.__name__}, ivyko klaida {v_error.__class__.__name__}: {v_error}')

def kablelis():
    l_tarpas["text"] = "Naudokite tašką, o ne kablelį"

def taskas():
    l_tarpas["text"] = ""

def isvalyti_error():
    l_error["text"] = ""

def isvalyti():
    l_rezultatas_kiekis_vnt["text"] = ""
    e_ziedo_dydis.delete(0, len(e_ziedo_dydis.get()))
    e_ziedo_aukstis.delete(0, len(e_ziedo_aukstis.get()))
    e_brilianto_dydis.delete(0, len(e_brilianto_dydis.get()))
    e_brilianto_dydis_ct.delete(0, len(e_brilianto_dydis_ct.get()))
    e_briliantu_kaina.delete(0, len(e_briliantu_kaina.get()))
    l_rezultatas_kaina_eur["text"] = ""
    e_inkrustavimo_kaina.delete(0, len(e_inkrustavimo_kaina.get()))
    l_rezultatas_inkrustavimo_kaina_eur["text"] = ""
    rb_aplink.deselect()
    rb_puse.deselect()
    rb_trecdalis.deselect()
    rb_ketvirtadalis.deselect()
    l_error["text"] = ""
    l_tarpas["text"] = ""
    l_tarpas2["text"] = ""
    l_tarpas4["text"] = ""

l_ziedo_dydis = Label(langas, text="Žiedo dydis mm")
e_ziedo_dydis = Entry(langas, width = 6)
e_ziedo_dydis.bind(",", lambda event: kablelis())
e_ziedo_dydis.bind(".", lambda event: taskas())
l_error  = Label(langas, text="", fg='red')
l_ziedo_aukstis = Label(langas, text="Žiedo aukštis mm")
e_ziedo_aukstis = Entry(langas, width = 6)
e_ziedo_aukstis.bind(",", lambda event: kablelis())
e_ziedo_aukstis.bind(".", lambda event: taskas())
l_brilianto_dydis = Label(langas, text="Brilianto dydis mm")
e_brilianto_dydis = Entry(langas, width = 6)
e_brilianto_dydis.bind(",", lambda event: kablelis())
e_brilianto_dydis.bind(".", lambda event: taskas())
l_kokia_ziedo_dali_inkrustuosime = Label(langas, text="Pasirinkite, \nkokią žiedo dalį \ninkrustuosime \nbriliantais ", justify=RIGHT)
rb_variable = IntVar()
rb_aplink = Radiobutton(langas, text="Aplink visą žiedą", variable = rb_variable, value = 1, indicatoron = 0, width = 15, activebackground = 'white', selectcolor = 'light yellow')
rb_aplink.bind("<Button-1>", lambda event: isvalyti_error())
rb_puse = Radiobutton(langas, text="Pusę žiedo", variable = rb_variable, value = 2, indicatoron = 0, width = 15, activebackground = 'white', selectcolor = 'light yellow')
rb_puse.bind("<Button-1>", lambda event: isvalyti_error())
rb_trecdalis = Radiobutton(langas, text="Trečdalį žiedo", variable = rb_variable, value = 3, indicatoron = 0, width = 15, activebackground = 'white', selectcolor = 'light yellow')
rb_trecdalis.bind("<Button-1>", lambda event: isvalyti_error())
rb_ketvirtadalis = Radiobutton(langas, text="Ketvirtadalį žiedo", variable = rb_variable, value = 4, indicatoron = 0, width = 15, activebackground = 'white', selectcolor = 'light yellow')
rb_ketvirtadalis.bind("<Button-1>", lambda event: isvalyti_error())
l_tarpas = Label(langas, text="", height=1, fg="red")
b_skaiciuoti_briliantu_kieki = Button(langas, text="Skaičiuoti briliantų kiekį", width = 22, command=apskaiciuoti_briliantu_kieki, bg ='light grey')
l_rezultatas_kiekis_vnt = Label(langas, text="", height=2)
l_tarpas1 = Label(langas)
l_brilianto_dydis_ct = Label(langas, text="Brilianto dydis ct")
e_brilianto_dydis_ct = Entry(langas, width = 6)
e_brilianto_dydis_ct.bind(",", lambda event: kablelis())
e_brilianto_dydis_ct.bind(".", lambda event: taskas())
l_briliantu_kaina = Label(langas, text="Briliantų kaina Eur/ct")
e_briliantu_kaina = Entry(langas, width = 6)
e_briliantu_kaina.bind(",", lambda event: kablelis())
e_briliantu_kaina.bind(".", lambda event: taskas())
l_tarpas2 = Label(langas, text="", fg="red")
b_skaiciuoti_briliantu_kaina = Button(langas, text="Skaičiuoti briliantų kainą", width = 22, command=skaiciuoti_briliantu_kaina, bg ='light grey')
l_rezultatas_kaina_eur = Label(langas, text="")
l_tarpas3 = Label(langas)
l_inkrustavimo_kaina = Label(langas, text="Brilianto inkrustavimo\nkaina Eur/vnt", justify=RIGHT)
e_inkrustavimo_kaina = Entry(langas, width = 6)
e_inkrustavimo_kaina.bind(",", lambda event: kablelis())
e_inkrustavimo_kaina.bind(".", lambda event: taskas())
l_tarpas4 = Label(langas, text="", fg="red")
b_skaiciuoti_inkrustavimo_kaina = Button(langas, text="Skaičiuoti inkrustavimo kainą", width = 22, command=skaiciuoti_inkrustavimo_kaina, bg ='light grey')
l_rezultatas_inkrustavimo_kaina_eur = Label(langas, text="", height=2)
b_isvalyti = Button(langas, text="Išvalyti visus laukus", width = 22, command=isvalyti)

l_ziedo_dydis.grid(row=0, column=0, sticky=E, padx=5, pady=5)
e_ziedo_dydis.grid(row=0, column=1, sticky=W, pady=5)
l_ziedo_aukstis.grid(row=1, column=0, sticky=E, padx=5, pady=5)
e_ziedo_aukstis.grid(row=1, column=1, sticky=W, pady=5)
l_brilianto_dydis.grid(row=2, column=0, sticky=E, padx=5, pady=5)
e_brilianto_dydis.grid(row=2, column=1, sticky=W, pady=5)
l_kokia_ziedo_dali_inkrustuosime.grid(row=0, rowspan=4, column=2, sticky=N+S, pady=5)
rb_aplink.grid(row=0, column=3, sticky=W, pady=2)
rb_puse.grid(row=1, column=3, sticky=W, pady=2)
rb_trecdalis.grid(row=2, column=3, sticky=W, pady=2)
rb_ketvirtadalis.grid(row=3, column=3, sticky=W, pady=2)
l_tarpas.grid(row=3, column=0, columnspan=2, sticky=E)
l_error.grid(row=8, column=3, sticky=W)
b_skaiciuoti_briliantu_kieki.grid(row=9, column=1, columnspan =2)
l_rezultatas_kiekis_vnt.grid(row=10, column=1, columnspan =2)
l_tarpas1.grid(row=11, column=1)
l_brilianto_dydis_ct.grid(row=12, column=0, sticky=E, padx=5, pady=5)
e_brilianto_dydis_ct.grid(row=12, column=1, sticky=W, pady=5)
l_briliantu_kaina.grid(row=13, column=0, sticky=E, padx=5, pady=5)
e_briliantu_kaina.grid(row=13, column=1, sticky=W, pady=5)
l_tarpas2.grid(row=14, column=0, columnspan=2, sticky=E)
b_skaiciuoti_briliantu_kaina.grid(row=15, column=1, columnspan =2)
l_rezultatas_kaina_eur.grid(row=16, column=1, columnspan =2)
l_tarpas3.grid(row=17, column=1)
l_inkrustavimo_kaina.grid(row=18, column=0, sticky=E, padx=5, pady=5)
e_inkrustavimo_kaina.grid(row=18, column=1, sticky=W, pady=5)
l_tarpas4.grid(row=19, column=0, columnspan=2, sticky=E)
b_skaiciuoti_inkrustavimo_kaina.grid(row=20, column=1, columnspan=2)
l_rezultatas_inkrustavimo_kaina_eur.grid(row=21, column=1, columnspan =2)
b_isvalyti.grid(row=22, column=1, columnspan=2)

langas.mainloop()