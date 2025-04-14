import geopandas as gpd
import pyproj 
from shapely.ops import transform
import plotly.express as px
from sqlalchemy import create_engine
import pandas as pd
import json

### Get the data from the database

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)
cursor = engine.raw_connection().cursor()

selectQuery = """
    SELECT Jahr, Einkommen_unselbstaendige_Erwerbstaetigkeit
    FROM haushaltseinkommen
"""
cursor.execute(selectQuery)

""" old school solution
result = cursor.fetchall()
for row in result:
    jahr , einkommen = row
    print(f"Jahr: {jahr}, Einkommen: {einkommen}") """

df = pd.read_sql(selectQuery, engine)
print(df.head())

cursor.close()
engine.dispose()

### Read the shapefile using geopandas

f=r"swissBOUNDARIES3D_1_5_TLM_KANTONSGEBIET.shp"
shapes = gpd.read_file(f)
shapes["geometry"] = shapes["geometry"].simplify(0.5)

# Define CRS using pyproj.CRS
lv03 = pyproj.CRS.from_epsg(21781) 
wgs84 = pyproj.CRS.from_epsg(4326) 
project = pyproj.Transformer.from_crs(lv03, wgs84, always_xy=True).transform

for i, shape in shapes.iterrows():
    if shape.geometry is not None:
        shape.geometry = transform(project, shape.geometry)
        shapes.iloc[i] = shape 

gdf=gpd.GeoDataFrame(columns=shapes.columns)

for i, shape in shapes.iterrows():
  if shape.geometry is not None:
    if shape.NAME in gdf.NAME.values:
      available_geometry = gdf.loc[gdf.NAME == shape.NAME, 'geometry'].geometry.values
      gdf.loc[gdf.NAME == shape.NAME, 'geometry'] = available_geometry.union(shape.geometry)
    else:
      gdf = pd.concat([gdf, gpd.GeoDataFrame([shape], columns=gdf.columns)], ignore_index=True)

gdf=gdf.rename(columns={'EINWOHNERZ':'Inhabitants'})

for col in gdf.select_dtypes(include=['datetime64[ns]', 'datetimetz']).columns:
    gdf[col] = gdf[col].astype(str)

geojson_data = json.loads(gdf.to_json())

print(gdf.geometry.is_valid.sum())
print(gdf['Inhabitants'].isnull().sum())
print(geojson_data['features'][:2]) 

figure = px.choropleth_map(
    gdf,
    geojson=geojson_data,
    locations=gdf.index,
    color='Inhabitants',
    hover_name='NAME',
    color_continuous_scale='algae',
    map_style="white-bg",  # renamed param
    zoom=6.3,
    center={"lat": 46.8, "lon": 8.5},
    opacity=0.5,
)

figure.update_geos(fitbounds="locations", visible=False)

figure.show()