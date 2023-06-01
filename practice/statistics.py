def main():

    input = input("Lista: ")
    numbers = []
    for n in input.split(','):
        numbers.append(int(n))

    min = None
    max = None
    total = 0

    for n in numbers:
        if min == None:
            min = n
        if max == None:
            max = n

        if n < min:
            min = n
        if n > max:
            max = n
        
        total += n

    average = total / len(numbers)

    print("Sum: ", total)
    print("Min: ", min)
    print("Max: ", max)
    print("Average: ", average)

if __name__ == "__main__":
    main()
