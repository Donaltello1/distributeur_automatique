# Banque Baobab — Distributeur automatique

Application Streamlit multipages qui simule un distributeur de billets (solde initial 150 000 FCFA) :
consulter le solde, déposer, retirer, calculer les intérêts annuels (3 %), consulter l'historique
et **télécharger un reçu PDF** (dépôts, retraits, intérêts).

## Structure

```
Distributor_app.py      point d'entrée (navigation)
operations.py           fonctions de l'exercice (solde, dépôt, retrait, intérêts, historique)
common.py               état de session, thème CSS, en-tête, bouton de reçu
illustrations.py        icônes et illustrations vectorielles (SVG)
recu.py                 génération du reçu PDF (fpdf2)
views/                  une page par opération
.streamlit/config.toml  thème (couleurs)
requirements.txt        dépendances
```

## Lancer en local

```bash
pip install -r requirements.txt
streamlit run Distributor_app.py
```

Sous Windows, double-cliquer sur `Lancer_Banque_Baobab.bat`.

## Déployer sur Streamlit Community Cloud
1. Mettre ce dossier dans un dépôt GitHub (`requirements.txt` à la racine du dépôt).
2. Sur https://share.streamlit.io : *Create app* → choisir le dépôt et la branche.
3. *Main file path* : `Distributor_app.py` (préfixer par le sous-dossier si le projet n'est pas à la racine du dépôt).
4. *Advanced settings* → Python 3.12 ou 3.13 → *Deploy*.

## Remarque
Le solde et l'historique sont conservés dans la session du navigateur (`st.session_state`) :
ils repartent de zéro quand la page est rechargée ou qu'une autre personne ouvre l'application.
