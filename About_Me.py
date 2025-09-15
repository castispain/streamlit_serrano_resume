import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime


def employment_history():

    today = datetime.today().strftime('%Y-%m-%d')

    df = pd.DataFrame([
        dict(Task="GIS Analyst", Start='2003-12-01', Finish='2007-01-01', Resource="TÉCNICA Y PROYECTOS SA"),
        dict(Task="GIS Specialist", Start='2007-01-01', Finish='2008-07-01', Resource="TELVENT INTERACTIVA"),
        dict(Task="GIS Consultant", Start='2008-07-01', Finish='2009-09-01', Resource="EPTISA-TI"),
        dict(Task="GIS Programmer/Analyst", Start='2010-09-01', Finish='2021-08-01', Resource="EDF Power Solutions"),
        dict(Task="Technical Lead <br> Geospatial Developer", Start='2021-08-01', Finish=today, Resource="EDF Power Solutions"),
    ])
    color_map = {
        'Sunrun': '#14a2d9',
        'EDFR': '#272f6a',
        'Nevados': '#f26543'
    }
    fig = px.timeline(
        df,
        x_start="Start", x_end="Finish", y="Resource",
        color="Resource", color_discrete_map=color_map,
        text='Task'
        )
    fig.update_traces(textposition='inside')

    fig.update_layout(
        title="Employment History",
        yaxis_title="Position"
        )

    return fig


st.set_page_config(
    page_title="Jose Luis Serrano Castillejo - Portfolio",
    layout="wide",
)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    st.image("images/headshot.jpg", width=200)
    st.markdown("<h2 style='text-align: center;'>Jose Luis <br> Serrano Castillejo</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #495057;'>Technical Lead <br> Geospatial Development</h3>",
                unsafe_allow_html=True)

    st.divider()

    st.subheader("Contact & Location")
    st.markdown("""
    - **Email:** casti_spain@hotmail.com
    - **Phone:** +1 858 248 9119
    - **Location:** Salzburg, Austria
    """)

# --- MAIN PAGE CONTENT ---
st.title("About Me")

st.markdown("""
Hello, my name is Jose Luis, and I am a GIS professional with a strong interest in applying spatial modeling and programming to solve business problems. My academic background is in Agricultural Engineering and Geospatial Information Science, but my passion for programming led me to teach myself Python in 2009, a skill I have used ever since.

Outside of my main work, I'm a "weekend warrior" who enjoys mountain biking, camping with family, and playing padel. I also love reading and fixing things around the house.

It's a pleasure to meet you. Please feel free to contact me directly to discuss any of the projects you see here in greater detail.
""", unsafe_allow_html=True)

# --- GANTT ---
st.subheader("Employment History")
gantt = employment_history()
st.plotly_chart(gantt, use_container_width=True)


# --- INTERACTIVE MAP ---
st.subheader("Places I have Studied and Worked")
locations_df = pd.DataFrame({
    'lat': [37.8916, 37.3891, 51.9893, 48.2082, 47.8095, 32.7157],
    'lon': [-4.7845, -5.9845, 5.6663, 16.3738, 13.0550, -117.1611],
    'city': ['Cordoba, Spain', 'Sevilla, Spain', 'Wageningen, Netherlands', 'Vienna, Austria', 'Salzburg, Austria', 'San Diego, California'],
    'company': ['University of Cordoba','TÉCNICA Y PROYECTOS SA<br>TELVENT INTERACTIVA<br>EPTISA', 'Wageningen University', 'Seibersdorf Research Centre', 'Nothing yet here', 'EDF Power Solutions']
})

fig = go.Figure(go.Scattermapbox(
    lat=locations_df['lat'],
    lon=locations_df['lon'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=20,
        color='red',
        symbol='circle',
    ),
    hovertext=locations_df['city'] + '<br>' + locations_df['company'],
    hoverinfo='text'
))

fig.update_layout(
    mapbox_style="open-street-map",
    hovermode='closest',
    margin={"r":0,"t":0,"l":0,"b":0},
    mapbox=dict(
        bearing=0,
        center=dict(
            lat=40.0,
            lon=-50.0
        ),
        pitch=0,
        zoom=2
    )
)

st.plotly_chart(fig, use_container_width=True)

# --- Additional Info Columns ---
st.divider()
c1, c2 = st.columns([2, 3])

# Data to be displayed. Please replace with your own information.
me1 = {
    'Pronouns': ['he', 'him', 'his'],
    'Locations': ['San Diego, CA', 'Sevilla, Spain', 'Vienna, Austria', 'Wageningen, The Netherlands', 'Cordoba, Spain'],
    'Education': ['MSc in Geo Information Science', 'Master in Agronomic Engineering'],
    'Contact': [
        'casti_spain@hotmail.com',
        r'+1 858 248 9119']
}
me2 = {
    'Mountain Biking': [
        '10 plus years in San Diego',
        'Currently Riding:',
        ['Pivot Shuttle', 'Pivot Mach 5.5'],
    ],
    'Padel': [
        '3 plus years in San Diego and Salzburg',
    ],
    'Favorite Reading': [
        'Las Hermanas Coloradas by Francisco García Pavón',
        'La Sombra del Viento by Carlos Ruiz Zafón'
        'A Study in Scarlet and The Hound of the Baskervilles by Sir Arthur Conan Doyle',
        'Musashi by Eiji Yoshikawa',
        'Twenty Thousand Leagues Under the Seas by Jules Verne'

    ],
    'Environment': [
        'Renewable energy',
        'Recycling',
        '80% Zero Waste'
    ]
}

with c1:
    st.write('## Logistics')
    st.write(me1)

with c2:
    st.write('## Other Stuff')
    st.write(me2)
