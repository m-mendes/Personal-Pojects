import codecs
database = codecs.open("database.txt", "r", "utf-8")
array=[]

for line in database:
    array.append(line)

while True:
    palavra=input("Informa a palavra: ")
    marcador = 0
    tamanho = len(array)
    line = 0
    if palavra == "exit":
        database.close()
        break
    while line < tamanho:
        marcador += 1
        entrei = 0
        nova_partida = 0
        if palavra in array[line]:
            found = marcador
            print(array[line])
            for x in range(found,tamanho):
                if array[x].startswith('(') or array[x].startswith('\t'):
                    print(array[x])
                elif array[x].startswith('(') == False or array[x].startswith('\t') == False:
                    entrei = 1
                    nova_partida = x
                    break
                
        if entrei == 1:
            line = nova_partida
            marcador = nova_partida
        else:
            line += 1

