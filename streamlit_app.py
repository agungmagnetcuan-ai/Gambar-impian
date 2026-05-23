import streamlit as st
import time



st.title("🎈 Impian Tuan Agung")

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)



# Judul aplikasi
st.title("⚽ Bola Bergerak di Streamlit")

# Membuat area animasi
placeholder = st.empty()

# Posisi awal bola
posisi = 0

# Animasi bola bergerak
for i in range(60):
    posisi += 10

    placeholder.markdown(f"""
    <div style="
        position: relative;
        width: 100%;
        height: 200px;
        background-color: lightblue;
        overflow: hidden;
        border-radius: 15px;
    ">

        <!-- Rumput -->
        <div style="
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50px;
            background-color: green;
        "></div>

        <!-- Bola -->
        <div style="
            position: absolute;
            left: {posisi}px;
            bottom: 60px;
            width: 60px;
            height: 60px;
            background-color: white;
            border-radius: 50%;
            border: 4px solid black;
        "></div>

    </div>
    """, unsafe_allow_html=True)

    time.sleep(0.05)

# Pesan selesai
st.success("Bola berhasil bergerak!")
