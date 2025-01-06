total = 10
count = 0

quantity = int(input("How many items do you want to purchase?: "))

for _ in range(quantity):
    if total > 0:
        total -= 1
        count += 1
        success = True
    else:
        success = False
if success:
    print(f"Success: {count} items purchased. Remaining items: {total}")
else:
    print(f"Success: {count} items purchased. Remaining items: {total}")
    count += 1
    print(f"Item {count} could not be purchased, item out of stock")
