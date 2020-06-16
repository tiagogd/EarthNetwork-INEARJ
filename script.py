import json, csv, os, sys

argv = sys.argv[1]

with open(argv+".txt", 'r') as fileone, open('data.json', 'w') as filetwo:
    data = fileone.read().replace('}   «{', '}, {').replace('«{', '{').replace('   ', '').replace('},', '},\n')
    filetwo.write('[')
    filetwo.write(data)
    filetwo.write(']')

with open("data.json") as file:
    datan = json.load(file)

with open(argv+".csv", "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["Time", "Type", "Latitude", "Longitude", "PeakCurrent", "IcHeight", "NumSensors", "IcMultiplicity", "CgMultiplicity"])
    for item in datan:
        csv_file.writerow([item['time'], item['type'], item['latitude'], item['longitude'], item['peakCurrent'], item['icHeight'], item['numSensors'], item['icMultiplicity'], item['cgMultiplicity']])

os.remove("data.json")