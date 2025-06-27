import streamlit as st
import requests
import pandas as pd

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

# Maintain session state for userId and page
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "page" not in st.session_state:
    st.session_state.page = 0

st.title("Dish Display App")

# Input field
user_input = st.text_input("User ID", value=st.session_state.user_id or "")

# Go button resets the page
if st.button("Go"):
    try:
        st.session_state.user_id = int(user_input)
        st.session_state.page = 0  # Reset to first page
    except ValueError:
        st.error("Please enter a valid integer User ID.")

# Only show if user_id is set
if st.session_state.user_id is not None:
    # Fetch dishes
    response = requests.get(
        "http://localhost:8000/dishes",
        params={"userId": st.session_state.user_id, "page": st.session_state.page}
    )
    dishes = response.json().get("dishes", [])

    # Display dishes
    if dishes:
        st.dataframe(pd.DataFrame([{"Dish Name": d} for d in dishes]), hide_index=True)
    # Show page number
    st.markdown(f"**Page:** {st.session_state.page + 1}")
    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        st.button("Previous", disabled=st.session_state.page == 0, on_click=prev_page)
    with col2:
        st.button("Next", disabled=len(dishes) < 5 or st.session_state.page >= 4,  on_click=next_page)
    if not dishes:
        st.info("No dishes found for this user/page.")
