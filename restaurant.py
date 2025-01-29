class Dish:
    def __init__(self, name: str, price: float, available: bool, quantity: int) -> None:
        self.name = name
        self.price = price
        self.available = available
        self.quantity = quantity

    def __str__(self):
        spaces =  40 - len(self.name)     
        return(
f"""{self.name}{spaces*' '}{self.price}{self.available}"""
        )
    def set_available(self, value: bool):
        self.available = value

    def update_quantity(self, quantity: int):
        self.quantity += quantity
        if self.quantity <= 0:
            self.set_available(False)
        else:
            self.set_available(True)
    
    def update_price(self, new_price: float):
        self.price = new_price
    


class Menu:
    def __init__(self, dishes: list[Dish]) -> None:
        self.dishes = dishes

    def add_new_dish(self, dish: Dish):
        self.dishes.append(dish)
    
    def update_stock(self, dish: Dish, quantity: int, remove: bool): #Change name of method
        if remove:
            dish.update_quantity(-quantity)
        else:
            dish.update_quantity(quantity)


    def print_menu(self):
        print(f"Dish:{35*" "}Price:", end="\n\n")
        for dish in self.dishes:
            print(dish)

class Table:
    def __init__(self, people: int) -> None:
        self.people = people

if __name__ == '__main__':
    piatto1 = Dish("Pizza", 10.00, True, 20)
    piatto2 = Dish("Pepperoni", 12.00, True, 20)
    piatto3 = Dish("Strascinat co e cim de repe", 16.00, True, 20)
    menu = Menu([piatto1, piatto2, piatto3])
    menu.print_menu()
    menu.update_stock(piatto3, 22, True)
    menu.update_stock(piatto3, 22, True)
    menu.update_stock(piatto3, 22, False)
    menu.print_menu()