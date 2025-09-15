import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide")

st.header("Geospatial Technology - Analysis | Automation | Integration")
st.markdown("---")
# st.markdown("### Featured Projects")
# st.write("Below are specific examples of my GIS skills in action.")



col1_new, col2_new = st.columns(2)
with col1_new:
    st.subheader("Skills and Techniques")
    automation_key = pd.DataFrame({
        'Description': ['Q/A', 'Raster Analysis',
                        'Hot Spot Analysis', 'Origin-Destination Diagrams',
                        '3D Analysis', 'Visualization'],
        'Project': ['Centralized GIS datasets integrity and consistency',
                    'Automatic slope/aspect constraint areas analysis for project construction',
                    'Density of competitor project filings for project siting areas',
                    'Radio communication frequencies between microwave towers',
                    '3D modelling of Fresnel Zones and wind turbine space intersections',
                    'ETL for utility and electric market data analysis and integration in ISO/RTO spectific dashboards']
    })
    automation_key.set_index('Project', inplace=True, drop=True)
    col1_new.write('### Analysis')
    col1_new.table(automation_key)


with col2_new:
    st.subheader("")
    automation_key = pd.DataFrame({
        'Project': [
            "ArcGIS Pro Tool creation",
            'ArcGIS Pro Tool creation',
            'Operational Data ETL',
            'Energy Prediction Workflow',
            'Land Control Processes'
        ],
        'Description': [
            'Viewshed analysis for DoD restricted areas',
            'Buildable land creation and integration into centralized system',
            "Remote ETL orchestration for datasets supporting EDF's project pipeline",
            "Automation of resource assessment and dataset creation",
            "API integration between EDF's GIS and contract lifecycle management platforms"
        ]
    })
    automation_key.set_index('Project', inplace=True, drop=True)
    col2_new.write('### Automation')
    col2_new.table(automation_key)



st.markdown("---")
# st.header("Sankey Diagram of Skill Flow")
col_sankey1, col_sankey2 = st.columns(2)

labels = [
    'Software',
    'ArcGIS Pro', 'ArcGIS Enterprise', 'Python', 'Arcade', 'SQL Server', 'Big Query', 'VertiGIS', 'Storage',
    'Python Toolboxes', 'Model Builder',
    'WebMaps', 'WebApps', 'Dashboards',
    'Geoprocessing Services', 'APIs', 'Scripts',
    'Symbology', 'Labels',
    'Queries', 'ETL scripts', 'Integrations',
    'Vector analysis',
    'WAB widgets', 'Experience Builder Widgets',
    'GeoDatabases', 'Parquet', 'KML',
]

source = []
target = []
values = []

# Flow from 'Software' (index 0) to second column
source.extend([0] * 8)
target.extend([1, 2, 3, 4, 5, 6, 7, 8])
values.extend([1/8] * 8)

# Flow from second column to third column
# ArcGIS Pro (1)
source.extend([1, 1])
target.extend([9, 10])
values.extend([1/16, 1/16])
# ArcGIS Enterprise (2)
source.extend([2, 2, 2])
target.extend([11, 12, 13])
values.extend([1/24, 1/24, 1/24])
# Python (3)
source.extend([3, 3, 3])
target.extend([14, 15, 16])
values.extend([1/24, 1/24, 1/24])
# Arcade (4)
source.extend([4, 4])
target.extend([17, 18])
values.extend([1/16, 1/16])
# SQL Server (5)
source.extend([5, 5, 5])
target.extend([19, 20, 21])
values.extend([1/24, 1/24, 1/24])
# Big Query (6)
source.extend([6])
target.extend([22])
values.extend([1/8])
# VertiGIS workflows (7)
source.extend([7, 7])
target.extend([23, 24])
values.extend([1/16, 1/16])
# Storage (8)
source.extend([8, 8, 8])
target.extend([25, 26, 27])
values.extend([1/24, 1/24, 1/24])


labels2 = [
    'Domain',
    'GIS Analysis', 'Modelling', 'Visualization', 'Data Engineering', 'Big data analytics', 'Sharing', 'GeoAI/ML',
    'Vector', 'Raster', '3D',
    'Statistics', 'Spatial interpolation', 'Networks', 'Suitability',
    'Mapping', 'Charts', 'Dashboards',
    'Data management', 'Data Q/A', 'Data integrity',
    'Point aggregation', 'Polygon intersections', 'In polygon stats',
    'Map publishing', 'Group and roles management', 'Permission based access',
    'Feature generation',
]

source2 = []
target2 = []
values2 = []
# Flow from 'Software' (index 0) to second column
source2.extend([0] * 7)
target2.extend([1, 2, 3, 4, 5, 6, 7])
values2.extend([1/7] * 7)

# Flow from second column to third column
# GIS Analysis (1)
source2.extend([1, 1, 1])
target2.extend([8, 9, 10])
values2.extend([1/24, 1/24, 1/24])
# Modelling (2)
source2.extend([2, 2, 2, 2])
target2.extend([11, 12, 13, 14])
values2.extend([1/32, 1/32, 1/32, 1/32])
# Visualization (3)
source2.extend([3, 3, 3])
target2.extend([15, 16, 17])
values2.extend([1/24, 1/24, 1/24])
# Data Engineering (4)
source2.extend([4, 4, 4])
target2.extend([18, 19, 20])
values2.extend([1/24, 1/24, 1/24])
# Big data analytics (5)
source2.extend([5, 5, 5])
target2.extend([21, 22, 23])
values2.extend([1/24, 1/24, 1/24])
# Sharing (6)
source2.extend([6, 6, 6])
target2.extend([24, 25, 26])
values2.extend([1/24, 1/24, 1/24])
# GeoAI/ML (7)
source2.extend([7])
target2.extend([27])
values2.extend([1/8])


link = dict(source=source, target=target, value=values)
node = dict(label=labels, pad=15, thickness=20)
data = go.Sankey(link=link, node=node)
fig = go.Figure(data)
fig.update_layout(title_text="Software", font_size=12, font_family="Inter")


link2 = dict(source=source2, target=target2, value=values2)
node2 = dict(label=labels2, pad=15, thickness=20)
data2 = go.Sankey(link=link2, node=node2)
fig2 = go.Figure(data2)
fig2.update_layout(title_text="Domain", font_size=12, font_family="Inter")

with col_sankey1:
    st.plotly_chart(fig, use_container_width=True)
with col_sankey2:
    st.plotly_chart(fig2, use_container_width=True)

