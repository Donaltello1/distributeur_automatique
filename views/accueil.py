import streamlit as st

from common import en_tete, titre
from illustrations import heros, picto

en_tete(retour=False)
st.session_state.deja_note = set()  # nouvelle visite du menu : on réautorise la journalisation
st.html(f'<div class="hero">{heros()}</div>')
titre("Bonjour, que souhaitez-vous faire ?", "Choisissez une opération pour continuer.")

CARTES = [
    ("solde", "Consulter le solde", "Voir le montant disponible", "views/consulter.py"),
    ("depot", "Déposer", "Ajouter de l'argent", "views/deposer.py"),
    ("retrait", "Retirer", "Retirer des FCFA", "views/retirer.py"),
    ("interets", "Intérêts", "Intérêts annuels à 3 %", "views/interets.py"),
    ("historique", "Historique", "Opérations de la session", "views/historique.py"),
    ("quitter", "Quitter", "Terminer la session", "views/quitter.py"),
]

for ligne in range(2):
    colonnes = st.columns(3)
    for col, (icone, nom, desc, page) in zip(colonnes, CARTES[ligne * 3 : ligne * 3 + 3]):
        with col.container(border=True):
            st.html(
                f'<div class="card-icon">{picto(icone)}</div><div class="card-title">{nom}</div>'
                f'<div class="card-desc">{desc}</div>'
            )
            if st.button("Ouvrir", key=f"btn_{nom}", use_container_width=True):
                st.switch_page(page)
