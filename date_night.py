# import libraries
from operator import contains
import numpy as np
import pandas as pd
import seaborn as sns
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import re as re
import collections as co
from adjustText import adjust_text
from PIL import Image
import random 

# import streamlit (website browser) and st_aggrid (aesthetic table)
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

# create lists
staying_in = ['Make Dinner Together', 'Get Takeout or Delivery', 'Valorant', 'Play Board Games', 'Play Card Games', 'Do a Puzzle', 'Paint', 'Update a Travel List', 'Update a Bucket List', 'Create a Photo Book']
going_out = ['Eat Out', 'Watch a movie', 'Picnic', 'Somewhere Tiktok famous', 'Instagram Aesthetic Photos', 'Play Laser Tag', 'Visit a Museum', 'Mall', 'Bowling', 'Comedy Show', 'Roller Skating', 'Ice Skating', 'See a Psychic', 'Be a Tourist', 'Amusement Park', 'Take a cooking or baking class', 'Go on a hike', 'Visit an animal shelter', 'Recreate your first date', 'Go on an alphabet date', 'Volunteer', 'Run or walk a charity 5k', 'Archery', 'Axe Throwing', 'Musical']
restaurant_to_try = ['Daiki Sushi', 'Gao Viet Kitchen', 'Avenida', 'Hummus Mediterranean Kitchen', 'Foreigner', 'Tomatina']

# title
st.markdown("<h1 style = 'text-align: center;'>Date Night</h1>", unsafe_allow_html=True)

# add columns
col1, col2 = st.columns(2)
with col1:

    # ask what to do buttons 
    st.markdown("<h2 style = 'text-align: left;'>Want to...?</h2>", unsafe_allow_html=True)
    stay_in = st.button("Stay In")
    if stay_in:
        st.write(random.choice(staying_in))

    go_out = st.button("Go Out")
    if go_out:
        st.write(random.choice(going_out))

with col2:
    st.markdown("<h2 style = 'text-align: left;'>Going Out</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style = 'text-align: left;'>Restuarants to Try</h3>", unsafe_allow_html=True)
    random_restaurant = st.button("Random Restaurant")
    if random_restaurant:
        st.write(random.choice(restaurant_to_try))

# cute pic of us
image = Image.open('ok_buddy.jpg')

st.image(image, caption='Tis still a dream')
