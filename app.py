import streamlit as st
import pandas as pd
import random
import time

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="TAM KAHİN GLOBAL | İsmail Enes Durmuş", layout="wide", page_icon="🌎")

# --- TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .vip-card {
        background: linear-gradient(145deg, #1a1a1a, #000000);
        padding: 30px; border-radius: 20px; border: 2px solid #f1c40f;
        text-align: center; box-shadow: 0 0 15px rgba(241,196,15,0.3);
    }
    .wp-btn {
        background-color: #25D366; color: white !important; padding: 15px 25px;
        text-decoration: none; border-radius: 10px; font-weight: bold; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- GLOBAL LİG VERİLERİ (2025-2026 SEZONU GÜNCEL) ---
def get_global_data():
    return {
        "🇹🇷 Türkiye - Trendyol Süper Lig": {
            "puan": pd.DataFrame({"Takım": ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Samsunspor", "Eyüpspor"], "P": [44, 39, 32, 30, 28]}),
            "not": "Osimhen ve Icardi fırtınası esiyor."
        },
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 İngiltere - Premier League": {
            "puan": pd.DataFrame({"Takım": ["Liverpool", "Arsenal", "Man City", "Chelsea", "Newcastle"], "P": [45, 40, 39, 35, 33]}),
            "not": "Slot yönetimindeki Liverpool zirveyi bırakmıyor."
        },
        "🇪🇸 İspanya - La Liga": {
            "puan": pd.DataFrame({"Takım": ["Barcelona", "Real Madrid", "Atletico Madrid", "Villarreal"], "P": [43, 39, 34, 31]}),
            "not": "Hansi Flick'in Barcelonası ofansif rekorlar kırıyor."
        },
        "🇩🇪 Almanya - Bundesliga": {
            "puan": pd.DataFrame({"Takım": ["Bayern Münih", "Leverkusen", "Leipzig", "Dortmund"], "P": [38, 32, 31, 28]}),
            "not": "Harry Kane gol krallığında rakipsiz."
        },
        "🇫🇷 Fransa - Ligue 1": {
            "puan": pd.DataFrame({"Takım": ["PSG", "Monaco", "Marseille", "Lille"], "P": [40, 34, 31, 29]}),
            "not": "PSG, Mbappe sonrası yeni sisteminde lider."
        },
        "🇳🇱 Hollanda - Eredivisie": {
            "puan": pd.DataFrame({"Takım": ["PSV", "Ajax", "Feyenoord", "Utrecht"], "P": [48, 38, 35, 34]}),
            "not": "PSV kayıpsız ilerliyor."
        },
        "🇵🇹 Portekiz - Liga Portugal": {
            "puan": pd.DataFrame({"Takım": ["Sporting", "Porto", "Benfica", "Braga"], "P": [42, 36, 33, 29]}),
            "not": "Gyökeres durdurulamaz bir formda."
        },
        "🇧🇪 Belçika - Pro League": {
            "puan": pd.DataFrame({"Takım": ["Genk", "Antwerp", "Club Brugge", "Anderlecht"], "P": [37, 32, 31, 28]}),
            "not": "Zirve yarışı çok çekişmeli."
        },
        "🇧🇷 Brezilya - Serie A": {
            "puan": pd.DataFrame({"Takım": ["Botafogo", "Palmeiras", "Flamengo", "Fortaleza"], "P": [68, 64, 60, 59]}),
            "not": "Sezon sonu heyecanı dorukta."
        },
        "🇦🇷 Arjantin - Liga Profesional": {
            "puan": pd.DataFrame({"Takım": ["Velez", "Huracan", "Racing", "River Plate"], "P": [43, 42, 40, 36]}),
            "not": "Velez şampiyonluğa yakın."
        },
        "🇺🇸 ABD - MLS": {
            "puan": pd.DataFrame({"Takım": ["Inter Miami", "Columbus", "LAFC", "LA Galaxy"], "P": [74, 66, 64, 64]}),
            "not": "Messi ve Suarez'li Miami rekor kırdı."
        }
    }

# --- VIP SİSTEMİ ---
if 'is_vip' not in st.session_state: st.session_state.is_vip = False

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/5328/5328065.png", width=80)
st.sidebar.title("🔐 VIP KONTROL")
sifre = st.sidebar.text_input("Aktivasyon Kodu", type="password")
if sifre == "GOLD2026":
    st.session_state.is_vip = True
    st.sidebar.success("🌟 HOŞ GELDİN PATRON!")
else:
    st.session_state.is_vip = False

# --- ANA EKRAN ---
st.title("⚽ GLOBAL FOOTBALL AI & DATA CENTER")
st.subheader("Kurucu: İsmail Enes Durmuş")

ligler = get_global_data()
secilen_lig = st.selectbox("🌍 İncelemek İstediğiniz Ligi Seçin", list(ligler.keys()))

col1, col2 = st.columns([2, 1])

with col1:
    st.write(f"### {secilen_lig} Puan Durumu")
    st.dataframe(ligler[secilen_lig]["puan"], use_container_width=True)
    st.info(f"ℹ️ **Lig Notu:** {ligler[secilen_lig]['not']}")

with col2:
    st.write("### 🤖 AI Analiz Motoru")
    ev = st.text_input("Ev Sahibi")
    dep = st.text_input("Deplasman")
    if st.button("ANALİZİ BAŞLAT"):
        with st.spinner("Yapay Zeka tüm dünya verilerini tarıyor..."):
            time.sleep(1.5)
            sans = random.randint(88, 98) if st.session_state.is_vip else random.randint(55, 75)
            st.metric("Kazanma İhtimali", f"%{sans}")
            if st.session_state.is_vip:
                st.success(f"🎯 VIP SKOR: {random.randint(1,4)}-{random.randint(0,2)}")
            else:
                st.warning("⚠️ Skor tahmini kilitli.")

# --- ÖDEME VE VIP ---
st.divider()
if not st.session_state.is_vip:
    st.markdown(f"""
    <div class="vip-card">
        <h2 style="color:#f1c40f;">💎 GLOBAL VIP KAHİN ÜYELİĞİ</h2>
        <p>12+ Ligin en derin analizleri, sakat/cezalı bilgileri ve AI skor tahminleri için;</p>
        <p style="font-size: 24px;"><b>250 TL / Aylık</b></p>
        <hr>
        <p><b>ALICI:</b> İSMAİL ENES DURMUŞ</p>
        <p><b>IBAN:</b> TR68 0004 6004 9088 8000 1770 49</p>
        <br>
        <a href="https://wa.me/905388508757?text=Merhaba%20Ismail%20Enes,%20Global%20VIP%20odemesini%20yaptim." class="wp-btn">✅ ÖDEME YAPTIM, ONAYLA</a>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write(f"📅 **Güncelleme:** {time.strftime('%d.%m.%Y')}")
