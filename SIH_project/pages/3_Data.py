import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Initialize SQLite database
conn = sqlite3.connect('energy_data.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS energy_data (
        region TEXT,
        wind_energy REAL,
        hydro_energy REAL,
        extra_energy_needed REAL,
        net_energy REAL
    )
''')
conn.commit()

# Streamlit Application
st.title("Energy Data Collection for Indian Regions")

# Energy Data Collection Form
with st.form("energy_form"):
    region = st.selectbox("Select the region", ["North", "South", "East", "West", "North East", "South West"])
    wind_energy = st.number_input("Enter Wind Energy (in MW)", min_value=0.0)
    hydro_energy = st.number_input("Enter Hydro Energy (in MW)", min_value=0.0)
    extra_energy_needed = st.number_input("Enter Extra Energy Needed (in MW)", min_value=0.0)
    net_energy = st.number_input("Enter Net Energy (in MW)", min_value=0.0)

    submit_button = st.form_submit_button("Submit")

if submit_button:
    # Insert data into the database
    c.execute("INSERT INTO energy_data (region, wind_energy, hydro_energy, extra_energy_needed, net_energy) VALUES (?, ?, ?, ?, ?)",
              (region, wind_energy, hydro_energy, extra_energy_needed, net_energy))
    conn.commit()
    st.success("Data submitted successfully!")

# Data Visualization Section
st.header("Energy Data Visualization")

# Load data from the database
df = pd.read_sql_query("SELECT * FROM energy_data", conn)

# if not df.empty:
#     st.subheader("Bar Plot: Energy Distribution by Region")
#     fig, ax = plt.subplots()
#     sns.barplot(x='region', y='net_energy', data=df, ax=ax)
#     st.pyplot(fig)

#     st.subheader("Scatter Plot: Wind Energy vs Hydro Energy")
#     fig, ax = plt.subplots()
#     sns.scatterplot(x='wind_energy', y='hydro_energy', hue='region', data=df, ax=ax)
#     st.pyplot(fig)

#     st.subheader("Line Plot: Extra Energy Needed by Region")
#     fig, ax = plt.subplots()
#     sns.lineplot(x='region', y='extra_energy_needed', data=df, ax=ax)
#     st.pyplot(fig)
# else:
#     st.write("No data available yet.")

# # Close the database connection
conn.close()
