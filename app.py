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
    "Dark Charcoal (Minimalis Premium)", 
    "Royal Purple (Kreatif & Elegan)"
])

# Penentuan Skema Warna
if "Navy" in theme_style:
    bg_style = "linear-gradient(135deg, #0b132b 0%, #1c2541 100%)"
    card_bg = "rgba(255, 255, 255, 0.07)"
    text_color = "#ffffff"
    accent_color = "#f59e0b" # Gold
    highlight_bg = "rgba(245, 158, 11, 0.15)"
elif "Emerald" in theme_style:
    bg_style = "linear-gradient(135deg, #064e3b 0%, #022c22 100%)"
    card_bg = "rgba(255, 255, 255, 0.08)"
    text_color = "#ffffff"
    accent_color = "#34d399" # Mint
    highlight_bg = "rgba(52, 211, 153, 0.15)"
elif "Dark Charcoal" in theme_style:
    bg_style = "linear-gradient(135deg, #18181b 0%, #09090b 100%)"
    card_bg = "rgba(255, 255, 255, 0.06)"
    text_color = "#ffffff"
    accent_color = "#38bdf8" # Sky Blue
    highlight_bg = "rgba(56, 189, 248, 0.15)"
else:
    bg_style = "linear-gradient(135deg, #3b0764 0%, #1e1b4b 100%)"
    card_bg = "rgba(255, 255, 255, 0.08)"
    text_color = "#ffffff"
    accent_color = "#f472b6" # Pink
    highlight_bg = "rgba(244, 114, 182, 0.15)"

st.sidebar.subheader("✍️ Isi Slide Infografis")

# Slide 1: Cover
st.sidebar.markdown("---")
st.sidebar.markdown("**Slide 1: Cover Utama**")
s1_tag = st.sidebar.text_input("Tagline Cover:", value="💡 TIPS PAJAK & KEUANGAN")
s1_title = st.sidebar.text_input("Judul Cover:", value="5 KESALAHAN PAJAK BISNIS YANG SERING TERJADI")
s1_subtitle = st.sidebar.text_input("Sub-Judul:", value="Hindari Denda Administrasi Sebelum Terlambat!")

# Slide 2: Infografis Poin 1 (Dengan Stat/Angka)
st.sidebar.markdown("---")
st.sidebar.markdown("**Slide 2: Poin 1 (Statistik/Highlight)**")
s2_title = st.sidebar.text_input("Judul Slide 2:", value="01. Salah Klasifikasi Biaya")
s2_stat_val = st.sidebar.text_input("Angka Infografis (Stat):", value="80%")
s2_stat_lbl = st.sidebar.text_input("Keterangan Stat:", value="UMKM Mengalami Kurang Bayar Pajak")
s2_body = st.sidebar.text_area("Penjelasan Slide 2:", value="Pencampuran biaya pribadi dan operasional membuat laporan keuangan tidak konsisten dan memicu sanksi denda.")

# Slide 3: Infografis Poin 2 (Highlight Box)
st.sidebar.markdown("---")
st.sidebar.markdown("**Slide 3: Poin 2 (Fitur Highlight Box)**")
s3_title = st.sidebar.text_input("Judul Slide 3:", value="02. Terlambat Lapor SPT Masa")
s3_highlight = st.sidebar.text_input("Teks Highlight Box:", value="⚠️ Denda Administrasi s/d Rp 500.000 / Bulan")
s3_body = st.sidebar.text_area("Penjelasan Slide 3:", value="Keterlambatan pelaporan PPN atau PPh Pasal 21 bulanan berakibat denda otomatis dari DJP.")

# Slide 4: Call to Action (CTA)
st.sidebar.markdown("---")
st.sidebar.markdown("**Slide 4: Penutup & Kontak**")
s4_title = st.sidebar.text_input("Judul Slide 4:", value="Perlu Audit & Pendampingan Pajak?")
s4_body = st.sidebar.text_area("Penjelasan Slide 4:", value="Tim Akuntan Publik kami siap membantu kerapian pembukuan dan efisiensi pajak usaha Anda.")
s4_cta = st.sidebar.text_input("Tombol CTA:", value="Hubungi Tim Konsultan 📩")

# Template HTML & JS (Infographic Card Layout)
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        body {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: #090d16;
            margin: 0;
            padding: 20px;
            color: #fff;
        }}
        .carousel-container {{
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding-bottom: 25px;
        }}
        .slide {{
            width: 320px;
            height: 420px;
            background: {bg_style};
            border-radius: 20px;
            padding: 25px;
            box-sizing: border-box;
            flex-shrink: 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 15px 35px rgba(0,0,0,0.6);
            border: 1px solid rgba(255, 255, 255, 0.12);
            position: relative;
        }}
        .brand-header {{
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: {accent_color};
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 10px;
        }}
        .tag-badge {{
            background: {highlight_bg};
            color: {accent_color};
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 10px;
            font-weight: 800;
            display: inline-block;
            margin-top: 12px;
        }}
        .slide-title {{
            font-size: 19px;
            font-weight: 800;
            line-height: 1.35;
            margin-top: 10px;
            color: {text_color};
        }}
        .stat-box {{
            background: {card_bg};
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 12px;
            border-radius: 12px;
            margin-top: 12px;
            text-align: center;
        }}
        .stat-number {{
            font-size: 28px;
            font-weight: 900;
            color: {accent_color};
        }}
        .stat-label {{
            font-size: 11px;
            opacity: 0.8;
            margin-top: 2px;
        }}
        .highlight-box {{
            background: {highlight_bg};
            border-left: 4px solid {accent_color};
            padding: 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            color: #fff;
            margin-top: 12px;
        }}
        .slide-body {{
            font-size: 12px;
            line-height: 1.5;
            opacity: 0.9;
            margin-top: 10px;
            color: #e2e8f0;
        }}
        .cta-btn {{
            background: {accent_color};
            color: #000;
            padding: 10px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: 800;
            text-align: center;
            margin-top: 15px;
        }}
        .footer-tag {{
            font-size: 10px;
            opacity: 0.5;
            text-align: right;
        }}
        .action-bar {{
            margin-top: 20px;
            text-align: center;
        }}
        .download-btn {{
            background-color: {accent_color};
            color: #000;
            font-weight: bold;
            border: none;
            padding: 12px 28px;
            border-radius: 10px;
            cursor: pointer;
            font-size: 14px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        }}
        .download-btn:hover {{
            opacity: 0.9;
        }}
    </style>
</head>
<body>

<div class="carousel-container">
    <!-- Slide 1 -->
    <div class="slide" id="slide-1">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>01/04</span>
            </div>
            <div class="tag-badge">{s1_tag}</div>
            <div class="slide-title" style="font-size: 21px; margin-top: 15px;">{s1_title}</div>
            <div class="slide-body" style="color: {accent_color}; font-weight: 600; margin-top: 12px;">{s1_subtitle}</div>
        </div>
        <div class="footer-tag">SWIPE KANAN ➔</div>
    </div>

    <!-- Slide 2 -->
    <div class="slide" id="slide-2">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>02/04</span>
            </div>
            <div class="slide-title">{s2_title}</div>
            <div class="stat-box">
                <div class="stat-number">{s2_stat_val}</div>
                <div class="stat-label">{s2_stat_lbl}</div>
            </div>
            <div class="slide-body">{s2_body}</div>
        </div>
        <div class="footer-tag">INFOGRAFIS #01</div>
    </div>

    <!-- Slide 3 -->
    <div class="slide" id="slide-3">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>03/04</span>
            </div>
            <div class="slide-title">{s3_title}</div>
            <div class="highlight-box">{s3_highlight}</div>
            <div class="slide-body">{s3_body}</div>
        </div>
        <div class="footer-tag">INFOGRAFIS #02</div>
    </div>

    <!-- Slide 4 -->
    <div class="slide" id="slide-4">
        <div>
            <div class="brand-header">
                <span>{brand_name}</span>
                <span>04/04</span>
            </div>
            <div class="slide-title">{s4_title}</div>
            <div class="slide-body">{s4_body}</div>
        </div>
        <div>
            <div class="cta-btn">{s4_cta}</div>
            <div class="footer-tag" style="margin-top: 8px;">{brand_name}</div>
        </div>
    </div>
</div>

<div class="action-bar">
    <button class="download-btn" onclick="downloadAllSlides()">📸 Unduh Semua Slide (PNG)</button>
</div>

<script>
function downloadSlide(slideId, filename) {{
    const element = document.getElementById(slideId);
    return html2canvas(element, {{ scale: 2 }}).then(canvas => {{
        const link = document.createElement('a');
        link.download = filename;
        link.href = canvas.toDataURL('image/png');
        link.click();
    }});
}}

async function downloadAllSlides() {{
    await downloadSlide('slide-1', 'Carousel_Slide_1.png');
    await downloadSlide('slide-2', 'Carousel_Slide_2.png');
    await downloadSlide('slide-3', 'Carousel_Slide_3.png');
    await downloadSlide('slide-4', 'Carousel_Slide_4.png');
}}
</script>

</body>
</html>
"""

# Render ke Streamlit
components.html(html_code, height=540, scrolling=True)
