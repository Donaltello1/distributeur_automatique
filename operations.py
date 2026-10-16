"""Logique métier du distributeur (fonctions demandées par l'exercice)."""

TAUX_ANNUEL = 3
SOLDE_INITIAL = 150_000


def formater(montant):
    """150000 -> '150 000' (espace insécable pour éviter les retours à la ligne)."""
    return f"{montant:,.0f}".replace(",", " ")


def consulter_solde(solde):
    """Retourne le message affichant le solde actuel."""
    return f"Votre solde actuel est de {formater(solde)} FCFA."


def deposer_argent(solde, montant):
    """Retourne le nouveau solde après dépôt ; refuse un montant non strictement positif."""
    if montant <= 0:
        raise ValueError("Le montant à déposer doit être strictement positif.")
    return solde + montant


def retirer_argent(solde, montant):
    """Retourne le solde actualisé après retrait ; refuse un montant invalide ou trop élevé."""
    if montant <= 0:
        raise ValueError("Le montant à retirer doit être strictement positif.")
    if montant > solde:
        raise ValueError("Montant supérieur au solde disponible.")
    return solde - montant


def calculer_interets(solde, taux):
    """Retourne les intérêts annuels théoriques : solde * taux / 100."""
    return solde * taux / 100


def afficher_historique(historique):
    """Retourne le texte de l'historique (une ligne par opération)."""
    lignes = ["========== HISTORIQUE =========="]
    for operation in historique:
        lignes.append(operation["texte"])
    return "\n".join(lignes)
