total = 10
count = 0

quantity = int(input("How many items do you want to purchase?: "))

for _ in range(quantity):
    if total > 0:
        total -= 1
        count += 1
    else:
        
        print(f"Item {count + 1} could not be purchased, item out of stock")
        break
        
print(f"Success: {count} items purchased. Remaining items: {total}")
    
