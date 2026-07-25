import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Generator Carousel Media Sosial", 
    page_icon="📱",
    layout="wide"
)

st.title("📱 Generator Carousel Media Sosial")
st.write("Buat slide carousel bertema profesional untuk Instagram/LinkedIn dalam hitungan detik!")

# Sidebar Pengaturan Desain & Konten
st.sidebar.header("🎨 Desain & Tema")
theme_style = st.sidebar.selectbox("Pilih Gaya Warna Slide:", [
    "Navy Professional (Biru Gelap)", 
    "Emerald Business (Hijau Elegan)", 
    "Dark Slate (Minimalis Modern)", 
    "Gradient Sunset (Energetik)"
])

# Penentuan Skema Warna
if "Navy" in theme_style:
    bg_style = "linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%)"
    card_bg = "rgba(255, 255, 255, 0.08)"
    text_color = "#ffffff"
    accent_color = "#38bdf8"
elif "Emerald" in theme_style:
    bg_style = "linear-gradient(135deg, #064e3b 0%, #047857 100%)"
    card_bg = "rgba(255, 255, 255, 0.08)"
    text_color = "#ffffff"
    accent_color = "#34d399"
elif "Dark Slate" in theme_style:
    bg_style = "linear-gradient(135deg, #18181b 0%, #27272a 100%)"
    card_bg = "rgba(255, 255, 255, 0.05)"
    text_color = "#ffffff"
    accent_color = "#fbbf24"
else:
    bg_style = "linear-gradient(135deg, #4c0519 0%, #881337 100%)"
    card_bg = "rgba(255, 255, 255, 0.08)"
    text_color = "#ffffff"
    accent_color = "#fb7185"

st.sidebar.subheader("✍️ Isi Konten Slide")

# Slide 1: Cover
st.sidebar.markdown("---")
st.sidebar.markdown("**Slide 1: Cover Utama**")
s1_title = st.sidebar.text_input("Judul Cover:", value="5 RAHASIA MANAJEMEN KEUANGAN BISNIS")
s1_subtitle = st.sidebar.text_input("Sub-Judul Cover:", value="Tips Praktis untuk Memaksimalkan Margin Keuntungan")

# Slide 2: Poin Utama 1
st.sidebar.markdown("---")
st.sidebar.markdown("**Slide 2: Poin Pertama**")
s2_title = st.sidebar.text_input("Judul Slide 2:", value="01. Lakukan Separation Account")
s2_body = st.sidebar.text_area("Isi Slide 2:", value="Pisahkan dengan tegas rekening pribadi dan rekening operasional bisnis untuk menjaga ketepatan pembukuan.")

# Slide 3: Poin Utama 2
st.sidebar.markdown("---")
st.sidebar.markdown("**Slide 3: Poin Kedua**")
s3_title = st.sidebar.text_input("Judul Slide 3:", value="02. Hitung Margin Secara Presisi")
s3_body = st.sidebar.text_area("Isi Slide 3:", value="Pastikan kalkulasi HPP mencakup seluruh biaya tersembunyi agar penetapan harga jual tidak tergerus inflasi.")

# Slide 4: Call to Action (CTA)
st.sidebar.markdown("---")
st.sidebar.markdown("**Slide 4: Penutup / CTA**")
s4_title = st.sidebar.text_input("Judul Slide 4:", value="Butuh Bantuan Pembukuan & Pajak?")
s4_body = st.sidebar.text_area("Isi Slide 4:", value="Konsultasikan kebutuhan laporan keuangan bisnis Anda bersama tim ahli akuntan kami.")
s4_cta = st.sidebar.text_input("Pesan Tombol CTA:", value="Simpan & Bagikan Postingan Ini 📌")

# Template HTML & JS untuk Render Multi-Slide Carousel
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        body {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background: #0d1117;
            margin: 0;
            padding: 20px;
            color: #fff;
        }}
        .carousel-container {{
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding-bottom: 20px;
        }}
        .slide {{
            width: 320px;
            height: 400px;
            background: {bg_style};
            border-radius: 16px;
            padding: 30px 25px;
            box-sizing: border-box;
            flex-shrink: 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
        }}
        .slide-number {{
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: {accent_color};
            font-weight: 700;
        }}
        .slide-title {{
            font-size: 20px;
            font-weight: 800;
            line-height: 1.3;
            margin-top: 10px;
            color: {text_color};
        }}
        .slide-body {{
            font-size: 13px;
            line-height: 1.6;
            opacity: 0.9;
            margin-top: 15px;
            color: #e2e8f0;
        }}
        .cta-btn {{
            background: {accent_color};
            color: #000;
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: bold;
            text-align: center;
            margin-top: 15px;
        }}
        .action-bar {{
            margin-top: 25px;
            text-align: center;
        }}
        .download-btn {{
            background-color: {accent_color};
            color: #000;
            font-weight: bold;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
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
            <div class="slide-number">SLIDE 1 / COVER</div>
            <div class="slide-title" style="font-size: 22px; margin-top: 20px;">{s1_title}</div>
            <div class="slide-body" style="color: {accent_color}; font-weight: 600; font-size: 14px; margin-top: 15px;">{s1_subtitle}</div>
        </div>
        <div class="slide-number">SWIPE ME ➔</div>
    </div>

    <!-- Slide 2 -->
    <div class="slide" id="slide-2">
        <div>
            <div class="slide-number">SLIDE 2 / POIN 1</div>
            <div class="slide-title">{s2_title}</div>
            <div class="slide-body">{s2_body}</div>
        </div>
        <div class="slide-number">SLIDE 2</div>
    </div>

    <!-- Slide 3 -->
    <div class="slide" id="slide-3">
        <div>
            <div class="slide-number">SLIDE 3 / POIN 2</div>
            <div class="slide-title">{s3_title}</div>
            <div class="slide-body">{s3_body}</div>
        </div>
        <div class="slide-number">SLIDE 3</div>
    </div>

    <!-- Slide 4 -->
    <div class="slide" id="slide-4">
        <div>
            <div class="slide-number">SLIDE 4 / CTA</div>
            <div class="slide-title">{s4_title}</div>
            <div class="slide-body">{s4_body}</div>
        </div>
        <div class="cta-btn">{s4_cta}</div>
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

# Render ke Tampilan Streamlit
components.html(html_code, height=520, scrolling=True)
