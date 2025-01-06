class Purchased:
    total = 10

    def __init__(self, quantity):
        if quantity < 0:
            raise ValueError("The quantity entered must be greater than 0")
        self.quantity = quantity

    def inventory(self):
        count = 0
        success = True
        for _ in range(self.quantity):
            if Purchased.total > 0:
                Purchased.total -= 1
                count += 1
            else:
                success = False
                return success, count, Purchased.total
        return success, count, Purchased.total


def main():
    success, count, purchase = get_infor()
    print()
    if success:
        print(f"All items {count} have been purchased successfully\n")
        print(f"{purchase} still remain in stock")
    else:
        print(f"{count} items have been purchased successfully\n")
        print(f"Unfortunately, the {count + 1} item could not be purchased since {purchase} remain in stock.")


def get_infor():
    while True:
        try:
            quantity = int(input("Kindly enter the number of items you want to purchase: "))
        except ValueError as e:
            print(e)
        else:
            break
    return Purchased(quantity).inventory()


if __name__ == "__main__":
    main()
