def loopMethod(n):
    finalNumber = 1

    if n < 0:
        return "Put a number >= 0"
    
    if n == 0 or n == 1:
        return 1
    
    for i in range(1, n+1):
        finalNumber *= i
    return finalNumber

def recursiveMethod(n):
    finalNumber = 1

    if n < 0:
        return "Put a number >= 0"
    
    if n == 0 or n == 1:
        return 1
    
    return n * recursiveMethod(n-1)

def main():
    n = int(input("Number: "))
    print("Loop method: ", loopMethod(n))
    print("Recursive method: ", recursiveMethod(n))

if __name__ == "__main__":
    main()