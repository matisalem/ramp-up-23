# Find the Discount

def dis(price, discount):
	return price - price * (discount/100)


def main():
    n = int(input("Number: "))
    n2 = int(input("Second number: "))

    print("discount: ", dis(n, n2))

if __name__ == "__main__":
    main()