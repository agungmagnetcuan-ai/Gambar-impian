import streamlit as st

st.title("🎈 impian tuan agung")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)



    

# Konfigurasi halaman
st.set_page_config(page_title="Pemandangan Alam", page_icon="🌄")

# Judul aplikasi
st.title("🌄 Pemandangan Alam dengan Streamlit")
st.write("Contoh gambar pemandangan sederhana menggunakan Python + Streamlit")

# Langit
st.markdown("""
<div style="
    position: relative;
    width: 100%;
    height: 500px;
    background: linear-gradient(to bottom, #87CEEB, #E0F6FF);
    overflow: hidden;
    border-radius: 20px;
">

    <!-- Matahari -->
    <div style="
        position: absolute;
        top: 40px;
        right: 80px;
        width: 100px;
        height: 100px;
        background: yellow;
        border-radius: 50%;
        box-shadow: 0 0 40px yellow;
    "></div>

    <!-- Awan -->
    <div style="
        position: absolute;
        top: 60px;
        left: 100px;
        width: 120px;
        height: 60px;
        background: white;
        border-radius: 50px;
    "></div>

    <div style="
        position: absolute;
        top: 80px;
        left: 160px;
        width: 100px;
        height: 50px;
        background: white;
        border-radius: 50px;
    "></div>

    <!-- Gunung 1 -->
    <div style="
        position: absolute;
        bottom: 120px;
        left: 50px;
        width: 0;
        height: 0;
        border-left: 200px solid transparent;
        border-right: 200px solid transparent;
        border-bottom: 300px solid green;
    "></div>

    <!-- Gunung 2 -->
    <div style="
        position: absolute;
        bottom: 120px;
        right: 50px;
        width: 0;
        height: 0;
        border-left: 250px solid transparent;
        border-right: 250px solid transparent;
        border-bottom: 350px solid darkgreen;
    "></div>

    <!-- Rumput -->
    <div style="
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 120px;
        background: limegreen;
    "></div>

    <!-- Jalan -->
    <div style="
        position: absolute;
        bottom: 0;
        left: 40%;
        width: 200px;
        height: 120px;
        background: gray;
        clip-path: polygon(40% 0%, 60% 0%, 100% 100%, 0% 100%);
    "></div>

</div>
""", unsafe_allow_html=True)

# Pesan tambahan
st.success("Pemandangan berhasil ditampilkan!")
