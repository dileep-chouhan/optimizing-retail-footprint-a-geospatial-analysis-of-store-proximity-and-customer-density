import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
# --- 1. Synthetic Data Generation ---
# Generate synthetic data for store locations, customer density, and competition
np.random.seed(42)  # for reproducibility
num_stores = 20
num_customers = 1000
# Store locations (randomly generated coordinates)
store_locations = gpd.GeoDataFrame(
    geometry=[Point(np.random.rand()*10, np.random.rand()*10) for _ in range(num_stores)],
    crs="EPSG:4326"
)
store_locations['StoreID'] = range(1, num_stores + 1)
# Customer locations (randomly generated coordinates)
customer_locations = gpd.GeoDataFrame(
    geometry=[Point(np.random.rand()*10, np.random.rand()*10) for _ in range(num_customers)],
    crs="EPSG:4326"
)
# Customer density (simplified - could be replaced with more sophisticated density estimation)
customer_locations['Density'] = np.random.randint(1, 10, size=num_customers)
# Competitor locations (randomly generated coordinates)
competitor_locations = gpd.GeoDataFrame(
    geometry=[Point(np.random.rand()*10, np.random.rand()*10) for _ in range(num_stores)],
    crs="EPSG:4326"
)
competitor_locations['CompetitorID'] = range(1, num_stores + 1)
# --- 2. Analysis ---
# Calculate distances between stores and customers (simplified - using Euclidean distance)
#  In a real-world scenario, you'd use a more appropriate distance metric considering the Earth's curvature.
#  Geopandas' spatial join functionality would be more efficient for large datasets.
# --- 3. Visualization ---
# Plot store and customer locations
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
store_locations.plot(ax=ax, color='red', markersize=50, label='Stores')
customer_locations.plot(ax=ax, color='blue', markersize=5, alpha=0.5, label='Customers')
competitor_locations.plot(ax=ax, color='green', markersize=30, label='Competitors')
ax.set_title('Store Locations, Customer Density, and Competitors')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.legend()
plt.tight_layout()
output_filename = 'store_customer_map.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
#Further analysis (example):  Calculate proximity scores, identify areas with high customer density and low competition.
#This would involve more sophisticated geospatial analysis techniques not shown here for brevity.