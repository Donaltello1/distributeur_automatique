"""Banque Baobab — distributeur automatique (Streamlit multipages).

Lancer avec :  streamlit run Distributor_app.py
"""
import streamlit as st

from common import init_state

st.set_page_config(page_title="Banque Baobab", page_icon="B", layout="centered")
init_state()

pages = [
    st.Page("views/accueil.py", title="Accueil", default=True),
    st.Page("views/consulter.py", title="Consulter le solde", url_path="solde"),
    st.Page("views/deposer.py", title="Déposer", url_path="deposer"),
    st.Page("views/retirer.py", title="Retirer", url_path="retirer"),
    st.Page("views/interets.py", title="Intérêts", url_path="interets"),
    st.Page("views/historique.py", title="Historique", url_path="historique"),
    st.Page("views/quitter.py", title="Quitter", url_path="quitter"),
]
st.navigation(pages, position="hidden").run()
