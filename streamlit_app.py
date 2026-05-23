import streamlit as st
import time

# Judul aplikasi
st.title("🎈 Impian Tuan Agung")

st.write(
    "Animasi bola bergerak menggunakan Streamlit"
)

# Judul animasi
st.title("⚽ Bola Bergerak di Streamlit")

# Tempat animasi
placeholder = st.empty()

# Posisi awal bola
posisi = 0

# Animasi bergerak
for i in range(60):

    posisi += 10

    placeholder.markdown(f"""
    <div style="
        position: relative;
        width: 100%;
        height: 250px;
        background: linear-gradient(to bottom, skyblue, white);
        overflow: hidden;
        border-radius: 20px;
        border: 3px solid black;
    ">

        <!-- Rumput -->
        <div style="
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 60px;
            background: green;
        "></div>

        <!-- Bola -->
        <div style="
            position: absolute;
            left: {posisi}px;
            bottom: 80px;
            width: 70px;
            height: 70px;
            background: white;
            border-radius: 50%;
            border: 5px solid black;
            box-shadow: 0px 0px 10px gray;
        ">

            <!-- Corak bola -->
            <div style="
                position:absolute;
                width:20px;
                height:20px;
                background:black;
                border-radius:50%;
                top:10px;
                left:25px;
            "></div>

            <div style="
                position:absolute;
                width:15px;
                height:15px;
                background:black;
                border-radius:50%;
                top:35px;
                left:10px;
            "></div>

            <div style="
                position:absolute;
                width:15px;
                height:15px;
                background:black;
                border-radius:50%;
                top:35px;
                right:10px;
            "></div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    time.sleep(0.05)

# Pesan selesai
st.success("⚽ Bola berhasil bergerak!")







import streamlit as st

st.write("Hello, *World!* :sunglasses:")
