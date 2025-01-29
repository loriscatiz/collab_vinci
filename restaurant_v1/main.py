import total_bill
import ristorante

def main():
    menu = ristorante.crea_menu()
    order = ristorante.presa_comanda(menu)
    total_bill.get_recipt(order, menu)
main()