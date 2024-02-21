
import csv
num2 = 0
num1 = 0
pokemons = []
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. Check first 10 pokemons")
    print("7. Check last 10 pokemons")
    print("8. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        seqnum = input("Please enter the number (0-799): ")
        if float(seqnum) > 799:
            print("")
            print("There is no such pokemon with id",int(seqnum))
        else:
            print("")
            print(pokemons[int(seqnum)])
            pass
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
        pass
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        text = input("Please enter the text: ")
        Searchbytext = [x for x in pokemons if text in x]
        print(Searchbytext)
        pass
    elif choice == '5':
        lengh = input("Please enter the lengh: ")
        Searchbylengh = [x for x in pokemons if len(x) == int(lengh)]
        print(Searchbylengh)
        pass
    elif choice == '6':
        print(pokemons[:10])
        pass
    elif choice == '7':
        print(pokemons[-10:-1])
        pass
    elif choice == '8':
        next = input("Press N to show next 10 pokemons (Press q to quit): ")
        while next != "n":
            if next == "n":
                print(pokemons[0+num1:10+num2])
                num1 = num1 + 10
                num2 = num2 + 10
            elif next == "q":
                print("somethn")
    elif choice == '9':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 8")

    print("==========================")
