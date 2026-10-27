import streamlit as st

st.set_page_config(
page_title="BatukBicara AI",
page_icon="🩺",
layout="centered"
)

st.title("🩺 BatukBicara AI")

st.subheader("Kenali Gejala Batukmu Sejak Dini")

st.write(
"BatukBicara AI adalah prototipe skrining awal "
"yang membantu pengguna mencatat gejala batuk "
"dan karakteristik suara batuk."
)

st.info(
"Aplikasi ini bukan alat diagnosis medis. "
"Hasilnya tidak dapat memastikan penyakit tertentu."
)

st.divider()

st.header("📝 Kuesioner Gejala")

lama_batuk = st.selectbox(
"Sudah berapa lama kamu mengalami batuk?",
[
"Kurang dari 3 hari",
"3–7 hari",
"8–13 hari",
"14 hari atau lebih"
]
)

dahak = st.radio(
"Apakah batuk disertai dahak?",
["Ya", "Tidak", "Tidak yakin"]
)

demam = st.radio(
"Apakah kamu mengalami demam?",
["Ya", "Tidak", "Tidak yakin"]
)

sesak = st.radio(
"Apakah kamu mengalami sesak napas?",
["Ya", "Tidak", "Tidak yakin"]
)

st.header("🎙️ Rekam Suara Batuk")

audio = st.audio_input("Rekam suara batukmu")

if audio:
st.audio(audio)

st.success(
    "Rekaman berhasil diterima. "
    "Analisis AI belum tersedia pada versi awal ini."
)

if st.button("Lihat Ringkasan Skrining"):
st.subheader("📋 Ringkasan Jawaban")

st.write("Durasi batuk:", lama_batuk)
st.write("Batuk berdahak:", dahak)
st.write("Demam:", demam)
st.write("Sesak napas:", sesak)

if sesak == "Ya":
    st.error(
        "Jika sesak berat atau kesulitan bernapas, "
        "segera cari pertolongan medis."
    )

if lama_batuk == "14 hari atau lebih":
    st.warning(
        "Batuk selama 14 hari atau lebih perlu "
        "diperiksakan kepada tenaga kesehatan."
    )

st.info(
    "Ringkasan ini bukan diagnosis. "
    "Konsultasikan keluhan kepada tenaga kesehatan."
)

st.divider()

st.caption(
"BatukBicara AI | Prototipe edukasi kesehatan"
)
