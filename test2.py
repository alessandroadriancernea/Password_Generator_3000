import streamlit as st
import random
import time

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Las Vegas Slot 2K26", layout="centered")

# --- CSS LUXURY SLOT ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #1a0033;
        background-image: radial-gradient(circle, #4b0082 0%, #1a0033 100%);
    }
    [data-testid="stVerticalBlock"] {
        background: rgba(0, 0, 0, 0.5);
        padding: 40px;
        border-radius: 30px;
        border: 5px solid #ffd700;
        text-align: center;
    }
    .slot-machine {
        display: flex;
        justify-content: center;
        gap: 20px;
        padding: 20px;
    }
    .reel {
        background: white;
        color: black !important;
        font-size: 80px;
        width: 120px;
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        border: 4px solid #d4af37;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
    }
    .stButton>button {
        background: linear-gradient(to bottom, #ff4b1f, #ff9068) !important;
        color: white !important;
        font-size: 25px !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        border-radius: 30px !important;
        border: none !important;
        box-shadow: 0 5px 15px rgba(255, 75, 31, 0.4);
    }
    h1 { color: #ffd700 !important; text-shadow: 2px 2px 10px gold !important; }
</style>
""", unsafe_allow_html=True)

# --- LOGICA SLOT ---
SIMBOLI = ['🍒', '🍋', '🔔', '💎', '7️⃣', '🍀']

if 'rulli' not in st.session_state:
    st.session_state.rulli = ['🍒', '🍒', '🍒']
if 'portafoglio' not in st.session_state:
    st.session_state.portafoglio = 1000

st.title("🎰 MEGA SLOT 2K26")
st.write(f"### 💰 Portafoglio: ${st.session_state.portafoglio}")

# --- AREA RULLI ---
placeholder = st.empty()

def mostra_rulli(r1, r2, r3):
    placeholder.markdown(f"""
    <div class="slot-machine">
        <div class="reel">{r1}</div>
        <div class="reel">{r2}</div>
        <div class="reel">{r3}</div>
    </div>
    """, unsafe_allow_html=True)

# Mostra lo stato iniziale
mostra_rulli(*st.session_state.rulli)

# --- AZIONE ---
if st.button("TIRA LA LEVA! 🕹️"):
    if st.session_state.portafoglio >= 10:
        st.session_state.portafoglio -= 10
        
        # Effetto animazione "finta"
        for _ in range(10):
            temp_rulli = [random.choice(SIMBOLI) for _ in range(3)]
            mostra_rulli(*temp_rulli)
            time.sleep(0.1)
        
        # Risultato finale
        st.session_state.rulli = [random.choice(SIMBOLI) for _ in range(3)]
        mostra_rulli(*st.session_state.rulli)
        
        # Controllo vincita
        r1, r2, r3 = st.session_state.rulli
        if r1 == r2 == r3:
            vincita = 500 if r1 == '7️⃣' else 100
            st.session_state.portafoglio += vincita
            st.success(f"JACKPOT! Hai vinto ${vincita}! 🎉")
            st.balloons()
        elif r1 == r2 or r2 == r3 or r1 == r3:
            st.session_state.portafoglio += 20
            st.info("Piccola vincita! +$20 💸")
        else:
            st.error("Ritenta, sarai più fortunato! 😜")
        
        st.rerun()
    else:
        st.warning("Sei al verde! Clicca Reset per ricominciare.")

if st.button("RICARICA 🔄"):
    st.session_state.portafoglio = 1000
    st.rerun()

st.markdown("<p style='text-align:right; font-size:12px; color: grey;'>v. Slot - 67</p>", unsafe_allow_html=True)