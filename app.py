import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Generator Infografis & Ringkasan", 
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 Generator Infografis & Ringkasan Bisnis")
st.write("Buat kartu ringkasan visual yang rapi dan profesional dalam hitungan detik.")

# Sidebar untuk Input Data
st.sidebar.header("⚙️ Pengaturan Infografis")
judul = st.sidebar.text_input("Judul Infografis:", value="Laporan Performa Keuangan")
subjudul = st.sidebar.text_input("Sub-Judul / Periode:", value="Kuartal I - Kantor Akuntan")

theme_color = st.sidebar.color_picker("Warna Tema Utama:", "#1E3A8A") # Warna Biru Gelap
bg_color = st.sidebar.color_picker("Warna Latar Belakang:", "#F8FAFC")

st.sidebar.subheader("📊 Poin-Poin Utama")
poin1_label = st.sidebar.text_input("Label 1:", value="Total Pendapatan")
poin1_val = st.sidebar.text_input("Nilai 1:", value="Rp 150.000.000")

poin2_label = st.sidebar.text_input("Label 2:", value="Margin Keuntungan")
poin2_val = st.sidebar.text_input("Nilai 2:", value="35.5%")

poin3_label = st.sidebar.text_input("Label 3:", value="Klien Aktif")
poin3_val = st.sidebar.text_input("Nilai 3:", value="42 Perusahaan")

catatan = st.sidebar.text_area("Catatan Tambahan:", value="Pertumbuhan stabil dipicu oleh peningkatan layanan konsultasi perpajakan.")

# Template HTML & CSS untuk Infografis
html_code = f"""
<div style="
    background-color: {bg_color};
    border-top: 8px solid {theme_color};
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #1F2937;
    margin-top: 10px;
">
    <h2 style="color: {theme_color}; margin-bottom: 4px; font-size: 28px;">{judul}</h2>
    <p style="color: #6B7280; font-size: 16px; margin-top: 0; margin-bottom: 24px;">{subjudul}</p>
    
    <div style="display: flex; gap: 15px; justify-content: space-between; margin-bottom: 24px; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 150px; background: white; padding: 15px; border-radius: 8px; border-left: 4px solid {theme_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <div style="font-size: 13px; color: #6B7280; font-weight: bold; text-transform: uppercase;">{poin1_label}</div>
            <div style="font-size: 20px; font-weight: bold; color: {theme_color}; margin-top: 5px;">{poin1_val}</div>
        </div>
        <div style="flex: 1; min-width: 150px; background: white; padding: 15px; border-radius: 8px; border-left: 4px solid {theme_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <div style="font-size: 13px; color: #6B7280; font-weight: bold; text-transform: uppercase;">{poin2_label}</div>
            <div style="font-size: 20px; font-weight: bold; color: {theme_color}; margin-top: 5px;">{poin2_val}</div>
        </div>
        <div style="flex: 1; min-width: 150px; background: white; padding: 15px; border-radius: 8px; border-left: 4px solid {theme_color}; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <div style="font-size: 13px; color: #6B7280; font-weight: bold; text-transform: uppercase;">{poin3_label}</div>
            <div style="font-size: 20px; font-weight: bold; color: {theme_color}; margin-top: 5px;">{poin3_val}</div>
        </div>
    </div>
    
    <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <strong style="color: {theme_color}; font-size: 14px;">📌 Ringkasan Eksekutif:</strong>
        <p style="margin-top: 8px; margin-bottom: 0; font-size: 14px; line-height: 1.5; color: #374151;">{catatan}</p>
    </div>
</div>
"""

# Tampilan Hasil Infografis
st.subheader("🖼️ Preview Infografis Anda")
st.components.v1.html(html_code, height=400, scrolling=True)

st.divider()

# Fitur Download HTML
st.download_button(
    label="📥 Download Hasil Infografis (HTML)",
    data=html_code,
    file_name="infografis_ringkasan.html",
    mime="text/html"
)
