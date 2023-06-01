def end_corona(recovers, new_cases, active_cases):
    days = 0
    while active_cases > 0:
        active_cases += new_cases - recovers
        days += 1
    return days
     

def main():
    n = int(input("recovers: "))
    n2 = int(input("new cases: "))
    n3 = int(input("active cases: "))


    print("Days: ", end_corona(n, n2, n3))

if __name__ == "__main__":
    main()