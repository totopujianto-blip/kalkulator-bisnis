import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Generator Carousel Infografis", 
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Generator Carousel Infografis Bisnis")
st.write("Buat slide konten edukasi & infografis bisnis visual berestetika tinggi untuk media sosial.")

# Sidebar Pengaturan Desain & Branding
st.sidebar.header("🏢 Branding & Tema")
brand_name = st.sidebar.text_input("Nama Brand / Usaha:", value="KJA Zainal, Totok & Rekan")

theme_style = st.sidebar.selectbox("Pilih Gaya Warna Slide:", [
    "Navy Gold (Mewah & Profesional)", 
    "Emerald Mint (Fresh & Modern)", 
    "Dark Charcoal (Minimalis Premium)"
])

# Penentuan Skema Warna
if "Navy" in theme_style:
    bg_style = "linear-gradient(135deg, #0b132b 0%, #1c2541 100%)"
    accent_color = "#f59e0b"
elif "Emerald" in theme_style:
    bg_style = "linear-gradient(135deg, #064e3b 0%, #022c22 100%)"
    accent_color = "#34d399"
else:
    bg_style = "linear-gradient(135deg, #18181b 0%, #09090b 100%)"
    accent_color = "#38bdf8"

st.sidebar.subheader("✍️ Isi Slide Infografis")

# Input Slide 1
s1_tag = st.sidebar.text_input("Tagline Cover:", value="💡 TIPS PAJAK & KEUANGAN")
s1_title = st.sidebar.text_input("Judul Cover:", value="5 KESALAHAN PAJAK BISNIS YANG SERING TERJADI")
s1_subtitle = st.sidebar.text_input("Sub-Judul:", value="Hindari Denda Administrasi Sebelum Terlambat!")

# Input Slide 2
s2_title = st.sidebar.text_input("Judul Slide 2:", value="01. Salah Klasifikasi Biaya")
s2_stat_val = st.sidebar.text_input("Angka Stat:", value="80%")
s2_stat_lbl = st.sidebar.text_input("Keterangan Stat:", value="UMKM Mengalami Kurang Bayar Pajak")
s2_body = st.sidebar.text_area("Penjelasan Slide 2:", value="Pencampuran biaya pribadi dan operasional membuat laporan keuangan tidak konsisten.")

# Input Slide 3
s3_title = st.sidebar.text_input("Judul Slide 3:", value="02. Terlambat Lapor SPT Masa")
s3_highlight = st.sidebar.text_input("Highlight Box:", value="⚠️ Denda Administrasi s/d Rp 500.000 / Bulan")
s3_body = st.sidebar.text_area("Penjelasan Slide 3:", value="Keterlambatan pelaporan PPN atau PPh bulanan berakibat denda otomatis dari DJP.")

# HTML Template (Diuji tanpa konflik kurung kurawal)
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #090d16;
            margin: 0;
            padding: 20px;
            color: #ffffff;
        }}
        .carousel-container {{
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding-bottom: 20px;
        }}
        .slide {{
            width: 300px;
            height: 400px;
            background: {bg_style};
            border-radius: 16px;
            padding: 20px;
            box-sizing: border-box;
            flex-shrink: 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .brand-header {{
            font-size: 11px;
            font-weight: bold;
            color: {accent_color};
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 8px;
            display: flex;
            justify-content: space-between;
        }}
        .tag-badge {{
            background: rgba(255,255,255,0.1);
            color: {accent_color};
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 10px;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        }}
        .slide-title {{
            font-size: 18px;
            font-weight: bold;
            margin-top: 10px;
            line-height: 1.3;
        }}
        .stat-box {{
            background: rgba(255,255,255,0.08);
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
            text-align: center;
        }}
        .stat-number {{
            font-size: 26px;
            font-weight: bold;
            color: {accent_color};
        }}
        .highlight-box {{
            background: rgba(255,255,255,0.1);
            border-left: 3px solid {accent_color};
            padding: 8px;
            font-size: 11px;
            margin-top: 10px;
        }}
        .slide-body {{
            font-size: 12px;
            opacity: 0.9;
            margin-top: 8px;
            line-height: 1.4;
        }}
        .footer-tag {{
            font-size: 10px;
            opacity: 0.5;
            text-align: right;
        }}
    </style>
</head>
<body>

<div class="carousel-container">
    <!-- Slide 1 -->
    <div class="slide">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>01/03</span>
            </div>
            <div class="tag-badge">{s1_tag}</div>
            <div class="slide-title">{s1_title}</div>
            <div class="slide-body" style="color: {accent_color}; font-weight: bold;">{s1_subtitle}</div>
        </div>
        <div class="footer-tag">SWIPE KANAN ➔</div>
    </div>

    <!-- Slide 2 -->
    <div class="slide">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>02/03</span>
            </div>
            <div class="slide-title">{s2_title}</div>
            <div class="stat-box">
                <div class="stat-number">{s2_stat_val}</div>
                <div style="font-size: 10px;">{s2_stat_lbl}</div>
            </div>
            <div class="slide-body">{s2_body}</div>
        </div>
        <div class="footer-tag">INFOGRAFIS #01</div>
    </div>

    <!-- Slide 3 -->
    <div class="slide">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>03/03</span>
            </div>
            <div class="slide-title">{s3_title}</div>
            <div class="highlight-box">{s3_highlight}</div>
            <div class="slide-body">{s3_body}</div>
        </div>
        <div class="footer-tag">INFOGRAFIS #02</div>
    </div>
</div>

</body>
</html>
"""

# Render langsung tanpa script eksternal pemblokir
components.html(html_code, height=480, scrolling=True)
