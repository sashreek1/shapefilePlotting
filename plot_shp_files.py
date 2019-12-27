import geopandas as gpd
import matplotlib.pyplot as plt
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size

cities = ['Tokyo','Chennai', 'Delhi','Seoul','Bengaluru']
files = ['0','buildings.shp','landuse.shp','natural.shp','places.shp','railways.shp','roads.shp','waterways.shp']

for city in cities:
    print("\n\n")
    print("What would you like to plot for",city)
    print('\n')
    print("""Choose the shp files that you would like to plot:(separate the numbers with spaces)
1)buildings
2)landuse
3)natural
4)places
5)railways
6)roads
7)waterways
            """)
    print("\n")
    lst = list(map(int,input().split()))
    fp = "shapefilesV2/"+city+"/shape/"+files[int(lst[0])]
    data = gpd.read_file(fp)
    ax = data.plot()
    for i in range(1,len(lst)) :
        fp = "shapefilesV2/" + city + "/shape/" + files[int(lst[i])]
        data = gpd.read_file(fp)
        data.plot(ax=ax)
    title = "Map of "+city
    plt.title(title)
    plt.show()