TOTAL = 10

def main():
    success, purchased, remaining = inventory()
    print()
    if success:
       
        print(f"Successfully purchased all {purchased} items, {remaining} still in stock. \n")
    else:
        print(f"Successfully purchased {purchased} items.\n")
        print(f"Could not successfully purchase item number {purchased + 1} and above since {remaining}  are in stock.")

def inventory():
    global TOTAL
    success = True
    count = 0
    
  
    while True:
        try:
            purchase = int(input("How many items do you want to purchase?: "))
            if purchase > 0:
                break
            else:
                print("Enter a value greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
   
    for _ in range(purchase):
        if TOTAL > 0:
            count += 1
            TOTAL -= 1
        else:
            success = False
            return success, count, TOTAL
    return success, count, TOTAL

if __name__ == "__main__":
    main()
