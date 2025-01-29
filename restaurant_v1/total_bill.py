

def get_subtotal(row: tuple[str, int], prices: dict[str, float]):
        dish = row[0]
        quantity = row[1]
        cad_price = prices[dish]
        subtotal = cad_price * quantity
        print(f"\n#{quantity} {dish}\ncad_price: ${cad_price} \nsubtotal: ${subtotal}")
        return subtotal
    

def get_recipt(order: list[tuple[str, int]], menu: dict[str, float]):
    total = 0
    print("BILL")
    for row in order:
          total += get_subtotal(row, menu)
    print (f"\nYour total is: ${total}")
    return total

