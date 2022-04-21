import csv
import matplotlib.pyplot as plt

csv_file = open('NYPD_Shooting_Incident_Data.csv')

reader = csv.DictReader(csv_file)

latitude = []
longitude = []

for row in reader:
    latitude.append(float(row['Latitude']))
    longitude.append(float(row['Longitude']))

map_boundries = [-74.4461, -73.5123, 40.4166, 41.0359]

map_image = plt.imread('map.png')

fig, ax = plt.subplots()

ax.scatter(longitude, latitude)

ax.set_ylim(map_boundries[2], map_boundries[3])
ax.set_xlim(map_boundries[0], map_boundries[1])


ax.imshow(map_image,extent=map_boundries, alpha=0.9)

plt.imsave('mapi.png',map_image)
plt.show()