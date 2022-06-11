#import streamlit
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')

streamlit.text('🥗 Kale,Spinach & Rocket smoothie')

streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response 
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/WATERMELON")
streamlit.text(fruityvice_response)

#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit advice!')
fruity_choice = streamlit.text_input('What Fruit would you like informatiopn about?', 'kiwi')
streamlit.write('The user entered', fruity_choice)


#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruity_choice)



#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)

# don't run anything past here while we troubleshoot
streamlit.stop()

#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("select * from fruit_load_list")

my_data_rows = my_cur.fetchall()

streamlit.header("The fruit load list contains:")

streamlit.dataframe (my_data_rows)

