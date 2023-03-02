import streamlit as st
import pandas as pd 

st.title('Streamlit - Filter by sex' )

DATA_URL = ('https://firebasestorage.googleapis.com/v0/b/heroes-proyect.appspot.com/o/datasets%2Fitzelrios%2Fdataset.csv?alt=media&token=f22f85f3-d682-4eba-96e8-a7aa3f051e63')


@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data 

@st.cache
def load_data_bysex(sex):
    data = pd.read_csv(DATA_URL)
    filtered_data_bysex = data[data['sex'] == sex ]

    return filtered_data_bysex

data = load_data()
selected_sex = st.selectbox("Select Sex", data ['sex']. unique() )
btnFilterbySex = st.button('Filter by sex')
if (btnFilterbySex):
    filterbysex = load_data_bysex(selected_sex)
    count_row = filterbysex.shape[0]
    st.write(f"Total items : {count_row}")

    st.dataframe(filterbysex)
