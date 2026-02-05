"""
------------------------------------------------------------
|   Project Title : BMI Calculator (Streamlit App)         |
|   Author        : SHIVANSH VISHWAKARMA                    |
|   Language      : Python                                 |
|   Framework     : Streamlit                              |
|   Date Created  : February 2026                          |
|   Version       : 1.0                                    |
|----------------------------------------------------------|
|   Description:                                          |
|   This project is a web-based Body Mass Index (BMI)      |
|   Calculator built using Python and Streamlit. It       |
|   allows users to calculate BMI by entering weight and  |
|   height in different units. The app automatically       |
|   converts units, calculates BMI, and displays health   |
|   status with motivational messages and animations.     |
|                                                          |
|   Features:                                             |
|   ➤ Multiple weight units (Kg, Gram, Pound)             |
|   ➤ Multiple height units (cm, meter, feet)             |
|   ➤ Automatic unit conversion                           |
|   ➤ BMI classification with color-coded results         |
|   ➤ Custom CSS styling                                  |
|   ➤ Images and animations for better UI                 |
|   ➤ Beginner-friendly and well-commented code           |
------------------------------------------------------------
"""

import streamlit as st
from math import *

# ===========================================================
# FUNCTION : BMI()
# PURPOSE  : Main function to run the BMI Calculator app
# ===========================================================
def BMI():

    # -------------------------------------------------------
    # Page configuration (title and icon)
    # -------------------------------------------------------
    st.set_page_config(
        page_title="BMI",
        page_icon="https://cdn-icons-png.flaticon.com/512/10476/10476452.png"
    )

    # -------------------------------------------------------
    # Top image section using two columns
    # -------------------------------------------------------
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.image(
            "https://img.freepik.com/free-photo/person-being-scanned-by-digital-health-app_23-2151891771.jpg",
            width=200
        )

    with col2:
        st.image(
            "https://img.freepik.com/free-photo/person-being-scanned-by-digital-health-app_23-2151891767.jpg",
            width=200
        )

    try:
        # ---------------------------------------------------
        # Custom CSS for background and button styling
        # ---------------------------------------------------
        st.markdown(
        """<style>
        .stApp{
            background-color:#000000;
            color:white;
        }
        .stButton>button{
            background-color:#66E538;
            color:white;
            border:2px solid red;
            border-radius:8px;
            padding:8px 20px;
        }
        </style>""",
        unsafe_allow_html=True
        )

        # ---------------------------------------------------
        # Custom CSS for selectbox styling
        # ---------------------------------------------------
        st.markdown(
        """<style>
        div[data-baseweb="select"] > div {
            background-color: #8A009E;
            color: white;
            border-radius: 8px;
            border: 1px solid #555;
        }
        div[data-baseweb="select"] span {
            color: white;
            font-weight: 500;
        }
        div[data-baseweb="select"] svg {
            fill: white;
        }
        ul[data-baseweb="menu"] {
            background-color: #2b2b2b;
        }
        ul[data-baseweb="menu"] li {
            color: white;
        }
        ul[data-baseweb="menu"] li:hover {
            background-color: #444;
        }
        </style>""",
        unsafe_allow_html=True
        )

        # ---------------------------------------------------
        # App title
        # ---------------------------------------------------
        st.title("| ---- BODY MASS INDEX ---- |")
        st.write("")

        # ---------------------------------------------------
        # Weight input section
        # ---------------------------------------------------
        st.write("Enter The Unit of Weight")
        w_unit = st.selectbox("", ["Kilogram", "Gram", "Pound"])

        st.write("")
        st.write("Enter Your Weight")
        weight = st.number_input(" ", min_value=0)

        # Weight conversion to kilograms
        if w_unit == "Kilogram":
            w = weight
        elif w_unit == "Gram":
            w = weight / 1000
        else:
            w = weight * 0.45359237

        # ---------------------------------------------------
        # Height input section
        # ---------------------------------------------------
        st.write("Enter the Height Unit")
        h_unit = st.selectbox("", ["Centimeter", "Meter", "Feet"])

        st.write("")
        st.write("Enter Your Height")
        height = st.number_input("", min_value=0)

        # Height conversion to meters
        if h_unit == "Centimeter":
            h = height / 100
        elif h_unit == "Feet":
            h = height * 0.3048
        else:
            h = height

        # ---------------------------------------------------
        # BMI calculation and classification
        # ---------------------------------------------------
        if st.button("Check BMI"):
            bmi = w / pow(h, 2)

            if bmi <= 18.5:
                st.markdown(
                f"""<div style="background-color:#CDD400;
                padding:12px; border-radius:8px; color:white;">
                UnderWeight! Your BMI is {bmi:.2f}
                </div>""",
                unsafe_allow_html=True
                )
                st.write("Fuel your body. Strength comes after nourishment.")

            elif bmi <= 24.9:
                st.markdown(
                f"""<div style="background-color:#19D400;
                padding:12px; border-radius:8px; color:white;">
                Healthy Body! Your BMI is {bmi:.2f}
                </div>""",
                unsafe_allow_html=True
                )
                st.write("Strong habits build strong bodies.")
                st.balloons()

            elif bmi <= 29.9:
                st.markdown(
                f"""<div style="background-color:#D9730F;
                padding:12px; border-radius:8px; color:white;">
                OverWeight! Your BMI is {bmi:.2f}
                </div>""",
                unsafe_allow_html=True
                )
                st.write("Progress begins with one step.")

            elif bmi <= 34.9:
                st.markdown(
                f"""<div style="background-color:#E60E0E;
                padding:12px; border-radius:8px; color:white;">
                Obese Class 1! Your BMI is {bmi:.2f}
                </div>""",
                unsafe_allow_html=True
                )
                st.write("Consistency beats excuses.")

            elif bmi < 39.9:
                st.markdown(
                f"""<div style="background-color:#E60E0E;
                padding:12px; border-radius:8px; color:white;">
                Obese Class 2! Your BMI is {bmi:.2f}
                </div>""",
                unsafe_allow_html=True
                )
                st.write("Start small. Stay steady.")

            else:
                st.markdown(
                f"""<div style="background-color:#E60E0E;
                padding:12px; border-radius:8px; color:white;">
                Obese Class 3! Your BMI is {bmi:.2f}
                </div>""",
                unsafe_allow_html=True
                )
                st.write("Health is built one decision at a time.")

    # -------------------------------------------------------
    # Error handling for invalid input
    # -------------------------------------------------------
    except:
        st.write("Enter a valid number!")

    st.write("")

    # -------------------------------------------------------
    # Bottom image section
    # -------------------------------------------------------
    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.image(
            "https://img.freepik.com/free-photo/person-being-scanned-by-digital-health-app_23-2151891762.jpg",
            width=300
        )

    with col4:
        st.image(
            "https://img.freepik.com/free-photo/person-being-scanned-by-digital-health-app_23-2151891765.jpg",
            width=300
        )

# ===========================================================
# Program execution starts here
# ===========================================================
if __name__=="__main__":
    BMI()
