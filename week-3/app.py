#create menu for user
import csv
inventory = []
def menu():
    while True:
        print("""---MENU---
              1.add product
              2.show inventory
              3.search product
              4.update product
              5.remove product
              6.calculate statistics
              7.save CSV
              8.up data
              0.exit""")

        option = input("chosse option")
        if option == "1":
            name = input(" into a name of product: ")

        while True:    
            try:
                price = float(input("into price of product:"))
                break
            except ValueError:
                print("into a value validate") 
                
        
        while True:
            try:
                amount = int(input("into amount product: "))
                break
            except ValueError :
                print("into value validate")
                

            inventory_list = { "name": name,
                          "price": price,
                          "amount": amount}
        
            inventory.append(inventory_list)
        
        if option == "2": 
            print(inventory)

        elif option == "3":
            search_name = input("into product want search: ")
            found = False
            for item in inventory:
                if item["name"].lower() == search_name.lower():
                    print(f"product found {item}")
                    found = True
                    break
            if not found:
                print("product not found in the inventory")

        elif option == "4":
            search_name = input("into name of product want you update: ")
            for item in inventory:
                if item ["name"].lower() == search_name.lower():
                    print(f"edit : {item['name']}")
                    item["name"] = input("into new name")
                    item["price"] = float(input("into new price: "))
                    item["amount"] = int(input("into new amount"))
       
        elif option == "5":
           search_name = input("into name of product want you remove: ")
           found = False
           for item in inventory:
                if item ["name"].lower() == search_name.lower():
                   print(f"remove : {item['name']}")
                   inventory.remove(item)
                   found = True

           if not found:
                print("product not found")

        elif option == "6":
            calculate_total = 0
            for item in inventory:
                calculate_total += item["price"]* item["amount"]
            print(f"total inventory : {calculate_total}")
                
        elif option == "7":
            with open("inventory.csv", mode="w", newline="", encoding="utf-8") as mifile:
                columns = ["name", "price", "amount"]
                writer = csv.DictWriter(mifile,fieldnames=columns)
                writer.writeheader()
                writer.writerows(inventory)
            
        elif option == "8":
            with open("inventory.csv", mode="r", encoding="utf-8") as mifile:
                reader = csv.DictReader(mifile)
                for row in reader:
                    print(f"product: {row['name']} {row['price']} {row['amount']}")
        elif option == "0":
            print("program finally")
            break

        else:
            print("into valor diferent")
            
menu()