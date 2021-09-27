import csv
import json
import os
import sys

argv = sys.argv[1]

if len(argv) != 8:
    print("Digite: python script.py AAAAMMDD")
else:
    with open(argv, 'rb') as fileone, open('data.json', 'w') as filetwo:
        data = fileone.read()

# Removendo lixo no fim do arquivo, se houver
        data = re.sub(b'}.*?$',b'}',\
# Removendo lixo no inicio do arquivo
            re.sub(b'^.*?{',b'{',\
# Removendo todo o lixo entre dois objetos JSON quaisquer (assumo aqui que nao havera objetos JSON aninhados)
            re.sub(b'}.*?{',b'}, \n{', data)))
# Transformando em string e adicionando colchetes
        data = '[' + data.decode('utf-8') + ']'

    filetwo.write(data)

    with open("data.json") as file:
        dj = file.read()
        dj = json.loads(dj)

    with open(argv+".csv", "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(["Time", "Type", "Latitude", "Longitude", "PeakCurrent", "IcHeight", "NumSensors", "IcMultiplicity", "CgMultiplicity"])
        for item in dj:
            csv_file.writerow([item['time'], item['type'], item['latitude'], item['longitude'], item['peakCurrent'], item['icHeight'], item['numSensors'], item['icMultiplicity'], item['cgMultiplicity']])

    os.remove("data.json")
