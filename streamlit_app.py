import streamlit as st

st.title("🎈 impian tuan agung")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


# Judul aplikasi
st.title("🌄 Gambar Pemandangan dengan Streamlit")
st.write("Contoh pemandangan sederhana menggunakan HTML dan CSS di Streamlit")

# Membuat gambar pemandangan
st.markdown("""
<div style="
    width:100%;
    height:500px;
    background:linear-gradient(to top, #87CEEB 60%, #ffffff 100%);
    position:relative;
    overflow:hidden;
">

    <!-- Matahari -->
    <div style="
        width:100px;
        height:100px;
        background:yellow;
        border-radius:50%;
        position:absolute;
        top:40px;
        right:80px;
    "></div>

    <!-- Gunung kiri -->
    <div style="
        width:0;
        height:0;
        border-left:180px solid transparent;
        border-right:180px solid transparent;
        border-bottom:250px solid green;
        position:absolute;
        bottom:120px;
        left:80px;
    "></div>

    <!-- Gunung kanan -->
    <div style="
        width:0;
        height:0;
        border-left:220px solid transparent;
        border-right:220px solid transparent;
        border-bottom:300px solid darkgreen;
        position:absolute;
        bottom:120px;
        right:60px;
    "></div>

    <!-- Rumput -->
    <div style="
        width:100%;
        height:120px;
        background:limegreen;
        position:absolute;
        bottom:0;
    "></div>

    <!-- Jalan -->
    <div style="
        width:200px;
        height:120px;
        background:gray;
        position:absolute;
        bottom:0;
        left:40%;
        clip-path: polygon(40% 0%, 60% 0%, 100% 100%, 0% 100%);
    "></div>

</div>
""", unsafe_allow_html=True)
