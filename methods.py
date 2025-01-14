class Inventory:
    total = 10
    
    def __init__(self, item):
        self.item = item
    
    def bought(self):
        count = 0
        success = True
        for _ in range(self.item):
            if Inventory.total > 0:
                count += 1
                Inventory.total -= 1
            else:
                success = False
                break
        return {"count": count, "balance": Inventory.total, "success": success}
    
    @classmethod
    def get(cls):
        while True:
            try:
                item = int(input("Enter the number of items you want to buy: "))
                buy = Inventory(item)
                return buy
            except TypeError:
                print()
                print("You have not entered a valid number.\n")
            except Exception as e:
                print()
                print(f"{e} \n")

    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, item):
        if item < 0:
            raise ValueError("Invalid number. Enter a number greater than 0.")
        self._item = item
    
def main():
    info = Inventory.get()
    results = info.bought()
    print()
    if results["success"]:
        print(f"Success! All your {results['count']} items have been bought successfully.\n")
        print(f"Need to make other purchases? There are still {results['balance']} items available.")
    else:
        print(f"{results['count']} items were purchased successfully.\n")
        print(f"Could not purchase any item from item {results['count'] + 1} since there are no remaining items in the store.")

if __name__ == "__main__":
    main()
