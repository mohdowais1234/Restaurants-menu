menu = {
'pizza':140,
'pasta':90,
'burger':80,
'coffee':60,
'momos':70,
'french fries':89,
'Chawmin':80,
'Dosa':120,
'Roasted':79,
'salad':70,
}
print("WELCOME TO OUR RESTAURANT")
print("pizza: Rs 140\n pasta: Rs 99\n burger: Rs 80\n coffee: Rs 60\n momos: Rs 70\n french fries: Rs 89\n Chawmin: Rs 80\n Dosa: Rs 120\n Roasted: Rs 79\n salad: Rs 70")

order_total = 0
item_1= input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"order item {item_1} is not available yet! ")

another_order = input("Do you want to another item? (yes/No) ")
if another_order == "yes":
    item_2 = input("Enter the name of second item =")    
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available")  
another_order = input("Do you want to another item? (yes/No) ")
if another_order == "yes":
    item_3 = input("Enter the name of third item =")    
    if item_3 in menu:
        order_total +=menu[item_3]
        print(f"Item {item_3} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available")         
    
print(f"The total amount of item  to pay is {order_total}")





