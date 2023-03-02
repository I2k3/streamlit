import streamlit as st
import pandas as pd

st.title("Search names")
st.write("Names")
DATA_URL="https://firebasestorage.googleapis.com/v0/b/heroes-proyect.appspot.com/o/datasets%2Fitzelrios%2Fdataset.csv?alt=media&token=f22f85f3-d682-4eba-96e8-a7aa3f051e63"


@st.cache
def load_data_byname(name):
    data= pd.read_csv(DATA_URL)
    filtered_data_byname= data[data["name"].str.contains(name)]

    return filtered_data_byname

myname = st.text_input("nombre :")
if (myname):
    filter_byname=load_data_byname(myname)
    count_row=filter_byname.shape[0]
    st.write(f"Total names: {count_row}")

    st.dataframe(filter_byname)
