"""État de session, thème (CSS) et éléments d'interface partagés."""
from datetime import datetime

import streamlit as st

from illustrations import deco_resultat, logo
from operations import SOLDE_INITIAL, formater

CSS = """
<style>
html, body, [class*="st-"], .stApp { font-family: "Segoe UI", system-ui, sans-serif; }
h1, h2, h3 { font-family: Georgia, "Times New Roman", serif !important; font-weight: 400 !important; }
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { display: none; }
.block-container { max-width: 880px; padding-top: 2.2rem; }
.brand { display: flex; align-items: center; gap: .6rem; font-family: Georgia, serif; font-weight: 700; font-size: 1.25rem; }
.brand svg { display: block; }
.topbar { display: flex; justify-content: space-between; align-items: center; }
.pill { background: #fff; border: 2px solid #141413; border-radius: 999px; box-shadow: 3px 3px 0 #D97757;
        padding: .3rem 1rem; font-size: .88rem; color: #6B6A63; }
.pill b { color: #141413; }
.title { text-align: center; font-family: Georgia, serif; font-size: 2.1rem; margin: 1.6rem 0 .3rem; }
.subtitle { text-align: center; color: #6B6A63; margin-bottom: 1.8rem; }
.card-icon { display: flex; justify-content: center; margin: .2rem auto .6rem; }
.hero { margin: 1.4rem 0 .4rem; border-radius: 22px; overflow: hidden; line-height: 0; }
.card-title { text-align: center; font-weight: 600; }
.card-desc { text-align: center; color: #6B6A63; font-size: .85rem; margin-bottom: .6rem; }
[data-testid="stVerticalBlockBorderWrapper"] { background: #fff; border: 2px solid #141413 !important; border-radius: 18px;
    box-shadow: 4px 4px 0 #E3DFD0; }
[data-testid="stVerticalBlockBorderWrapper"]:hover { box-shadow: 4px 4px 0 #D97757; }
.result { position: relative; overflow: hidden; background: #FBEBE3; border: 2px solid #141413; border-radius: 18px;
          box-shadow: 4px 4px 0 #D97757; text-align: center; padding: 1.4rem 1rem; }
.result .deco { position: absolute; right: 0; top: 0; }
.result .label { color: #6B6A63; font-size: .9rem; }
.result .value { font-family: Georgia, serif; font-size: 2.6rem; color: #D97757; line-height: 1.2; }
.result .formula { font-family: Consolas, monospace; color: #6B6A63; font-size: .9rem; }
.op { display: flex; justify-content: space-between; align-items: center; padding: .7rem 0; border-bottom: 1px solid #E3DFD0; }
.op:last-child { border-bottom: none; }
.op .dot { display: inline-block; width: 11px; height: 11px; border-radius: 50%; margin-right: .8rem; }
.op small { color: #6B6A63; display: block; margin-left: 1.55rem; }
.pos { color: #5E8B5A; font-weight: 600; } .neg { color: #B5483A; font-weight: 600; } .acc { color: #D97757; font-weight: 600; }
.stButton > button { border-radius: 12px; border: 2px solid #141413; font-weight: 600; box-shadow: 2px 2px 0 #141413; }
.stButton > button[kind="tertiary"] { border: none; box-shadow: none; }
</style>
"""


def init_state():
    if "solde" not in st.session_state:
        st.session_state.solde = SOLDE_INITIAL
        st.session_state.historique = []   # liste de dicts {type, texte, montant}
        st.session_state.deja_note = set()  # évite de re-journaliser à chaque rerun


def noter(type_, texte, montant=None, une_fois=None):
    """Ajoute une opération à l'historique (une seule fois par visite si `une_fois` est donné)."""
    if une_fois:
        if une_fois in st.session_state.deja_note:
            return
        st.session_state.deja_note.add(une_fois)
    st.session_state.historique.append(
        {"type": type_, "texte": texte, "montant": montant, "heure": datetime.now().strftime("%H:%M:%S")}
    )


def en_tete(retour=True):
    st.markdown(CSS, unsafe_allow_html=True)
    st.html(
        f'<div class="topbar"><div class="brand">{logo()}Banque Baobab</div>'
        f'<div class="pill">Solde <b>{formater(st.session_state.solde)} FCFA</b></div></div>'
    )
    if retour:
        if st.button("← Retour au menu", type="tertiary"):
            st.switch_page("views/accueil.py")


def carte_resultat(label, valeur, formule=""):
    """Carte de résultat plate avec décor vectoriel."""
    formule_html = f'<div class="formula">{formule}</div>' if formule else ""
    st.html(
        f'<div class="result">{deco_resultat()}<div class="label">{label}</div>'
        f'<div class="value">{valeur}</div>{formule_html}</div>'
    )


def titre(texte, sous_titre=""):
    st.markdown(f'<div class="title">{texte}</div><div class="subtitle">{sous_titre}</div>', unsafe_allow_html=True)


def afficher_message():
    """Affiche (une fois) le message de succès mis de côté avant un st.rerun()."""
    message = st.session_state.pop("message", None)
    if message:
        st.success(message)


def bouton_recu(cle):
    """Bouton de téléchargement du reçu PDF (dépôts, retraits, intérêts)."""
    from recu import generer_recu, operations_du_recu

    historique = st.session_state.historique
    if not operations_du_recu(historique):
        st.caption("Le reçu PDF sera disponible après un dépôt, un retrait ou un calcul d'intérêts.")
        return
    st.download_button(
        "Télécharger le reçu (PDF)",
        data=generer_recu(historique, st.session_state.solde),
        file_name=f"recu_banque_baobab_{datetime.now():%Y%m%d_%H%M%S}.pdf",
        mime="application/pdf",
        type="primary",
        key=cle,
    )
