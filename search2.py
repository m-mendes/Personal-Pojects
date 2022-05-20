import codecs
database = codecs.open("database.txt", "r", "utf-8")
entrei = 0
while True:
    palavra = input("Informa a palavra: ")
    if palavra == "exit":
        database.close()
        break
    else:
        for line in database:
            if palavra in line:
                entrei = 1
                print(line)
                continue
            if entrei == 1:
                if line.startswith("(") or line.startswith("    "):
                    print(line)
                else:
                    entrei = 0
