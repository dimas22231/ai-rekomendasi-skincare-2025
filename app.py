import streamlit as st

st.title("🌟 AI Rekomendasi Skincare Lengkap")

# INPUT DARI USER
masalah_kulit = st.selectbox("Apa masalah kulitmu?", [
    "Jerawat", "Bruntusan", "Kulit Kusam", "Flek Hitam", "Kulit Kering", "Kulit Berminyak", "Sensitif"
])

tipe_kulit = st.selectbox("Apa tipe kulitmu?", [
    "Kering", "Berminyak", "Sensitif", "Kombinasi", "Normal"
])

budget = st.selectbox("Berapa budget kamu?", [
    "Low (di bawah 50rb)", "Medium (50rb - 150rb)", "High (di atas 150rb)"
])

waktu = st.selectbox("Untuk pemakaian kapan?", [
    "Pagi", "Malam", "Bisa Kapan Saja"
])

# FUNGSI REKOMENDASI
def rekomendasi(masalah, tipe, budget, waktu):
    hasil = {}

    # CONTOH DATA MANUAL (bisa diperbanyak)
    database = [
        {
            "masalah": "Jerawat",
            "tipe": "Berminyak",
            "budget": "Medium (50rb - 150rb)",
            "produk": "The Ordinary Niacinamide 10% + Zinc 1%",
            "kandungan": "Niacinamide, Zinc",
            "harga": "Rp 130.000",
            "pakai": "Malam",
            "keterangan": "Mengurangi minyak berlebih dan jerawat ringan."
        },
        {
            "masalah": "Bruntusan",
            "tipe": "Sensitif",
            "budget": "Low (di bawah 50rb)",
            "produk": "Azarine Cica Toner",
            "kandungan": "Centella Asiatica",
            "harga": "Rp 38.000",
            "pakai": "Pagi",
            "keterangan": "Menenangkan kulit sensitif dan memperbaiki tekstur."
        },
        {
            "masalah": "Kulit Kusam",
            "tipe": "Kering",
            "budget": "High (di atas 150rb)",
            "produk": "Some By Mi Galactomyces Toner",
            "kandungan": "Galactomyces, Niacinamide",
            "harga": "Rp 180.000",
            "pakai": "Pagi",
            "keterangan": "Mencerahkan kulit kusam dan melembapkan."
        },
        {
            "masalah": "Flek Hitam",
            "tipe": "Kombinasi",
            "budget": "Medium (50rb - 150rb)",
            "produk": "Wardah Crystal Secret Dark Spot Serum",
            "kandungan": "Niacinamide, Tranexamic Acid",
            "harga": "Rp 110.000",
            "pakai": "Malam",
            "keterangan": "Menyamarkan noda hitam dan meratakan warna kulit."
        },
        {
            "masalah": "Kulit Kering",
            "tipe": "Kering",
            "budget": "Low (di bawah 50rb)",
            "produk": "Hada Labo Gokujyun Lotion Mini",
            "kandungan": "Hyaluronic Acid",
            "harga": "Rp 45.000",
            "pakai": "Pagi",
            "keterangan": "Menghidrasi kulit kering dan menjaga kelembapan."
        }
    ]

    hasil = []
    for item in database:
        if (
            item["masalah"] == masalah and
            item["tipe"] == tipe and
            item["budget"] == budget and
            (item["pakai"] == waktu or item["pakai"] == "Bisa Kapan Saja")
        ):
            hasil.append(item)

    return hasil

# TOMBOL REKOMENDASI
if st.button("🔍 Dapatkan Rekomendasi"):
    rekom = rekomendasi(masalah_kulit, tipe_kulit, budget, waktu)
    if rekom:
        for item in rekom:
            st.subheader(f"💄 {item['produk']}")
            st.write(f"✅ Kandungan: {item['kandungan']}")
            st.write(f"💰 Harga: {item['harga']}")
            st.write(f"🕒 Waktu Pakai: {item['pakai']}")
            st.info(item['keterangan'])
    else:
        st.warning("Tidak ada produk yang cocok dengan semua kriteria. Coba ubah pilihan.")