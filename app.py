import streamlit as st
import ProjectML as pm #import kode dari file notebook.py

#Function untuk merekomendasikan tempat wisara
def recommend_destination(city, category, price):
    #menambahkan logika rekomendasi berdasarkan data yang dimiliki
    #misal menggunakan algoritma rekomendasi yang sesuai atau filter data berdasarkan input pengguna
    recommended_destinations = pm.recommend_destination(city, category, price)

    return recommended_destinations

#UI streamlit
def main():
    st.title("Recommendation Tourism Destination")
    city = st.text_input("Masukkan kota tujuan : ")
    category = st.selectbox("Pilih kategori wisata : ", ['Budaya', 'Taman Hiburan', 'Cagar Alam', 'Bahari',
       'Pusat Perbelanjaan', 'Tempat Ibadah'])
    price = st.slider("Pilih budget : ", 0, 900000, (0, 900000), 0)

    if st.button("Recommendation"):
        recommendations = recommend_destination(city, category, price)
        st.success("Berikut rekomendasi tempat wisata untuk Anda : ")
        for recommendation in recommendations:
            st.write(recommendation)
            
if __name__ == "__main__":
    main()
