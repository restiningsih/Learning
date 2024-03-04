import streamlit as st
import pandas as pd
import numpy as np
import calendar

def load_data(sepeda):
    sewa_sepeda = pd.read_csv(r"C:\Users\ASUS\Downloads\Bike-sharing-dataset\sewa_sepeda.csv")
    return sewa_sepeda

def filter_by_month(sewa_sepeda, months):
    bulan = list(calendar.month_name).index(months)
    filter_data = sewa_sepeda[sewa_sepeda['mnth_x'].dt.month == bulan]
    return filter_data

def main():
    st.title('Data Bisnis Sewa Sepeda')

    #menambahkan sidebar
    st.sidebar.header('Kalender :D')
    bulan1 = st.sidebar.selectbox("Pilih bulan", list(calendar.month_name)[1:])
    tahun = 2011
    tanggalan = list(calendar.month_name).index(bulan1)
    kalender1 = calendar.monthcalendar(tahun, tanggalan)
    st.sidebar.write("Kalender %s" %bulan1)
    st.sidebar.write("Minggu sen sel rab kam jum sab")
    for week in kalender1:
        st.sidebar.write(week)

    sepeda = (r"C:\Users\ASUS\Downloads\Bike-sharing-dataset\sewa_sepeda.csv")
    sewa_sepeda = load_data(sepeda)
    sewa_sepeda['mnth_x'] = pd.to_datetime(sewa_sepeda['mnth_x'])

    filter_data = filter_by_month(sewa_sepeda, bulan1)

    st.write('Data Awal: ')
    st.write(sewa_sepeda)
    
    st.write('Statistik Deskriptif:')
    st.write(filter_data.describe())

    # Bar chart
    st.write('Bar Chart:')
    grafik1 = filter_data[['season_x', 'cnt_y']].groupby('season_x').sum()
    st.bar_chart(grafik1)

    # Line chart
    st.write('Line Chart:')
    jumlah_sewa = filter_data.groupby('mnth_x')['cnt_y'].sum() 
    st.line_chart(jumlah_sewa)
    
if __name__ == "__main__":
    main()