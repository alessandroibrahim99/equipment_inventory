# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:23:18 2021

@author: alessandro.ibrahim
"""

import streamlit as st
import pandas as pd
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
fig = go.Figure()

#csv_file_state = 'usa_covid_data_states.csv'
csv_file_state = 'Liste_Eqpt_Sites.csv'


@st.cache
def load_data(nrows):
    data = pd.read_csv(csv_file_state)
    return data

  


dfstate = load_data(100000) 





#Dashboard Sidebar with State list
st.sidebar.title("Equipment Inventory")


State_list = st.sidebar.selectbox(
     'Choose your Job (11.0338.ZT)',
       dfstate.Job[:80000])

State_list1 = st.sidebar.selectbox(
     'Class Name (11.0338.ZT)',
       dfstate.EquipClassName[:80000])

# Select a State from sidebar to update this chart
st.markdown("""Inventory Equipment - Detailed Version
 	""")

newdf = dfstate[dfstate['Job'] == State_list]
#newdf1 = dfstate[dfstate['EquipClassName'] == State_list1]
#rows = df[newdf & newdf1]


df = newdf

def get_table():
    datatable = df[['Job', 'EquipClassName', 'Equip. Code',	'Equip. Name', 'Equip. Desc', 'Start Date', 'Brand', 'Model', 'Year', 'Serial #','lat','lon']].sort_values(by=['Job'], ascending=False)
    
    return datatable

newdf = get_table()

st.dataframe(newdf)




# Select a State from sidebar to update this chart
st.markdown("""Inventory Equipment - Short Version
 	""")

newdf = dfstate[dfstate['Job'] == State_list]
df = newdf

def get_table():
    datatable = df[['Job', 'EquipClassName', 'Equip. Name', 'Equip. Desc', 'Start Date','lat','lon']].sort_values(by=['Job'], ascending=False)
    
    return datatable

newdf = get_table()

st.dataframe(newdf)
print(newdf)

#st.map(newdf)
