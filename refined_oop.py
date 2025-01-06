class Buy:
    total = 10

    def __init__(self, quantity):
        if quantity < 1:
            raise ValueError("The number of items you are buying must be greater than 0")
        self.quantity = quantity

    def inventory_control(self):
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


def main():
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
    while True:
        try:
            quantity = int(input("How many items do you want to purchase?: "))
            buy = Buy(quantity)
            return buy
        except ValueError:
            print(f"Invalid input: What you have put is not a valid number")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
