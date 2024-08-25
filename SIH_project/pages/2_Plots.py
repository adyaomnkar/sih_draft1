import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

st.header("📈 Watt Watch")
st.subheader("Visualizing the Shifts in Energy Consumption Patterns Across Indian Regions")
st.divider()

conn = sqlite3.connect('energy_data.db')
c = conn.cursor()

# Setting up the Tabs
tab1, tab2 = st.tabs(["Real Time", "Available"])

## Display from database
with tab1:
    df = pd.read_sql_query("SELECT * FROM energy_data", conn)
    d = pd.DataFrame(df)
    x, space, y = st.columns((1, 0.4, 1))
    a, b, c = st.columns(3)
    x.line_chart(d)
    y.bar_chart(d)
    x.area_chart(d)
    df = pd.read_csv('d1.csv')
    df1 = pd.read_csv('d2.csv')
    y.table(df1.iloc[0:10])
    d = pd.DataFrame(df)
    a, b, c = st.columns(3)
    st.divider()

    # Allow the user to select columns for the charts
    columns = st.multiselect("Select columns for the charts:", df.columns.tolist())

    # Check if the user has selected any columns
    if columns:
        # Plotting a Line Chart
        x.write("Trend Variations:")
        x.line_chart(df[columns])

        # Plotting an Area Chart
        st.write("Energy Variation Chart:")
        st.area_chart(df[columns])

        # Plotting a Bar Chart
        st.write("Bar Chart:")
        st.bar_chart(df[columns])
    else:
        st.write("Please select at least one column to display the charts.")

## Display from dataset/dataframe
## Display from dataset/dataframe
with tab2:
    # Load the CSV file
    p="""
    This component of the Watt Watch project enables users to visualize energy consumption patterns across Indian regions in real-time and from available datasets. Users can select specific columns to display in various charts, including line, area, and bar charts. Additionally, users can choose to view energy usage by region or state, providing a more detailed understanding of energy consumption trends
    
    """
    df = pd.read_csv('d2.csv')

    # Display the dataframe
    st.markdown("This component of the Watt Watch project enables users to visualize energy consumption patterns across Indian regions in real-time and from available datasets. Users can select specific columns to display in various charts, including line, area, and bar charts. Additionally, users can choose to view energy usage by region or state, providing a more detailed understanding of energy consumption trends")
    st.write("Data from Real Time:")
    # st.dataframe(df)

    # Allow the user to select columns for the x-axis
    x_axis = st.selectbox("Select the column for the x-axis:", ['Regions', 'States'])

    # Check if the user has selected the x-axis
    if x_axis:
        # Create a new dataframe with the selected column and 'Usage'
        df_selected = df[[x_axis, 'Usage']]

        # Group the dataframe by the selected column and calculate the sum of 'Usage'
        df_grouped = df_selected.groupby(x_axis)['Usage'].sum().reset_index()

        p, spac, q = st.columns(3)
        # Plotting a Line Chart
        p.write(f"{x_axis} vs Usage Line Chart:")
        p.line_chart(df_grouped.set_index(x_axis))

        # Plotting a Bar Chart
        q.write(f"{x_axis} vs Usage Bar Chart:")
        q.bar_chart(df_grouped.set_index(x_axis))
    else:
        st.write("Please select a column for the x-axis to display the charts.")

# Close the database connection
conn.close()