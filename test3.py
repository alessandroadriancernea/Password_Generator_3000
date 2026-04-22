import streamlit as st
import random

# --- CONFIGURAZIONE E STILE IMPERIALE ---
st.set_page_config(page_title="Poker Royal 2K26", layout="wide")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
        background-image: radial-gradient(circle, #1a1a00 0%, #000000 100%);
    }
    h1, h2, h3, p, span {
        color: #FFD700 !important;
        text-shadow: 0 0 15px #FFD700, 0 0 30px #B8860B !important;
        font-family: 'Garamond', serif !important;
        text-align: center;
    }
    [data-testid="stVerticalBlock"] {
        background: rgba(30, 30, 30, 0.9);
        padding: 40px;
        border-radius: 60px;
        border: 5px solid #FFD700;
        box-shadow: 0 0 50px #B8860B;
    }
    .card {
        background: white;
        color: black !important;
        padding: 15px;
        border-radius: 15px;
        font-size: 35px;
        border: 3px solid #D4AF37;
        box-shadow: 0 0 20px #FFD700;
        display: inline-block;
        margin: 10px;
        width: 85px;
        text-shadow: none !important;
    }
    .wallet-box {
        border: 4px ridge #FFD700;
        background: linear-gradient(145deg, #222, #000);
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 0 20px gold;
    }
    .stButton>button {
        background: linear-gradient(to bottom, #FFD700, #B8860B) !important;
        color: black !important;
        font-weight: 900 !important;
        border-radius: 30px !important;
        box-shadow: 0 0 15px #FFD700 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGICA ---
def crea_mazzo():
    v = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    s = ['♠️', '♥️', '♦️', '♣️']
    m = [val + sem for val in v for sem in s]
    random.shuffle(m)
    return m

if 'poker_step' not in st.session_state:
    st.session_state.poker_step = "PRE-FLOP"
    st.session_state.mazzo = crea_mazzo()
    st.session_state.player_hand = [st.session_state.mazzo.pop(), st.session_state.mazzo.pop()]
    st.session_state.community_cards = []
    st.session_state.pot = 0
    if 'wallet' not in st.session_state: st.session_state.wallet = 5000

def mostra_carta(carta):
    color = "#FF0000" if ('♥️' in carta or '♦️' in carta) else "#000000"
    return f'<div class="card" style="color: {color} !important;">{carta}</div>'

# --- INTERFACCIA ---
st.markdown("<h1>👑 POKER DEL RE 👑</h1>", unsafe_allow_html=True)

# Portafoglio e Piatto
c_w1, c_w2 = st.columns(2)
with c_w1:
    st.markdown(f'<div class="wallet-box"><h3>💰 PORTAFOGLIO REALE</h3><h2>${st.session_state.wallet}</h2></div>', unsafe_allow_html=True)
with c_w2:
    st.markdown(f'<div class="wallet-box"><h3>🏺 PIATTO D\'ORO</h3><h2>${st.session_state.pot}</h2></div>', unsafe_allow_html=True)

# Board
st.markdown(f"## 🏟️ TAVOLO: {st.session_state.poker_step}")
board_html = '<div style="text-align: center;">'
for c in st.session_state.community_cards: board_html += mostra_carta(c)
for _ in range(5 - len(st.session_state.community_cards)):
    board_html += '<div class="card" style="background: rgba(255,215,0,0.1); border: 2px dashed gold; color: gold !important;">?</div>'
st.markdown(board_html + '</div>', unsafe_allow_html=True)

# Giocatore
st.markdown("<br>## 🔱 LE TUE CARTE", unsafe_allow_html=True)
hand_html = '<div style="text-align: center;">'
for c in st.session_state.player_hand: hand_html += mostra_carta(c)
st.markdown(hand_html + '</div>', unsafe_allow_html=True)

# --- CONTROLLI ---
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

if st.session_state.poker_step != "RISULTATO":
    if c1.button("PUNTA $200 ORO 🏺"):
        if st.session_state.wallet >= 200:
            st.session_state.wallet -= 200
            st.session_state.pot += 200
            if st.session_state.poker_step == "PRE-FLOP":
                st.session_state.community_cards = [st.session_state.mazzo.pop() for _ in range(3)]
                st.session_state.poker_step = "FLOP"
            elif st.session_state.poker_step == "FLOP":
                st.session_state.community_cards.append(st.session_state.mazzo.pop()); st.session_state.poker_step = "TURN"
            elif st.session_state.poker_step == "TURN":
                st.session_state.community_cards.append(st.session_state.mazzo.pop()); st.session_state.poker_step = "RIVER"
            elif st.session_state.poker_step == "RIVER":
                st.session_state.poker_step = "RISULTATO"
            st.rerun()
        else: st.error("NON HAI PIÙ ORO, RE!")

    if c2.button("RITIRATA (FOLD) 🏃"):
        st.session_state.poker_step = "PERSO"
        st.rerun()

if c3.button("NUOVA MANO 🔄"):
    del st.session_state.poker_step
    st.rerun()

# --- VERDETTO FINALE ---
if st.session_state.poker_step == "RISULTATO":
    # Simulazione vittoria 50/50 per semplicità
    if random.random() > 0.4:
        vincita = st.session_state.pot * 2
        st.session_state.wallet += vincita
        st.markdown(f"<h1 style='color: #00FF00 !important; font-size: 60px;'>✨ HAI VINTO ${vincita}! ✨</h1>", unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown("<h1 style='color: #FF0000 !important; font-size: 60px;'>💀 IL BANCO TI HA DERUBATO! 💀</h1>", unsafe_allow_html=True)
    st.session_state.pot = 0

if st.session_state.poker_step == "PERSO":
    st.markdown("<h1 style='color: #FF4500 !important;'>🏳️ TI SEI ARRESO!</h1>", unsafe_allow_html=True)
    st.session_state.pot = 0

st.markdown("<p style='text-align:right; color:gold;'>67</p>", unsafe_allow_html=True)