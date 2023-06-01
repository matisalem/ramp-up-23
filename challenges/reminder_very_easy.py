# Return the Remainder from Two Numbers

def remainder(x, y):
    return x % y

def main():
    n = int(input("Number: "))
    n2 = int(input("Second number: "))

    print("Reminder: ", remainder(n, n2))

if __name__ == "__main__":
    main()