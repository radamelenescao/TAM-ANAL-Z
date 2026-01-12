import streamlit as st
import pandas as pd
import requests

# --- AYARLAR ---
st.set_page_config(page_title="TAM KAHİN GLOBAL", layout="wide")

# BURAYA kopyaladığın o uzun anahtarı yapıştır
API_KEY = "8402333254msh7779a0414d0c81bp1fda55jsnf5e3f57d9586" 

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# --- CANLI VERİ FONKSİYONU ---
@st.cache_data(ttl=600)
def get_live_data(league_id):
    url = "https://api-football-v1.p.rapidapi.com/v3/standings"
    querystring = {"league": str(league_id), "season": "2025"}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    try:
        standings = data['response'][0]['league']['standings'][0]
        return pd.DataFrame([{
            "Sıra": i['rank'], "Takım": i['team']['name'], "Puan": i['points'], "Form": i['form']
        } for i in standings])
    except:
        return pd.DataFrame({"Hata": ["Veri çekilemedi, lütfen anahtarı kontrol et."]})

# --- ARAYÜZ ---
st.title("🏆 TAM KAHİN GLOBAL AI")
st.write("### Kurucu: İsmail Enes Durmuş")

ligler = {
    "🇫🇷 Fransa Ligue 1": 61,
    "🇹🇷 Süper Lig": 203,
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League": 39,
    "🇪🇸 La Liga": 140,
    "🇪🇺 Şampiyonlar Ligi": 2
}

secim = st.sidebar.selectbox("Lig Seçin", list(ligler.keys()))
df = get_live_data(ligler[secim])

st.subheader(f"📊 {secim} Canlı Puan Durumu")
st.dataframe(df, use_container_width=True)

# --- VIP VE IBAN ---
st.sidebar.divider()
st.sidebar.markdown(f"""
### 💎 VIP ÜYELİK
**İSMAİL ENES DURMUŞ**
**IBAN:** TR68 0004 6004 9088 8000 1770 49
[WhatsApp Onay](https://wa.me/905388508757)
""")
