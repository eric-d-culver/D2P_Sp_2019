#!/usr/bin/python3

import csv

fout = open('fire_police.dat', 'w')

### Read data from CSV files ###

polDat = []

with open('police_stations_lat_and_lon.csv', 'r') as polFile:
    polCSV = csv.reader(polFile, delimiter=',')
    for i, row in enumerate(polCSV):
        if i is 0:
            for j in range(len(row)):
                if row[j] == 'POLICE_STATION_NUM':
                    namej = j
                if row[j] == 'REAL_LAT':
                    latj = j
                if row[j] == 'REAL_LON':
                    lonj = j
        else:
            polDat.append([])
            polDat[i-1].append(row[namej])
            polDat[i-1].append(int(row[latj])*(10**(-6)))
            polDat[i-1].append(int(row[lonj])*(10**(-6)))

fireDat = []

with open('fire_stations_lat_and_lon.csv', 'r') as fireFile:
    fireCSV = csv.reader(fireFile, delimiter=',')
    for i, row in enumerate(fireCSV):
        if i is 0:
            for j in range(len(row)):
                if row[j] == 'FIRE_STATION_NUM':
                    namej = j
                if row[j] == 'REAL_LAT':
                    latj = j
                if row[j] == 'REAL_LON':
                    lonj = j
        else:
            fireDat.append([])
            fireDat[i-1].append(row[namej])
            fireDat[i-1].append(int(row[latj])*(10**(-6)))
            fireDat[i-1].append(int(row[lonj])*(10**(-6)))

accDat = []

with open('Accidents_fatal.csv', 'r') as accFile:
    accCSV = csv.reader(accFile, delimiter=',')
    for i, row in enumerate(accCSV):
        if i is 0:
            for j in range(len(row)):
                if row[j] == 'CRASH_NUM':
                    namej = j
                if row[j] == 'REAL_LAT':
                    latj = j
                if row[j] == 'REAL_LON':
                    lonj = j
        else:
            accDat.append([])
            accDat[i-1].append(row[namej])
            accDat[i-1].append(int(row[latj])*(10**(-6)))
            accDat[i-1].append(int(row[lonj])*(10**(-6)))

#print(fireDat[4])

### Clean up accident lat/lon ###

for row in accDat:
    if row[1] > 300:
        row[1] /= 10
    if row[2] < -1000:
        row[2] /= 10

### Write in AMPL Data file format ###

fout.write("data;\n")

fout.write("\nparam: POLICE: px py :=")

for row in polDat:
    fout.write("\n%s %.6f %.6f" % tuple(row))

fout.write(" ;\n")

fout.write("\nparam: FIRE: fx fy :=")

for row in fireDat:
    fout.write("\n%s %.6f %.6f" % tuple(row))

fout.write(" ;\n")

fout.write("\nparam: ACCIDENT: ax ay :=")

for row in accDat:
    fout.write("\n%s %.6f %.6f" % tuple(row))

fout.write(" ;\n\n")
