import streamlit as st

st.header("Applied Technology")
st.markdown("""
<p style="font-size:1.1rem; text-align:justify;">
    Leveraging my expertise in GIS and scripting, I solve complex engineering and data challenges to deliver tangible solutions that directly address core business objectives. 
</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Grid scale solar projects support")
    st.image(r"images/solar farm.png", use_container_width=True)
    st.markdown("")
with col2:
    st.subheader("Wind projects support")
    st.image(r"images/wind wake.png", use_container_width=True)
    st.markdown("")

st.markdown("---")

st.subheader("Wind, solar, BESS, and siting buildable land generation")
st.image(r"images/buildable land.png", use_container_width=True)
st.markdown("Custom tools for ArcGIS Pro and Enterprise, including US wide datasets for initial generic buildable land and scenario based for siting")


st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("3D communications and turbine space intersections")
    st.image(r"images/fresnelzones.png", use_container_width=True)
    st.markdown("Custom tool for calculating 3D communication paths and turbine spaces")
with col2:
    st.subheader("Production and cost of energy")
    st.image(r"images/lmp_weighted resources.png", use_container_width=True)
    st.markdown("ETL and report for analysis of 10 min energy production and costs time series")
st.markdown("---")

st.subheader("Land campaign design and land control")
col1, col2 = st.columns(2)
with col1:
    st.image("images\\lcm_roles_and_tech.jpg", use_container_width=True)
    st.markdown("Systems integration and custom tool development to allow the departments involved in land control"
                " to carry on their specific tasks on a centralized system")
with col2:
    st.image(r"images/land control.png", use_container_width=True)
    st.markdown("ETL and report for analysis of 10 min energy production and costs time series")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Environmental risk analysis")
    st.image(r"images/fathom flood.png", use_container_width=True)
    st.markdown("Flood risk analytics by potential parcel for different return periods.")
with col2:
    st.subheader("Fire incidents aggregation")
    col3, col4, col5 = st.columns([1, 5, 1])
    with col4:
        st.image(r"images/fire clustering.png", width='content')
    st.markdown("Number of fire incidents weighted by severity summarized using H3 spatial indexes")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Multifactor suitability modelling")
    st.image(r"images/models factors to suitability 1.png", width='content')
    st.markdown("")
with col2:
    st.subheader("")
    st.image(r"images/models factors to suitability 2.png", width='stretch')
st.markdown("Weighted multifactor raster model for wind project suitability using logic analysis.")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("GIS based grading for cut-and-fill analysis")
    st.image(r"images/cutfill_profile.png", use_container_width=True)
    st.markdown("Determination of the best grading surface")
with col2:
    st.subheader("")
    st.image(r"images/cutfill_dashboard.png", use_container_width=True)
    st.markdown("Making results accessible")
st.markdown("---")


