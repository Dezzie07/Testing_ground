import streamlit as st
import json
import os

# File to store data persistently
DATA_FILE = "pipe_data.json"

# Function to load data
def load_data():
    """Load pipe data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save data
def save_data(data):
    """Save pipe data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a new pipe
def add_new_pipe(pipe_data):
    """Interface for adding a new pipe."""
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

# Function to display stored pipes
def display_stored_pipes(pipe_data):
    """Interface for displaying stored pipes."""
    st.header("Stored Pipes")
    if pipe_data:
        table_data = [
            {"Pipe Name": name, "Coordinates": details["coordinates"], "Length (meters)": details["length"]}
            for name, details in pipe_data.items()
        ]
        st.subheader("Pipe Data (Table View)")
        st.table(table_data)  # Static table
    else:
        st.info("No pipes stored yet. Add a new pipe to get started.")

# Function to clear all pipe data
def clear_all_data(pipe_data):
    """Interface to clear all stored pipe data."""
    if st.button("Clear All Data"):
        pipe_data.clear()
        save_data(pipe_data)
        st.warning("All data cleared!")

# Main function to organize the Streamlit app
def main():
    """Main function to run the Pipe Storage System app."""
    pipe_data = load_data()

    st.title("Pipe Storage System")
    st.subheader("Store and View Pipe Details")

    # Call individual functionalities
    add_new_pipe(pipe_data)
    display_stored_pipes(pipe_data)
    clear_all_data(pipe_data)

# Run the app
if __name__ == "__main__":
    main()
