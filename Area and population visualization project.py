
import pandas as pd
cities = pd.read_csv("India_cities.csv")


print(cities.head(9))



# extracting the data we are interested in
latitude, longitude = cities["latd"], cities["longd"]
population, area = cities["population_total"], cities["area_total_km2"]




# to scatter the points, using size and color but without label
import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
plt.scatter(longitude, latitude, label=None, c=np.log10(population),
            cmap='viridis', s=area, linewidth=1, alpha=0.5)
# plt.axis(aspect='equal')
plt.xlabel('Longitude')
plt.ylabel('Longitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)
# now we will craete a legend, we will plot empty lists with the desired size and label
for area in [100, 200, 300, 400, 500, 700]:
    plt.scatter([], [], c='k', alpha=0.7, s=area, label=str(area) + 'km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Areas')
plt.title("Area and Population of India Cities")
plt.show()


# In[ ]:




