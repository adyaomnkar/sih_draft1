import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

df=pd.read_csv('d1.csv')
df1=pd.read_csv('d2.csv')

# d1=pd.DataFrame(df1)
# se=d1[['Regions','Dates','Usage']]

st.header("⚡️Automated Energy Supply System: ")
st.subheader("Optimizing Energy Distribution with AI🤖")
st.divider()
p="""
Hydro and wind energy are crucial for India to diversify its energy sources, reduce reliance on fossil fuels, and meet its growing power demands sustainably. As power consumption rises with economic growth, these renewable sources help ensure energy security while mitigating environmental impact.

"""
st.write(p)
st.sidebar.write("Welcome to WatchWatt, your go-to platform for tracking and analyzing energy consumption trends across India. Dive into real-time insights and discover how power usage evolves region by region.")
d=pd.DataFrame(df)
a,c=st.columns(2)
# st.dataframe(df1)

st.map(df1)


# Initialize connection to SQLite database
conn = sqlite3.connect('scam_reports.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS scam_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_address TEXT,
    state TEXT,
    photo BLOB
)
''')
conn.commit()

# Streamlit app title
st.title("Scam Report Map: Report Suspected Electricity Theft")

# Streamlit form
with st.form("scam_report_form"):
    st.write("Please fill out the details below. Your identity will remain confidential.")

    # Full address input
    full_address = st.text_area("Enter the Full Address of the Suspected Theft:")

    # Dropdown for Indian states
    states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
              "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
              "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
              "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
              "Uttarakhand", "West Bengal"]
    state = st.selectbox("Select the State:", states)

    # File uploader for photo
    photo = st.file_uploader("Upload a Photo of the Incident (optional):", type=["jpg", "jpeg", "png"])

    # Submit button
    submitted = st.form_submit_button("Submit Report")

    if submitted:
        # Handle photo upload as binary data
        photo_data = None
        if photo:
            photo_data = photo.read()

        # Store the data in SQLite database
        c.execute("INSERT INTO scam_reports (full_address, state, photo) VALUES (?, ?, ?)",
                  (full_address, state, photo_data))
        conn.commit()

        st.success("Your report has been submitted successfully. Thank you for helping us fight electricity theft!")

# Optionally, show the reports for verification (this can be removed in production)
if st.checkbox("Show Reports (for debugging)"):
    c.execute("SELECT * FROM scam_reports")
    reports = c.fetchall()
    # for report in reports:
    #     st.write(f"ID: {report[0]}, Address: {report[1]}, State: {report[2]}")
    #     if report[3]:
    #         st.image(report[3])

# Close the database connection when done
conn.close()


























# st.line_chart(se)

# st.write(se)

# Allow the user to select columns for the charts
# columns = st.multiselect("Select columns for the charts:", df.columns.tolist())

# Check if the user has selected any columns
# if columns:
#     # Plotting a Line Chart
#     st.write("Line Chart:")
#     st.line_chart(df[columns])

#     # Plotting an Area Chart
#     st.write("Area Chart:")
#     st.area_chart(df[columns])

#     # Plotting a Bar Chart
#     st.write("Bar Chart:")
#     st.bar_chart(df[columns])
# else:
#     st.write("Please select at least one column to display the charts.")

