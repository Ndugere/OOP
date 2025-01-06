class Buy:
    total = 10  # Shared stock for all purchases

    def __init__(self, quantity):
        self.quantity = quantity  # Validate via the setter

    def inventory_control(self):
        """
        Handles purchase logic, updating the total stock and tracking purchased items.
        """
        count = 0
        success = True
        for _ in range(self.quantity):
            if Buy.total > 0:
                Buy.total -= 1
                count += 1
            else:
                success = False
                return success, Buy.total, count
        return success, Buy.total, count

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Validates that the quantity is greater than 0.
        """
        if quantity < 1:
            raise ValueError("The number of items you are buying must be greater than 0")
        self._quantity = quantity


def main():
    """
    Main function to handle user input and process the purchase.
    """
    buy = get_info()
    success, remaining, count = buy.inventory_control()
    print()
    if success:
        print(f"Success!!: All your {count} items have been purchased successfully! \n")
        print(f"Want to make more purchases?: There are still {remaining} items remaining in our stock.")
    else:
        print(f"{count} items were purchased successfully. Remaining stock is {remaining} \n")
        print(f"Could not purchase more than {count} items.")


def get_info():
    """
    Handles user input for quantity and returns a valid Buy instance.
    """
    while True:
        try:
            quantity = int(input("How many items do you want to purchase?: "))
            return Buy(quantity)  # Return a valid Buy object
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
