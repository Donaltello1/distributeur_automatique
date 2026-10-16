import streamlit as st

from common import carte_resultat, en_tete, noter, titre
from operations import consulter_solde, formater

en_tete()
titre("Consulter le solde", "Le montant actuellement disponible sur votre compte.")
noter("consultation", "Consultation du solde", une_fois="consultation")

carte_resultat("Solde disponible", f"{formater(st.session_state.solde)} FCFA")
st.caption(consulter_solde(st.session_state.solde))
