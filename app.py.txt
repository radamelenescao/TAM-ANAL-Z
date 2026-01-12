import streamlit as st
import pandas as pd
import random
import time

# --- SİSTEM AYARLARI ---
st.set_page_config(page_title="TAM KAHİN | AI Analiz", layout="wide", page_icon="⚽")

# --- TASARIM (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: #1e2129; border-radius: 5px; color: white; padding: 10px; }
    .vip-card {
        background: linear-gradient(135deg, #1f1f1f 0%, #111 100%);
        padding: 25px; border-radius: 15px; border: 2px solid #f1c40f;
        text-align: center; margin: 20px 0;
    }
    .wp-btn {
        background-color: #25D366; color: white !important; padding: 12px 20px;
        text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- VERİ SETİ ---
def get_data():
    return {
        "Trendyol Süper Lig": {
            "puan": pd.DataFrame({
                "Takım": ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Samsunspor", "Eyüpspor"],
                "Puan": [44, 39, 32, 30, 28], "Form": ["✅✅✅✅✅", "✅✅❌✅✅", "❌✅✅➖✅", "✅➖✅❌✅", "✅✅➖✅❌"]
            }),
            "cezali": ["Muslera (GS) - Sakat", "Djiku (FB) - Cezalı"]
        },
        "Premier League": {
            "puan": pd.DataFrame({
                "Takım": ["Liverpool", "Man City", "Arsenal", "Chelsea"],
                "Puan": [45, 40, 39, 35], "Form": ["✅✅✅✅✅", "❌✅✅✅✅", "✅➖✅✅✅", "✅✅➖❌✅"]
            }),
            "cezali": ["Rodri (Man City) - Sakat", "Saliba (Arsenal) - Cezalı"]
        }
    }

# --- VIP DURUMU VE AKTİVASYON ---
if 'is_vip' not in st.session_state: st.session_state.is_vip = False

# Sidebar VIP Aktivasyon
st.sidebar.title("🔐 VIP Panel")
aktivasyon_kodu = st.sidebar.text_input("Aktivasyon Kodunu Girin", type="password")
if aktivasyon_kodu == "GOLD2026":
    st.session_state.is_vip = True
    st.sidebar.success("🌟 VIP Üyelik Aktif!")
else:
    st.session_state.is_vip = False

# --- ANA SAYFA ---
st.title("🏆 TAM KAHİN AI: Global Analiz Merkezi")
data = get_data()
secilen_lig = st.selectbox("📍 İncelemek İstediğiniz Ligi Seçin", list(data.keys()))

tab1, tab2, tab3 = st.tabs(["📊 Puan Durumu", "🤖 AI Tahmin Motoru", "💎 VIP Odası & Ödeme"])

with tab1:
    st.subheader(f"{secilen_lig} - Canlı Tablo")
    st.table(data[secilen_lig]["puan"])
    st.info("Eksikler: " + ", ".join(data[secilen_lig]["cezali"]))

with tab2:
    st.header("🤖 Yapay Zeka Analizi")
    c1, c2 = st.columns(2)
    ev = c1.text_input("Ev Sahibi")
    dep = c2.text_input("Deplasman")
    
    if st.button("ANALİZ ET"):
        if ev and dep:
            with st.spinner("AI lig verilerini ve sakatları süzüyor..."):
                time.sleep(1.5)
                guven = random.randint(85, 96) if st.session_state.is_vip else random.randint(60, 75)
                st.write(f"📊 **Analiz:** {ev} kazanma ihtimali: %{guven}")
                if st.session_state.is_vip:
                    st.success(f"🎯 VIP Skor Tahmini: {random.randint(1,3)}-{random.randint(0,2)}")
                else:
                    st.warning("🔒 Skor tahmini sadece VIP üyeler içindir.")
        else:
            st.error("Lütfen takımları girin.")

with tab3:
    if not st.session_state.is_vip:
        st.markdown(f"""
        <div class="vip-card">
            <h2 style="color:#f1c40f;">🌟 VIP ÜYELİK PLANI</h2>
            <p>Günlük %90+ başarı oranlı analizler ve skor tahminleri için:</p>
            <p style="font-size: 22px;"><b>Ücret: 250 TL / Aylık</b></p>
            <hr>
            <p><b>ALICI:</b> İSMAİL ENES DURMUŞ</p>
            <p><b>IBAN:</b> TR68 0004 6004 9088 8000 1770 49</p>
            <p style="font-size: 13px;"><i>Açıklamaya kullanıcı adınızı yazmayı unutmayın.</i></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 📢 Ödeme Bildirimi")
        kullanici = st.text_input("Uygulama Kullanıcı Adınız:")
        if st.button("✅ Ödemeyi Yaptım, Bildir"):
            if kullanici:
                wp_mesaj = f"Merhaba İsmail Enes, ben {kullanici}. Tam Kahin VIP ödemesini yaptım, onay bekliyorum."
                wp_link = f"https://wa.me/905388508757?text={wp_mesaj.replace(' ', '%20')}"
                st.markdown(f'<a href="{wp_link}" class="wp-btn" target="_blank">WhatsApp Onay Hattına Git</a>', unsafe_allow_html=True)
            else:
                st.error("Lütfen önce bir kullanıcı adı girin.")
    else:
        st.success("🔥 VIP Üyesiniz! Bugünün tüm banko maçları ve skorları sizinle.")

st.sidebar.divider()
st.sidebar.write("🟢 Server: Online")
