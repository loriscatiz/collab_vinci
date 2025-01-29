"""
creare un dizionario con  i piatti e il prezzo          OK
creare la gestione degli ordini che faccia uscire una lista di tuple
la tupla avrà due indici 0 piatto 1 quantità
"""
def quante_persone():
    number = 0
    while number < 1:
        try:
            number = int(input("\n"))
        except ValueError:
            print("Inserisci un valore valido\n")
    return number

def crea_menu():
    menu = {"Bruschette al pomodoro": 3, 
            "Carpaccio di manzo": 8, 
            "Risotto ai funghi porcini":12,
            "Tagliatelle al ragù": 15, 
            "Bistecca alla Fiorentina": 20, 
            "Orata al forno con patate": 12, 
            "Verdure grigliate": 3, 
            "Patate al forno":5, 
            "Tiramisù":10, 
            "Panna cotta ai frutti di bosco":10}
    return menu

def stampa_menu(menu):
    max_len = 0
    for i in menu:
        if len(i) > max_len:
            max_len = len(i)
    for i in menu:
        print(i," "*(max_len-len(i)), menu[i])

def cosa_vuoi_ordinare(menu):
    retvalue = " "
    while len(retvalue) <= 2:
        try:
            retvalue = input("")
            if retvalue not in menu:
                raise ValueError
        except ValueError:
            print("Mi dispiace non è presente nel menù, scegli un piatto fra questi\n")
            stampa_menu(menu)
    return retvalue

def Yes_or_no():
    retvalue = ""
    yes_list = ["yes", "sì", "si", "yepp", "yep"]
    no_list = ["no", "not", "nope", "nop", "none"]
    wrong = 0
    while retvalue.lower() not in yes_list and retvalue.lower() not in no_list:
        try:
            retvalue = input("")
            if wrong >= 4:
                print("Coglione devi inserire uno di questi comandi\n")
                print("Continua:", end="\t")
                print("Stoppa:")
                for i in range(len(yes_list)):
                    print(yes_list[i], end="\t\t")
                    print(no_list[i])
            if retvalue.lower() not in yes_list and retvalue.lower() not in no_list:
                print("Inserisci un valore consono\n")
                raise ValueError
        except ValueError:
            wrong+=1
    continua = False
    if retvalue in yes_list:
        continua = True
    return continua 

def presa_comanda(menu):
    print("Qaunti siete al tavolo?")
    clienti = quante_persone()
    print("")
    stampa_menu(menu)
    print("")
    retvalue = []
    for i in range(clienti):
        continua_ordine = True 
        while continua_ordine == True:
            print(f"cliente {i+1} cosa vuoi ordinare e quanto?\n")
            tupla = cosa_vuoi_ordinare(menu), quante_persone()
            retvalue.append(tupla)
            print("Vuoi ordinare qualcos'altro?\n")
            continua_ordine = Yes_or_no()
    return retvalue

if __name__ == "__main__":
    menu = crea_menu()
    presa_comanda(menu)