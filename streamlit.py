import pandas
import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text(' 🥣 Omega & Blueberry Oatmeal')

streamlit.text(' 🥗 Kale, Spinach & Rocket Smooth')

streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')

streamlit.text('  🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.dataframe(my_fruit_list)


streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
