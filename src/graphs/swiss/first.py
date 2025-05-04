from sqlalchemy import create_engine
import pandas as pd
import plotly.graph_objects as go

engine = create_engine('mysql+mysqlconnector://root:MScBINA2025-@localhost/bina', echo=False)
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

df['text'] = df['Jahr'].astype(str) + '<br>' + df['Einkommen_unselbstaendige_Erwerbstaetigkeit'].astype(str)
limits = [(0,6000), (6000,6100), (6100, 6200), (6200, 6300), (6300, 7000)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
scale = 5000

figure = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    def_sub = df[lim[0]:lim[1]]
    figure.add_trace(go.Scattergeo(
        locationmode = 'Switzerland',
        lon = def_sub['Jahr'],
        lat = def_sub['Einkommen_unselbstaendige_Erwerbstaetigkeit'],
        text = def_sub['text'],
        marker = dict(
            size = def_sub['Einkommen_unselbstaendige_Erwerbstaetigkeit'] / scale,
            color = colors[i],
            line_color = 'black',
            line_width = 0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])
    )) 
    
  

""" figure.update_layout(
        title_text = '2014 US city populations<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope = 'switzerland',
            landcolor = 'rgb(217, 217, 217)',
        )
    ) """

figure.show()
    