import streamlit as st

from common import bouton_recu, en_tete, titre
from operations import formater

en_tete(retour=False)
titre("Merci de votre visite", "Votre session est terminée. À bientôt à la Banque Baobab !")

with st.container(border=True):
    st.metric("Solde final", f"{formater(st.session_state.solde)} FCFA")
    st.caption(f"{len(st.session_state.historique)} opération(s) réalisée(s) pendant la session.")
    bouton_recu("recu_quitter")
    if st.button("Démarrer une nouvelle session", type="primary", use_container_width=True):
        for cle in list(st.session_state.keys()):
            del st.session_state[cle]
        st.switch_page("views/accueil.py")
