import streamlit

streamlit.title('MY PARENTS NEW HEALTHY DINNER')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some Fruits:",list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_row)

fruit_choice = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for Adding ', fruit_choice)

my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")
