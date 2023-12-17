import pandas as pd
import streamlit as st

# Import Data
day_df = pd.read_csv("day.csv")

datetime_columns = ["dteday"]

for column in datetime_columns :
    day_df[column] = pd.to_datetime(day_df[column])

# Membuat Filter
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar :
    st.subheader("Dashboard Fanky")


    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df["dteday"] >= str(start_date)) & 
                (day_df["dteday"] <= str(end_date))]

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['season'] = day_df.season.astype('category')
day_df['mnth'] = day_df.mnth.astype('category')
day_df['holiday'] = day_df.holiday.astype('category')
day_df['weekday'] = day_df.weekday.astype('category')
day_df['workingday'] = day_df.workingday.astype('category')
day_df['weathersit'] = day_df.weathersit.astype('category')

day_df.season.replace((1,2,3,4), ('Winter','Spring','Summer','Fall'), inplace=True)
day_df.yr.replace((0,1), (2011,2012), inplace=True)
day_df.mnth.replace((1,2,3,4,5,6,7,8,9,10,11,12),('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'), inplace=True)
day_df.weathersit.replace((1,2,3,4), ('Clear','Misty','Light_RainSnow','Heavy_RainSnow'), inplace=True)
day_df.weekday.replace((0,1,2,3,4,5,6), ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'), inplace=True)
day_df.workingday.replace((0,1), ('No', 'Yes'), inplace=True)

# Visualisasi

st.header("Final Project Analisa Data dengan Python 😁")

st.subheader("Banyak Pengendara Sepeda per Tahun")
st.bar_chart(data=day_df, x="yr", y="cnt", color="#02def7")
st.caption("""Banyak sepeda yang disewa selama tahun `2011` lebih dari 3000 sepeda.
Dan banyak sepeda yang disewa pada tahun `2012` lebih dari 5000 sepeda.""")

st.subheader("Banyak Pengendara Sepeda per Musim")
st.bar_chart(data=day_df, x="season", y="cnt", color="#f7b202")
st.caption("""Pada `2011` pengendara sepeda banyak yang memakai sepeda pada musim panas, begitu juga dengan `2012` yang memiliki penyewa sebanyak terbanyak pada musim panas. 
           Dengan total penyewa sebanyak 4000 lebih pada tahun `2011` dan 6000 lebih pada tahun `2012`.""")