# Length of Number

def number_length(num):

    lengtht = 0

    if num < 0:
        return 0
    
    if num <=1: 
        return 1
    
    while num >= 1:
        lengtht = lengtht + 1
        num = num / 10
    return lengtht

def main():
    n = int(input("Number: "))
    print("Length: ", number_length(n))

if __name__ == "__main__":
    main()