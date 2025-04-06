India Cities: Area vs Population Visualization

This project visualizes the population and area of Indian cities using a scatter plot. The data is extracted from a CSV file containing latitude,
longitude, population, and area information of various cities in India.

1- Project Objective:

     To create a clear and interactive scatter plot to visualize:

     The geographic spread (latitude & longitude) of cities in India

     The population density using color (log scale)

      The total area using marker size

2- Dataset:
The project uses a dataset named India_cities.csv with the following relevant columns:

    latd: Latitude of the city

    longd: Longitude of the city

    population_total: Total population of the city

    area_total_km2: Total area of the city in square kilometers

3- Requirements:
Install dependencies using pip:

    pip install pandas matplotlib seaborn numpy

4- How to Run:
   Make sure you have India_cities.csv in your working directory.

   Run the Python script:

     python city_plot.py

   This will generate a scatter plot with:

         Color representing log-scaled population

         Marker size representing city area

         Location based on coordinates

5- Sample Output:
   A scatter plot showing:

     Cities positioned by geographic coordinates

     Larger markers for cities with bigger area

     Darker colors for more populated cities

6- Customization:
    
     You can adjust the plt.clim() values to focus on different population ranges.

     Add more cities or update the CSV for better coverage.

7- Libraries Used:

     Pandas

     NumPy

     Matplotlib

     Seaborn




