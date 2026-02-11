import sys

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print("none")
else:
    n = int(sys.argv[1])

    i = 0
    while i <= 10:
        print("Table de " + str(i) + ":", end=" ")

        j = 0
        while j <= 10:
            print(i * j, end=" ")
            j += 1

        print()
        i += 1
