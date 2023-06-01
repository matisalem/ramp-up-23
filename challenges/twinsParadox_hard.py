def twins(age, distance, speed):

    jill = 2 * distance / speed 
    weirdFactor = (1 - speed * speed) ** 0.5

    jack = jill * weirdFactor

    ageJill = age + jill
    ageJack = age + jack
    texto = "Jack's age is " + str(round(ageJack, 1)) + ", Jill's age is " + str(round(ageJill, 1))

    return texto

def main():
    n = int(input("age: "))
    n2 = int(input("distance: "))
    n3 = int(input("speed: "))


    print(twins(n, n2, n3))

if __name__ == "__main__":
    main()