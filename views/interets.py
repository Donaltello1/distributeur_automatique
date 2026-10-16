import streamlit as st

from common import carte_resultat, en_tete, noter, titre
from operations import TAUX_ANNUEL, calculer_interets, formater

en_tete()
titre("Intérêts annuels", f"Ce que rapporte votre solde sur un an, au taux de {TAUX_ANNUEL} %.")

solde = st.session_state.solde
interets = calculer_interets(solde, TAUX_ANNUEL)
noter("interets", f"Intérêts calculés : {formater(interets)} FCFA", interets, une_fois=f"interets{solde}")

carte_resultat(
    "Intérêts gagnés sur 1 an (théorique)",
    f"{formater(interets)} FCFA",
    f"Solde × {TAUX_ANNUEL} / 100 = {formater(solde)} × {TAUX_ANNUEL} / 100",
)
