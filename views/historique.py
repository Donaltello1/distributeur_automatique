import streamlit as st

from common import bouton_recu, en_tete, titre

en_tete()
titre("Historique", "Toutes les opérations de la session.")

COULEURS = {"depot": ("#5E8B5A", "pos"), "retrait": ("#B5483A", "neg"), "interets": ("#D97757", "acc")}
historique = st.session_state.historique

if not historique:
    st.info("Aucune opération pour le moment.")
else:
    lignes = ""
    for i, op in enumerate(historique, 1):
        couleur, classe = COULEURS.get(op["type"], ("#6B6A63", ""))
        nom, _, montant = op["texte"].partition(" : ")
        lignes += (
            f'<div class="op"><div><span class="dot" style="background:{couleur}"></span><b>{nom}</b>'
            f'<small>Opération n°{i}</small></div><span class="{classe}">{montant}</span></div>'
        )
    with st.container(border=True):
        st.markdown(lignes, unsafe_allow_html=True)
    gauche, droite = st.columns(2)
    with gauche:
        bouton_recu("recu_historique")
    with droite:
        if st.button("Effacer l'historique", use_container_width=True):
            st.session_state.historique = []
            st.rerun()
