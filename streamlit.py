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
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])


streamlit.dataframe(my_fruit_list)

