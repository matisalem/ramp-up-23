# Count the digits

def digits_count(n):
    while n != int(n):
        n *= 10

    lengtht = 0

    if n == 0:
        return 1
    
    if n < 0:
        n = -n 
    
    while n >= 1:
        lengtht = lengtht + 1
        n = n / 10
    return lengtht

def main():
    n = float(input("Number: "))
    print("Count: ", digits_count(n))

if __name__ == "__main__":
    main()