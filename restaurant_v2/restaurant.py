def get_int_greater_or_equal_than(min_value: int) -> int:
    while True:
        try:
            retvalue: int = int(input())
            if retvalue < min_value:
                raise ValueError 
        except ValueError:
            print(f"The integer number must be >= {min_value}")
        else:
            return retvalue
        


def yes_or_no():
    answer = ""
    yes_list = ["yes", "sì", "si", "yepp", "yep"]
    no_list = ["no", "not", "nope", "nop", "none"]
    wrong = 0
    while answer.lower() not in yes_list and answer.lower() not in no_list:
        try:
            answer = input("")
            if wrong >= 4:
                print("The accepted answers are these: \n")
                print("Continue:", end="\t")
                print("Stop:")
                for i in range(len(yes_list)):
                    print(yes_list[i], end="\t\t")
                    print(no_list[i])
            if answer.lower() not in yes_list and answer.lower() not in no_list:
                print("Answer not valid\n")
                raise ValueError
        except ValueError:
            wrong+=1
    retvalue = False
    if answer in yes_list:
        retvalue = True
    return retvalue 

class Dish:
    def __init__(self, name: str, price: float, available: bool, quantity: int) -> None:
        self.name = name
        self.price = price
        self.available = available
        self.quantity = quantity

    def __str__(self):
        spaces =  40 - len(self.name)     
        return(
f"""{self.name}{spaces*' '}{self.price}"""
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
            if dish.available:
                print(dish)

    def get_menu(self):
        menu_dict: dict[str, int]= {}
        for dish in self.dishes:
            if dish.available:
                menu_dict[dish.name] = dish.quantity
        return menu_dict
    
    def get_dish_by_name(self, name: str) -> Dish | None:
        for dish in self.dishes:
            if dish.name == name:
                return dish
        return None  # Return None if the dish is not found
    
    
    

class Table:
    def __init__(self, name: str, people: int) -> None:
        self.name = name
        self.people = people

    def get_personal_order(self, menu: Menu) -> dict[str, int]:
        retvalue: dict[str, int] = {}
        menu.print_menu()
        menu_available = menu.get_menu()
        still_ordering = True
        while still_ordering:
            print("What do you want to order?")
            dish_name = input()
            if dish_name in menu_available:
                print(f"How many {dish_name} do you want?")
                quantity = get_int_greater_or_equal_than(1)
                if menu_available[dish_name] < quantity:
                    print(f"There are only {menu_available[dish_name]}, choose another dish or change the quantity")
                else:
                    retvalue[dish_name] = retvalue[dish_name] + quantity if dish_name in retvalue else quantity
                    menu.update_stock(menu.get_dish_by_name(dish_name), quantity, True) # type: ignore
                    print(f"{quantity} {dish_name} added to the order. Do you want to order again?")
                    still_ordering = yes_or_no()
            else:
                print(f"{dish_name} is not on the menu")
        return retvalue
    
    def get_table_order(self, menu: Menu):
        retvalue: dict[str, int] = {}
        for _ in range(self.people):
            personal_order = self.get_personal_order(menu)
            for dish in personal_order:
                retvalue[dish] = retvalue[dish] + personal_order[dish] if dish in retvalue else personal_order[dish]
        return retvalue 
        
    

if __name__ == '__main__':
    piatto1 = Dish("Pizza", 10.00, True, 20)
    piatto2 = Dish("Pepperoni", 12.00, True, 20)
    piatto3 = Dish("Strascinat co e cim de repe", 16.00, True, 20)
    menu = Menu([piatto1, piatto2, piatto3])
    table_test = Table("test", 3)

    table_test.get_table_order(menu)