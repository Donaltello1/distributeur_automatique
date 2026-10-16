import streamlit as st

from common import afficher_message, en_tete, noter, titre
from operations import deposer_argent, formater

en_tete()
titre("Déposer de l'argent", "Le montant doit être strictement positif.")
afficher_message()


def choisir(valeur):
    st.session_state.montant_depot = valeur


with st.container(border=True):
    montant = st.number_input("Montant à déposer (FCFA)", min_value=0, step=1000, key="montant_depot")
    for col, v in zip(st.columns(4), [10_000, 25_000, 50_000, 100_000]):
        col.button(formater(v), key=f"d{v}", on_click=choisir, args=(v,), use_container_width=True)
    valider = st.button("Déposer", type="primary", use_container_width=True)

if valider:
    try:
        st.session_state.solde = deposer_argent(st.session_state.solde, montant)
    except ValueError as e:
        st.error(str(e))
    else:
        noter("depot", f"Dépôt : +{formater(montant)} FCFA", montant)
        st.session_state.message = f"Dépôt de {formater(montant)} FCFA effectué. Nouveau solde : {formater(st.session_state.solde)} FCFA."
        st.rerun()  # rafraîchit le solde affiché dans l'en-tête
