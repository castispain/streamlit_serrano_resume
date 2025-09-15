import streamlit as st

st.header("Geospatial Technologies")
st.markdown("""
<p style="font-size:1.1rem; text-align:justify;">
Throughout my 20-year career, I have the opportunity to gain first hands experience in a wide range of GIS technologies. From the early days of ESRI's desktop software like ArcInfo and ArcView to the modern, integrated ArcGIS Pro and Enterprise solutions we use today.

My hands-on experience includes a platform transitions from the early days of ArcMap and MapInfo in a Citrix server to a really recent multi clustered ESRI deployment in AWS.
I have extensively leveraged relational databases, including SQL Server with SDE technology and the robust open-source capabilities of PostGIS, to the scalable Big Query in Google Cloud, to manage and analyze geospatial datasets.
My technical foundation is anchored in Python, which I have used to automate geoprocessing workflows, build efficient ETL pipelines for data integration, integrate platforms using APIs, and develop custom tools that streamline operations. 

My current intersts lay in leveraging big data with Spark for predicting modelling and applying machine learning and other GeoAI techniques to boost insights and decision making.
</p>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    st.subheader("Geospatial platform")
    st.image("images/gis_platform.jpg", use_container_width=True)
    st.markdown("Desktop and Web for GIS")
with col2:
    st.subheader("Customizing GIS")
    st.image("images/etl_workflow.jpg", use_container_width=True)
    st.markdown("Custom web widgets with VertiGIS workflows")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Raster and 3D analysis")
    st.image("images/iec_3d.PNG", use_container_width=True)
    st.markdown("Complex Terrain Analysis for IEC Norm")

with col2:
    st.subheader("Vector analysis and statistics")
    st.image("images/lcoe_bl_2.png", use_container_width=True)
    st.markdown("Least Cost of Energy (LCOE)")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Big Geospatial Data Processing")
    st.image("images/big data.png", use_container_width=True)
    st.markdown("Grid schema for parallel processing")

with col2:
    st.subheader("Systems Integration")
    st.image("images/lcm 1.jpg", use_container_width=True)
    st.markdown("ArcGIS Enterprise and Malbek integration")
