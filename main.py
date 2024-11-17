import streamlit as st
import pipe
import wikipedia1

# Create a sidebar for navigation
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to", ["Map", "Wikipedia"])

# Navigate to the selected app
if choice == "Map":
    pipe.pipe_main()  # Call the app1 function
elif choice == "Wikipedia":
    wikipedia1.app()  # Call the app2 function
