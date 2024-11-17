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
    coordinates = st.text_input("Coordinates", placeholder="e.g., (10, 20)")
    length = st.number_input("Length", min_value=0.0, step=0.1, format="%.2f")
    submitted = st.form_submit_button("Add Pipe")

    if submitted:
        if pipe_name and coordinates:
            if pipe_name not in pipe_data:
                pipe_data[pipe_name] = {
                    "coordinates": coordinates,
                    "length": length
                }
                save_data(pipe_data)
                st.success(f"Pipe '{pipe_name}' added successfully!")
            else:
                st.warning("Pipe name already exists. Please use a unique name.")
        else:
            st.error("Pipe name and coordinates are required.")

# Display stored pipes
st.header("Stored Pipes")
if pipe_data:
    for name, details in pipe_data.items():
        st.write(f"**Pipe Name:** {name}")
        st.write(f"**Coordinates:** {details['coordinates']}")
        st.write(f"**Length:** {details['length']} meters")
        st.write("---")
else:
    st.info("No pipes stored yet. Add a new pipe to get started.")

# Option to clear all data
if st.button("Clear All Data"):
    pipe_data = {}
    save_data(pipe_data)
    st.warning("All data cleared!")