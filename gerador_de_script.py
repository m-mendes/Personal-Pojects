from openpyxl import Workbook, load_workbook


vlans = ["gerenciamento","servidor","catracas","pontos","desktop_cabeado","desktop_wireless","impressoras","mobile","Guest"]
infoSwitch = load_workbook('levantamento switches.xlsx')
for switch in range(25):
    
    nome_arquivo = "SWTESTE"+str(switch+1)+".txt"
    arquivo = open(nome_arquivo, "w")
    possicao_vlans = 0
    abaInfoSwitch = infoSwitch[f'SW{switch+1}']
    for vlan in range(10,100,10):
        arquivo.write(f"vlan {vlan}")
        arquivo.write("\n")
        arquivo.write("\n")
        arquivo.write(f"name {vlans[possicao_vlans]}")
        arquivo.write("\n")
        arquivo.write("\n")
        possicao_vlans+=1
        arquivo.write("exit")
        arquivo.write("\n")
        arquivo.write("\n")
        if (switch+1) == 1:
            arquivo.write(f"interface vlan {vlan}")
            arquivo.write("\n")
            arquivo.write("\n")
            arquivo.write(f"ip address 10.80.{vlan}.0 255.255.255.0")
            arquivo.write("\n")
            arquivo.write("\n")
            arquivo.write("exit")
            arquivo.write("\n")
            arquivo.write("\n")

    for i in range(25):
        arquivo.write(f"interface ethernet1/1/{i+1}")
        arquivo.write("\n")
        arquivo.write("\n")
        arquivo.write(f"description {abaInfoSwitch[f'B{i+2}'].value}")
        arquivo.write("\n")
        arquivo.write("\n")
        if abaInfoSwitch[f'C{i+2}'].value == "ACCESS":
            arquivo.write("switchport mode access ")
            arquivo.write("\n")
            arquivo.write("\n")
            arquivo.write(f"switchport access vlan {abaInfoSwitch[f'D{i+2}'].value}")
            arquivo.write("\n")
            arquivo.write("\n")
        else:
            arquivo.write("switchport mode trunk ")
            arquivo.write("\n")
            arquivo.write("\n")
            arquivo.write("switchport trunk native vlan 10 ")
            arquivo.write("\n")
            arquivo.write("\n")
            arquivo.write("switchport trunk allowed vlan add 10,20,30,40,50,60,70,80,90 ")
            arquivo.write("\n")
            arquivo.write("\n")
        arquivo.write("exit")
        arquivo.write("\n")
        arquivo.write("\n")

    arquivo.close()
