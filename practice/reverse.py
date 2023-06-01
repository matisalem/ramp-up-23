def main():
    text = str(input("text: "))
    vocalsCount = 0
    finalText = ""

    for i in text:
        finalText = finalText + i
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
            vocalsCount = vocalsCount + 1
    
    finalText = text[::-1]
    print("Final text: ", finalText)
    print("Vocal count: ", vocalsCount)

    return finalText


    

if __name__ == "__main__":
    main()