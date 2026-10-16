@echo off
rem Double-cliquez sur ce fichier pour ouvrir l'application dans le navigateur.
cd /d "%~dp0"
title Banque Baobab
python -m streamlit run Distributor_app.py --server.headless false
if errorlevel 1 (
    echo.
    echo Le lancement a echoue. Verifiez que Python et streamlit sont installes : pip install streamlit
    pause
)
