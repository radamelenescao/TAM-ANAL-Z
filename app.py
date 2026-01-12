import streamlit as st
import random
import time
import pandas as pd # İstatistik tabloları için

# --- SAYFA AYARLARI & TASARIM ---
st.set_page_config(page_title="Football AI Global", layout="wide", page_icon="🏆")

# Özel VIP Tasarımı (Altın Renkler)
st.markdown("""
    <style>
    .vip-text { color: #f1c40f !important; font-weight: bold; }
    .stat-box { background-color: #1e1e1e; padding: 15px; border-radius: 10px; border-left: 5px solid #f1c40f; }
    </style>
    """, unsafe_allow_html=True)

# --- SİSTEM DEĞİŞKENLERİ ---
if 'is_vip' not in st.session_state: st.session_state.is_vip = False

# --- 1. CANLI VERİ SERVİSİ (SİMÜLASYON) ---
# Gerçekte burada API-Football veya Opta API'den veri çekilir.
def get_league_stats():
    data = {
        "Gol Krallığı": [
            {"Oyuncu": "Erling Haaland", "Takım": "Man City", "Gol": 18},
            {"Oyuncu": "Mauro Icardi", "Takım": "Galatasaray", "Gol": 15},
            {"Oyuncu": "Robert Lewandowski", "Takım": "Barcelona", "Gol": 14}
        ],
        "Asist Krallığı": [
            {"Oyuncu": "Kevin De Bruyne", "Takım": "Man City", "Asist": 12},
            {"Oyuncu": "Kerem Aktürkoğlu", "Takım": "Galatasaray", "Asist": 9}
        ],
        "Cezalılar": [
            {"Oyuncu": "Sergio Ramos", "Takım": "Sevilla", "Neden": "Kırmızı Kart", "Dönüş": "1 Hafta"},
            {"Oyuncu": "Fred", "Takım": "Fenerbahçe", "Neden": "Sarı Kart Sınırı", "Dönüş": "Hemen"}
        ]
    }
    return data

# --- 2. ANA ARAYÜZ ---
st.title("🌍 Global Football AI & Data Center")

# Dil ve Bölge Seçimi
c1, c2 = st.columns(2)
lang = c1.selectbox("🌐 Dil / Language", ["Türkçe", "English", "Spanish", "German"])
region = c2.selectbox("📍 Bölge / Region", ["Türkiye", "Europe", "South America", "Asia"])

# --- 3. YENİ ÖZELLİKLER: İSTATİSTİK MERKEZİ ---
st.divider()
st.header("📊 Canlı Lig İstatistikleri")

stat_tab1, stat_tab2, stat_tab3, stat_tab4 = st.tabs([
    "📈 Puan Durumu", "⚽ Gol/Asist Krallığı", "🚫 Cezalılar", "🏃 Takım/Oyuncu Analizi"
])

stats = get_league_stats()

with stat_tab1:
    st.subheader(f"{region} - Canlı Puan Durumu")
    # Örnek Puan Durumu Tablosu
    df_puan = pd.DataFrame({
        "Sıra": [1, 2, 3],
        "Takım": ["Real Madrid", "Man City", "Galatasaray"],
        "Maç": [20, 20, 20],
        "Puan": [52, 50, 48],
        "Form": ["✅✅✅✅✅", "✅✅➖✅✅", "✅❌✅✅✅"]
    })
    st.table(df_puan)

with stat_tab2:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("🔥 Gol Krallığı")
        st.dataframe(pd.DataFrame(stats["Gol Krallığı"]))
    with col_b:
        st.subheader("🎯 Asist Krallığı")
        st.dataframe(pd.DataFrame(stats["Asist Krallığı"]))

with stat_tab3:
    st.subheader("❌ Cezalı ve Sakat Oyuncu Bilgisi")
    st.warning("Bu veriler maç kadrolarını %100 etkiler. Tahmin yaparken dikkate alın.")
    st.dataframe(pd.DataFrame(stats["Cezalılar"]))

with stat_tab4:
    st.subheader("👤 Detaylı Oyuncu Analizi (Opta Verileri)")
    player = st.text_input("Oyuncu İsmi Girin (Örn: Mbappe)")
    if player:
        st.write(f"**{player}** için maç başı şut: 3.5, Başarılı dripling: %65, Pas isabeti: %88")
        if not st.session_state.is_vip:
            st.error("Daha detaylı 'Isı Haritası' ve 'XG' verileri için VIP üyelik gereklidir.")

# --- 4. PREMİUM & AI TAHMİN ---
st.sidebar.title("💎 VIP Kontrol Paneli")
if st.sidebar.button("VIP SATIN AL (100 TL)"):
    st.session_state.is_vip = True
    st.sidebar.success("VIP Üyelik Aktif!")

st.divider()
st.header("🤖 AI Maç Tahmin Motoru")
h_team = st.text_input("Ev Sahibi Takım")
a_team = st.text_input("Deplasman Takımı")

if st.button("ANALİZ ET"):
    with st.spinner("Yapay zeka cezalıları ve puan durumunu kontrol ediyor..."):
        time.sleep(2)
    
    if st.session_state.is_vip:
        st.balloons()
        st.success("✅ VIP ANALİZ TAMAMLANDI")
        st.write("**Gelişmiş Tahmin:** Cezalı oyuncular ve takımların son form durumu analiz edildiğinde, Ev Sahibi galibiyeti %88 güvenle önerilir.")
        st.metric("Beklenen Skor", "3 - 1")
    else:
        st.warning("Standart tahmin: 1 (Güven: %65). %88 güvenli skor ve cezalı analizi için VIP olun.")
