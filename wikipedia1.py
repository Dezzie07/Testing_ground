import streamlit as st
import json
import os

# File to store data persistently
DATA_FILE = "pipe_data.json"

# Function to load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Load existing data
pipe_data = load_data()

# Streamlit app interface
st.title("Pipe Storage System")
st.subheader("Store and View Pipe Details")

# Add a new pipe
st.header("Add New Pipe")
with st.form("add_pipe_form"):
    pipe_name = st.text_input("Pipe Name", placeholder="Enter unique pipe name")
    
    # Allow user to input multiple coordinates
    coordinates_input = st.text_area(
        "Coordinates (comma-separated list of x,y pairs)",
        placeholder="e.g., (10, 20), (30, 40), (50, 60)"
    )
    
    length = st.number_input("Length", min_value=0.0, step=0.1, format="%.2f")
    submitted = st.form_submit_button("Add Pipe")

    if submitted:
        if pipe_name and coordinates_input:
            # Convert the input string to a list of tuples (x, y)
            try:
                coordinates = [
                    tuple(map(int, coord.strip("()").split(","))) 
                    for coord in coordinates_input.split(",")
                ]
                
                if pipe_name not in pipe_data:
                    pipe_data[pipe_name] = {
                        "coordinates": coordinates,
                        "length": length
                    }
                    save_data(pipe_data)
                    st.success(f"Pipe '{pipe_name}' added successfully!")
                else:
                    st.warning("Pipe name already exists. Please use a unique name.")
            except ValueError:
                st.error("Invalid coordinate format. Ensure coordinates are in the form (x, y).")
        else:
            st.error("Pipe name and coordinates are required.")

# Display stored pipes
st.header("Stored Pipes")
if pipe_data:
    # Convert dictionary to list of dictionaries for tabular display
    table_data = [
        {
            "Pipe Name": name, 
            "Coordinates": ', '.join([f"({x}, {y})" for x, y in details["coordinates"]]), 
            "Length (meters)": details["length"]
        }
        for name, details in pipe_data.items()
    ]
    st.subheader("Pipe Data (Table View)")
    st.table(table_data)  # Static table
else:
    st.info("No pipes stored yet. Add a new pipe to get started.")

# Option to clear all data
if st.button("Clear All Data"):
    pipe_data = {}
    save_data(pipe_data)
    st.warning("All data cleared!")
