import streamlit as st
import random

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Blackjack Luxury 2K26", layout="centered")

# --- CSS DEFINITIVO (BEAUTIFUL MODE) ---
st.markdown("""
<style>
    /* Sfondo Tavolo Verde Professionale */
    [data-testid="stAppViewContainer"] {
        background-color: #064222;
        background-image: radial-gradient(circle, #0a5c2f 0%, #064222 100%);
    }

    /* Contenitore Principale stile Tavolo */
    [data-testid="stVerticalBlock"] {
        background: rgba(0, 0, 0, 0.3);
        padding: 40px;
        border-radius: 50px;
        border: 4px solid #d4af37;
        box-shadow: 0px 0px 30px rgba(0,0,0,0.5);
    }

    /* Styling delle Carte */
    .card {
        background-color: white;
        color: black !important;
        padding: 10px 15px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 24px;
        border: 2px solid #ccc;
        box-shadow: 3px 3px 5px rgba(0,0,0,0.3);
        margin: 5px;
        display: inline-block;
    }

    /* Bottoni Dorati */
    .stButton>button {
        background-color: #d4af37 !important;
        color: #000 !important;
        font-weight: bold !important;
        border-radius: 20px !important;
        border: 2px solid #b8860b !important;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #ffd700 !important;
        transform: scale(1.05);
    }

    /* Testi */
    h1, h2, h3, p, span {
        color: #f1f1f1 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        font-family: 'Georgia', serif;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGICA DEL GIOCO ---
def crea_mazzo():
    v = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    s = ['♠️', '♥️', '♦️', '♣️']
    mazzo = [val + sem for val in v for sem in s]
    random.shuffle(mazzo)
    return mazzo

def valore_mano(mano):
    punti = 0
    assi = 0
    mappa = {v: int(v) if v.isdigit() else 10 for v in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']}
    mappa['A'] = 11
    for c in mano:
        val = c[:-2] if '10' not in c else '10'
        punti += mappa[val]
        if val == 'A': assi += 1
    while punti > 21 and assi:
        punti -= 10
        assi -= 1
    return punti

# --- STATO DEL GIOCO ---
if 'mazzo' not in st.session_state:
    st.session_state.mazzo = crea_mazzo()
    st.session_state.player = [st.session_state.mazzo.pop(), st.session_state.mazzo.pop()]
    st.session_state.dealer = [st.session_state.mazzo.pop(), st.session_state.mazzo.pop()]
    st.session_state.game_over = False

# --- UI ---
st.title("🎩 CASINÒ BLACKJACK 2K26")

# Visualizzazione Casa
st.markdown("### 🏦 BANCO")
dealer_html = ""
if st.session_state.game_over:
    for c in st.session_state.dealer:
        dealer_html += f'<div class="card">{c}</div>'
    st.markdown(dealer_html, unsafe_allow_html=True)
    st.write(f"Punteggio: **{valore_mano(st.session_state.dealer)}**")
else:
    dealer_html = f'<div class="card">{st.session_state.dealer[0]}</div><div class="card" style="background:#222; color:#222 !important;">?</div>'
    st.markdown(dealer_html, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Visualizzazione Giocatore
st.markdown("### 👤 VOSTRO GIOCO")
player_html = ""
for c in st.session_state.player:
    color = "red" if ('♥️' in c or '♦️' in c) else "black"
    player_html += f'<div class="card" style="color: {color} !important;">{c}</div>'
st.markdown(player_html, unsafe_allow_html=True)
st.write(f"Punteggio attuale: **{valore_mano(st.session_state.player)}**")

st.markdown("---")

# --- CONTROLLI ---
c1, c2, c3 = st.columns(3)

if not st.session_state.game_over:
    if c1.button("CHIEDI CARTA ➕"):
        st.session_state.player.append(st.session_state.mazzo.pop())
        if valore_mano(st.session_state.player) > 21:
            st.session_state.game_over = True
            st.rerun()
    
    if c2.button("STAI ✋"):
        st.session_state.game_over = True
        while valore_mano(st.session_state.dealer) < 17:
            st.session_state.dealer.append(st.session_state.mazzo.pop())
        st.rerun()

if c3.button("NUOVA MANO 🔄"):
    for k in list(st.session_state.keys()): del st.session_state[k]
    st.rerun()

# --- RISULTATO ---
if st.session_state.game_over:
    p, d = valore_mano(st.session_state.player), valore_mano(st.session_state.dealer)
    st.markdown("<br>", unsafe_allow_html=True)
    if p > 21:
        st.error("SBALLATO! La casa vince. 💸")
    elif d > 21 or p > d:
        st.success("VITTORIA! 🎉")
        st.balloons()
    elif p < d:
        st.error("IL BANCO VINCE. 🏛️")
    else:
        st.info("PAREGGIO (PUSH). 🤝")

st.markdown("<p style='text-align:right; font-size:12px; color: gold !important;'>v. 2.0 - 67</p>", unsafe_allow_html=True)