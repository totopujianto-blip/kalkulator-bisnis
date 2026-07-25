import streamlit as st
from g4f.client import Client

st.set_page_config(page_title="Infographic Generator", page_icon="🎨")
st.title("🎨 Generator Infografis")

# Input Topik (API Key tidak lagi diperlukan)
topik = st.text_input("Masukkan Topik Infografis:", placeholder="Contoh: Manfaat Air Putih")

if st.button("🚀 Buat Infografis", type="primary"):
    if not topik:
        st.warning("Silakan masukkan topik terlebih dahulu.")
    else:
        try:
            client = Client()
            
            prompt_text = f"""
            Anda adalah desainer konten viral. Buat ringkasan naskah infografis singkat 
            berbahasa Indonesia berdasarkan topik berikut: '{topik}'. 
            
            Teks harus terdiri dari: 
            1. Judul Utama (Singkat & Menarik), 
            2. Pengenalan (1 kalimat), 
            3. 3 Poin Krusial (Fakta, Dampak, Solusi), 
            4. Kesimpulan Singkat. Buat ringkas dan mudah dibaca.
            """
            
            with st.spinner("Sedang meracik naskah infografis..."):
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt_text}]
                )
                
                st.success("✨ Naskah Infografis Berhasil Dibuat!")
                st.markdown(response.choices[0].message.content)
                
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses permintaan: {e}")