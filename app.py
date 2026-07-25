import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(
    page_title="Kalkulator Keuangan Bisnis", 
    page_icon="💰",
    layout="centered"
)

st.title("💰 Kalkulator Keuangan & Margin Bisnis")
st.write("Alat bantu hitung margin keuntungan, harga jual ideal, dan estimasi pajak bisnis Anda.")

# Menu Tab
tab1, tab2 = st.tabs(["📊 Margin & Harga Jual", "🧾 Kalkulator PPN / Pajak"])

# ==========================================
# TAB 1: KALKULATOR MARGIN & HARGA JUAL
# ==========================================
with tab1:
    st.subheader("Hitung Harga Jual & Keuntungan")
    
    col1, col2 = st.columns(2)
    with col1:
        hpp = st.number_input("Harga Pokok Penjualan / HPP (Rp):", min_value=0, value=50000, step=1000)
    with col2:
        target_margin = st.number_input("Target Margin Keuntungan (%):", min_value=0.0, max_value=99.0, value=30.0, step=1.0)
    
    if hpp > 0:
        # Rumus Margin: Harga Jual = HPP / (1 - Margin%)
        harga_jual = hpp / (1 - (target_margin / 100))
        profit = harga_jual - hpp
        markup = (profit / hpp) * 100
        
        st.divider()
        st.markdown("### 🎯 Hasil Perhitungan:")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Harga Jual Ideal", f"Rp {harga_jual:,.0f}")
        c2.metric("Keuntungan (Profit)", f"Rp {profit:,.0f}")
        c3.metric("Persentase Markup", f"{markup:.1f}%")
        
        st.info(f"💡 **Penjelasan:** Untuk mendapatkan **margin {target_margin}%**, Anda perlu menjual produk seharga **Rp {harga_jual:,.0f}** (markup **{markup:.1f}%** dari HPP).")

# ==========================================
# TAB 2: KALKULATOR PPN / PAJAK
# ==========================================
with tab2:
    st.subheader("Hitung PPN & Total Tagihan")
    
    tipe_pajak = st.radio("Metode Perhitungan PPN:", ["Belum Termasuk PPN (Exclude)", "Sudah Termasuk PPN (Include)"])
    
    col_a, col_b = st.columns(2)
    with col_a:
        nominal = st.number_input("Nominal Transaksi (Rp):", min_value=0, value=1000000, step=50000)
    with col_b:
        tarif_ppn = st.number_input("Tarif PPN (%):", min_value=0.0, value=11.0, step=0.5)
        
    if nominal > 0:
        st.divider()
        if tipe_pajak == "Belum Termasuk PPN (Exclude)":
            pajak = nominal * (tarif_ppn / 100)
            total = nominal + pajak
            dpp = nominal
        else:
            # Include PPN
            dpp = nominal / (1 + (tarif_ppn / 100))
            pajak = nominal - dpp
            total = nominal
            
        st.markdown("### 📑 Rincian Transaksi:")
        
        df_pajak = pd.DataFrame({
            "Komponen": ["DPP (Dasar Pengenaan Pajak)", f"PPN ({tarif_ppn}%)", "Total Pembayaran"],
            "Jumlah (Rp)": [f"Rp {dpp:,.0f}", f"Rp {pajak:,.0f}", f"Rp {total:,.0f}"]
        })
        
        st.table(df_pajak)
