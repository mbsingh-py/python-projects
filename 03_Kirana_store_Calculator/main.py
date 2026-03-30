from random import randint
n = randint(1000, 10000)*1000

print(f"\n{'*'*25} CALCULATOR {'*'*25} \nHow to use: \n• Enter product name\n• Enter product cost\n• Press 'Enter' (empty input) to generate bill for current customer\n• Type 'stop' to end the program\n• Enter discount (%) if any after billing\n")

credited_bDis = 0     # Total amount credited before discount (Marked price)
credited_aDis = 0     # Total amount credited after discount
sale_today = {}


while True:
    print(f"\n...New Customer...")
    amount_bDis = 0
    sold_items = {}

    while True:

        while True:
            product_name = input("Enter name of product: ").strip()
            clean_name = product_name.replace(" ", "").lower()

            if clean_name == "stop":
                next_step = "end"
                break
            elif clean_name.isalpha():
                n += 1
                product_name = " ".join(product_name.split()).title()
                product_id = "p-" + clean_name[:3].ljust(3, "x") + str(n)     # Product ID generate
                next_step = "add"
                break
            elif clean_name == "":
                next_step = "calculate"
                break
            else:
                print("Only alphabets and spaces are allowed!")

        if next_step == "add" and clean_name != "stop":
            while True:
                try:
                    product_price = int(input("Enter the product cost: "))
                except ValueError:
                    print("Only digits are allowed!")
                    continue
                if product_price < 0:
                    print("Only positive value are allowed!")
                else:
                    break
            
            amount_bDis += product_price
            sold_items[product_id] = {"name": product_name, "price": product_price}
            continue

        if (next_step == "calculate" or next_step == "end") and len(sold_items) == 0:
            break

        if (next_step == "calculate" or next_step == "end") and len(sold_items) != 0:

            while True:
                dis = input("Enter discount(%) if any: ").strip()
                cleaned_dis = dis.replace(" ", "")
                if cleaned_dis.isdigit() and 0 <= int(cleaned_dis) <= 100:
                    discount_percent = int(cleaned_dis)
                    break
                elif cleaned_dis == "":
                    discount_percent = 0
                    break
                else:
                    print("Enter valid discount if any or enter '0' or press 'Enter' in case of no discount!")

            amount_aDis = round(amount_bDis * (1 - (discount_percent/100)))

            credited_bDis += amount_bDis
            credited_aDis += amount_aDis

            print(f"\n{'*'*15} Items Purchased {'*'*15} \n{'S No.':<5}  {'Product name:':<18} {'Product ID:':<18} {'Price:'} ")

            s_no = 0
            for key, value in sold_items.items():
                s_no += 1
                print(f"{s_no:>3}    {value['name']:<18} {key:<18} {value['price']:<18}")
            
            print(f"\n{'Marked price:':<30} {amount_bDis} \n{'Price after discount:':<30} {amount_aDis}")
            
            sale_today.update(sold_items)

            print(f"{'*'*15} Signing off for current Customer! {'*'*15}\n")
            break

    if len(sale_today) != 0 and next_step == "end":

        print(f"\n\n{'*'*15} SALE TODAY {'*'*15} \n{'S No.':<5}  {'Product name:':<18} {'Product ID:':<18} {'Price:'} ")
        
        s_no = 0
        for key, value in sale_today.items():
            s_no += 1
            print(f"{s_no:>3}    {value['name']:<18} {key:<18} {value['price']:<18}")
        
        print(f"{'Total amount before discount:':<40} {credited_bDis} \n{'Total amount after discount:':<40} {credited_aDis}")
        break
    if (next_step == "calculate" or next_step == "end") and len(sale_today) == 0:
        print(f"\nNo sale today \nHave a nice day")
        break

print(f"\n{'*'*15} Signing off for Today! {'*'*15}\n")
