import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Generator Carousel Infografis", 
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Generator Carousel Infografis Bisnis")
st.write("Buat slide konten edukasi & infografis bisnis visual lengkap dengan gambar ilustrasi untuk media sosial.")

# Sidebar Pengaturan Branding & Tema
st.sidebar.header("🏢 Branding & Tema")
brand_name = st.sidebar.text_input("Nama Brand / Usaha:", value="KJA Zainal, Totok & Rekan")

theme_style = st.sidebar.selectbox("Pilih Gaya Warna Slide:", [
    "Navy Gold (Mewah & Profesional)", 
    "Emerald Mint (Fresh & Modern)", 
    "Dark Charcoal (Minimalis Premium)"
])

if "Navy" in theme_style:
    bg_color = "#1c2541"
    accent_color = "#f59e0b"
    card_bg = "#0b132b"
elif "Emerald" in theme_style:
    bg_color = "#044e3b"
    accent_color = "#34d399"
    card_bg = "#022c22"
else:
    bg_color = "#27272a"
    accent_color = "#38bdf8"
    card_bg = "#18181b"

st.sidebar.subheader("✍️ Isi Slide & URL Ilustrasi")

# Input Data Slide 1
s1_tag = st.sidebar.text_input("Tagline Cover:", value="💡 TIPS PAJAK & KEUANGAN")
s1_title = st.sidebar.text_input("Judul Cover:", value="5 KESALAHAN PAJAK BISNIS YANG SERING TERJADI")
s1_subtitle = st.sidebar.text_input("Sub-Judul:", value="Hindari Denda Administrasi Sebelum Terlambat!")
s1_img = st.sidebar.text_input("URL Gambar Slide 1:", value="https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=600&auto=format&fit=crop&q=80")

# Input Data Slide 2
s2_title = st.sidebar.text_input("Judul Slide 2:", value="01. Salah Klasifikasi Biaya")
s2_stat_val = st.sidebar.text_input("Angka Stat:", value="80%")
s2_stat_lbl = st.sidebar.text_input("Keterangan Stat:", value="UMKM Mengalami Kurang Bayar Pajak")
s2_body = st.sidebar.text_area("Penjelasan Slide 2:", value="Pencampuran biaya pribadi dan operasional membuat laporan keuangan tidak konsisten.")
s2_img = st.sidebar.text_input("URL Gambar Slide 2:", value="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&auto=format&fit=crop&q=80")

# Input Data Slide 3
s3_title = st.sidebar.text_input("Judul Slide 3:", value="02. Terlambat Lapor SPT Masa")
s3_highlight = st.sidebar.text_input("Highlight Box:", value="⚠️ Denda Administrasi s/d Rp 500.000 / Bulan")
s3_body = st.sidebar.text_area("Penjelasan Slide 3:", value="Keterlambatan pelaporan PPN atau PPh bulanan berakibat denda otomatis dari DJP.")
s3_img = st.sidebar.text_input("URL Gambar Slide 3:", value="https://images.unsplash.com/photo-1586486855514-8c633cc6fd38?w=600&auto=format&fit=crop&q=80")

# Tampilan Grid Slide
st.markdown("### 📱 Preview Slide Carousel")

col1, col2, col3 = st.columns(3)

# Style CSS Kustom untuk Kartu & Gambar
css_style = f"""
<style>
    .slide-card {{
        background-color: {card_bg};
        border: 2px solid {bg_color};
        border-radius: 16px;
        padding: 20px;
        min-height: 520px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        color: white;
        font-family: sans-serif;
        box-shadow: 0 10px 20px rgba(0,0,0,0.25);
    }}
    .brand-header {{
        font-size: 11px;
        font-weight: bold;
        color: {accent_color};
        border-bottom: 1px solid rgba(255,255,255,0.1);
        padding-bottom: 8px;
        display: flex;
        justify-content: space-between;
    }}
    .badge {{
        background-color: rgba(255,255,255,0.1);
        color: {accent_color};
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }}
    .slide-img {{
        width: 100%;
        height: 140px;
        object-fit: cover;
        border-radius: 10px;
        margin-top: 12px;
        border: 1px solid rgba(255,255,255,0.1);
    }}
    .card-title {{
        font-size: 17px;
        font-weight: bold;
        margin-top: 10px;
        line-height: 1.3;
    }}
    .stat-box {{
        background-color: rgba(255,255,255,0.05);
        border-radius: 8px;
        padding: 8px;
        text-align: center;
        margin-top: 10px;
        border: 1px solid rgba(255,255,255,0.1);
    }}
    .stat-val {{
        font-size: 24px;
        font-weight: bold;
        color: {accent_color};
    }}
    .highlight-box {{
        background-color: rgba(255,255,255,0.08);
        border-left: 4px solid {accent_color};
        padding: 8px;
        font-size: 11px;
        border-radius: 4px;
        margin-top: 10px;
    }}
    .card-body {{
        font-size: 12px;
        opacity: 0.9;
        margin-top: 8px;
        line-height: 1.4;
    }}
    .card-footer {{
        font-size: 10px;
        opacity: 0.5;
        text-align: right;
        margin-top: 12px;
    }}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# Slide 1
with col1:
    st.markdown(f"""
    <div class="slide-card">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>01/03</span>
            </div>
            <div class="badge">{s1_tag}</div>
            <img src="{s1_img}" class="slide-img">
            <div class="card-title">{s1_title}</div>
            <div class="card-body" style="color: {accent_color}; font-weight: bold;">{s1_subtitle}</div>
        </div>
        <div class="card-footer">SWIPE KANAN ➔</div>
    </div>
    """, unsafe_allow_html=True)

# Slide 2
with col2:
    st.markdown(f"""
    <div class="slide-card">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>02/03</span>
            </div>
            <div class="card-title">{s2_title}</div>
            <img src="{s2_img}" class="slide-img">
            <div class="stat-box">
                <div class="stat-val">{s2_stat_val}</div>
                <div style="font-size: 10px; opacity: 0.8;">{s2_stat_lbl}</div>
            </div>
            <div class="card-body">{s2_body}</div>
        </div>
        <div class="card-footer">INFOGRAFIS #01</div>
    </div>
    """, unsafe_allow_html=True)

# Slide 3
with col3:
    st.markdown(f"""
    <div class="slide-card">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>03/03</span>
            </div>
            <div class="card-title">{s3_title}</div>
            <img src="{s3_img}" class="slide-img">
            <div class="highlight-box">{s3_highlight}</div>
            <div class="card-body">{s3_body}</div>
        </div>
        <div class="card-footer">INFOGRAFIS #02</div>
    </div>
    """, unsafe_allow_html=True)
