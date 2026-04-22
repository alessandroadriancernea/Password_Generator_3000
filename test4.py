import streamlit as st
import random
import time

# --- CONFIGURAZIONE REALE ---
st.set_page_config(page_title="👑 Roulette Imperiale WOW", layout="wide")

# --- CSS IMPERIALE (ORO NEON E MARMO) ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle, #1a472a 0%, #000000 100%);
    }
    
    /* Titolo Imperiale */
    .imperial-title {
        color: #FFD700;
        text-shadow: 0 0 20px #FFD700, 0 0 40px #B8860B;
        font-size: 60px !important;
        font-family: 'Garamond', serif;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Box Tesoro */
    .treasure-box {
        border: 3px solid #FFD700;
        background: rgba(0,0,0,0.6);
        padding: 20px;
        border-radius: 25px;
        box-shadow: 0 0 25px #FFD700;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Ruota Animata */
    .wheel-glow {
        font-size: 120px;
        text-shadow: 0 0 30px gold;
        display: block;
        margin: auto;
        animation: spin 3s linear infinite;
    }
    
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* Tappeto di Puntata */
    .betting-carpet {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 20px 0;
    }

    /* Bottoni Custom */
    .stButton>button {
        background: linear-gradient(145deg, #FFD700, #B8860B) !important;
        color: black !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        border: 2px solid white !important;
        box-shadow: 0 0 15px gold !important;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.1) rotate(2deg);
        box-shadow: 0 0 40px gold !important;
    }

    /* Numero Uscito */
    .result-circle {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
        font-weight: bold;
        border: 5px solid gold;
        margin: auto;
        box-shadow: 0 0 20px gold;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGICA DEL DESTINO ---
ROSSI = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

if 'tesoro' not in st.session_state:
    st.session_state.tesoro = 5000
if 'spinning' not in st.session_state:
    st.session_state.spinning = False
if 'ultimo_n' not in st.session_state:
    st.session_state.ultimo_n = None

# --- UI PRINCIPALE ---
st.markdown("<h1 class='imperial-title'>✨ ROULETTE IMPERIALE ✨</h1>", unsafe_allow_html=True)

# Layout: Sinistra (Puntata) | Centro (Ruota) | Destra (Risultato)
col_bet, col_wheel, col_res = st.columns([1, 1, 1])

with col_bet:
    st.markdown(f"<div class='treasure-box'><h3>💰 ORO REALE</h3><h1 style='color:gold;'>{st.session_state.tesoro}</h1></div>", unsafe_allow_html=True)
    scelta_colore = st.selectbox("SCEGLI IL TUO DESTINO:", ["ROSSO 🔴", "NERO ⚫", "ZERO 🟢"])
    puntata = st.number_input("QUANTO ORO OFFRI?", 50, st.session_state.tesoro, 100, step=50)

with col_wheel:
    placeholder_ruota = st.empty()
    if not st.session_state.spinning:
        placeholder_ruota.markdown("<div style='text-align:center;'><span style='font-size:150px;'>🎡</span></div>", unsafe_allow_html=True)
    else:
        placeholder_ruota.markdown("<div style='text-align:center;' class='wheel-glow'>🎡</div>", unsafe_allow_html=True)

with col_res:
    if st.session_state.ultimo_n is not None:
        n = st.session_state.ultimo_n
        colore_bg = "#b30000" if n in ROSSI else "#1a1a1a"
        if n == 0: colore_bg = "#008000"
        st.markdown(f"<h3>ESTRATTO:</h3><div class='result-circle' style='background:{colore_bg};'>{n}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='opacity:0.5;'>IN ATTESA...</h3>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- IL GRANDE LANCIO ---
if st.button("🔮 LANCIA LA SFERA DEL DESTINO 🔮"):
    if st.session_state.tesoro >= puntata:
        st.session_state.spinning = True
        st.rerun() # Forza il reload per l'animazione
        
# Questo blocco gira solo se abbiamo appena cliccato
if st.session_state.spinning:
    # Simuliamo il tempo della ruota
    time.sleep(2) 
    
    risultato = random.randint(0, 36)
    st.session_state.ultimo_n = risultato
    st.session_state.spinning = False
    
    # Calcolo Vincita
    vinto = False
    moltiplicatore = 2
    
    if scelta_colore == "ROSSO 🔴" and risultato in ROSSI: vinto = True
    elif scelta_colore == "NERO ⚫" and risultato not in ROSSI and risultato != 0: vinto = True
    elif scelta_colore == "ZERO 🟢" and risultato == 0: 
        vinto = True
        moltiplicatore = 36 # Lo zero paga tantissimo!

    if vinto:
        oro_vinto = puntata * moltiplicatore
        st.session_state.tesoro += oro_vinto
        st.success(f"🎊 GLORIA AL RE! HAI VINTO {oro_vinto} ORO! 🎊")
        st.balloons()
    else:
        st.session_state.tesoro -= puntata
        st.error(f"💀 IL DESTINO È STATO CRUDELE. HAI PERSO {puntata} ORO.")
    
    st.rerun()

st.markdown("<p style='text-align:right; color:gold; font-size:12px;'>IMPERATOR 2K26 - 67</p>", unsafe_allow_html=True)
