"""Génération du reçu PDF des opérations (dépôts, retraits, intérêts)."""
from datetime import datetime

from fpdf import FPDF

from operations import formater

TERRA, TINT, CREAM, INK, GREY, GREEN, RED = (
    (217, 119, 87), (251, 235, 227), (245, 244, 237), (20, 20, 19), (107, 106, 99), (94, 139, 90), (181, 72, 58),
)
TYPES_RECU = {"depot": "Dépôt", "retrait": "Retrait", "interets": "Intérêts calculés"}


def _txt(texte):
    """Les polices PDF de base n'acceptent que le latin-1 : on neutralise le reste."""
    return str(texte).replace(" ", " ").encode("latin-1", "replace").decode("latin-1")


def operations_du_recu(historique):
    """Garde uniquement dépôts, retraits et intérêts (les consultations n'ont pas de montant)."""
    return [op for op in historique if op["type"] in TYPES_RECU]


class _Recu(FPDF):
    def footer(self):
        self.set_y(-18)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*GREY)
        self.cell(0, 5, _txt("Banque Baobab - reçu généré automatiquement, sans valeur légale (projet pédagogique)."),
                  align="C")


def _logo(pdf, x, y, d=14):
    """Logo vectoriel : rond terracotta + baobab crème."""
    pdf.set_fill_color(*TERRA)
    pdf.ellipse(x, y, d, d, style="F")
    pdf.set_fill_color(*CREAM)
    pdf.rect(x + d * 0.43, y + d * 0.5, d * 0.14, d * 0.32, style="F")
    pdf.ellipse(x + d * 0.18, y + d * 0.2, d * 0.64, d * 0.4, style="F")


def generer_recu(historique, solde_final):
    """Retourne le PDF (bytes) du reçu des opérations de la session."""
    operations = operations_du_recu(historique)
    depots = sum(op["montant"] for op in operations if op["type"] == "depot")
    retraits = sum(op["montant"] for op in operations if op["type"] == "retrait")
    interets = [op for op in operations if op["type"] == "interets"]
    solde_initial = solde_final - depots + retraits
    maintenant = datetime.now()

    pdf = _Recu(format="A4")
    pdf.set_auto_page_break(auto=True, margin=22)
    pdf.add_page()
    pdf.set_margins(18, 18, 18)

    # Bandeau d'en-tête
    pdf.set_fill_color(*TINT)
    pdf.rect(0, 0, 210, 44, style="F")
    pdf.set_fill_color(*TERRA)
    pdf.rect(0, 44, 210, 1.6, style="F")
    _logo(pdf, 18, 14)
    pdf.set_xy(36, 14)
    pdf.set_font("Times", "B", 20)
    pdf.set_text_color(*INK)
    pdf.cell(100, 8, "Banque Baobab")
    pdf.set_xy(36, 23)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*GREY)
    pdf.cell(100, 6, _txt("Reçu des opérations - distributeur automatique"))
    pdf.set_xy(120, 14)
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*INK)
    pdf.cell(72, 6, _txt(f"Reçu n° {maintenant:%Y%m%d-%H%M%S}"), align="R")
    pdf.set_xy(120, 21)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*GREY)
    pdf.cell(72, 6, _txt(f"Émis le {maintenant:%d/%m/%Y à %H:%M}"), align="R")

    # Tableau des opérations
    pdf.set_y(58)
    largeurs = (14, 26, 70, 62)
    pdf.set_fill_color(*INK)
    pdf.set_text_color(*CREAM)
    pdf.set_font("Helvetica", "B", 10)
    for titre, w, al in zip(("N°", "Heure", "Opération", "Montant (FCFA)"), largeurs, ("C", "C", "L", "R")):
        pdf.cell(w, 9, _txt(titre), fill=True, align=al, border=0)
    pdf.ln(9)

    if not operations:
        pdf.set_text_color(*GREY)
        pdf.set_font("Helvetica", "I", 10)
        pdf.cell(sum(largeurs), 14, _txt("Aucune opération enregistrée pour cette session."), align="C")
        pdf.ln(14)
    for i, op in enumerate(operations, 1):
        pdf.set_fill_color(*(CREAM if i % 2 else (255, 255, 255)))
        signe, couleur = {"depot": ("+", GREEN), "retrait": ("-", RED), "interets": ("", TERRA)}[op["type"]]
        pdf.set_text_color(*INK)
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(largeurs[0], 9, str(i), fill=True, align="C")
        pdf.cell(largeurs[1], 9, op.get("heure", "-"), fill=True, align="C")
        pdf.cell(largeurs[2], 9, _txt(TYPES_RECU[op["type"]]), fill=True)
        pdf.set_text_color(*couleur)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(largeurs[3], 9, _txt(f"{signe}{formater(op['montant'])}"), fill=True, align="R")
        pdf.ln(9)

    # Récapitulatif
    pdf.ln(8)
    lignes = [
        ("Solde initial", formater(solde_initial), INK),
        ("Total des dépôts", "+" + formater(depots), GREEN),
        ("Total des retraits", "-" + formater(retraits), RED),
    ]
    for label, valeur, couleur in lignes:
        pdf.set_x(18)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(*GREY)
        pdf.cell(110, 7, _txt(label))
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*couleur)
        pdf.cell(62, 7, _txt(valeur + " FCFA"), align="R")
        pdf.ln(7)

    pdf.ln(2)
    pdf.set_fill_color(*TINT)
    pdf.set_draw_color(*INK)
    pdf.set_line_width(0.5)
    pdf.set_x(18)
    pdf.set_font("Times", "B", 14)
    pdf.set_text_color(*INK)
    pdf.cell(110, 13, _txt("  Solde final"), fill=True, border="LTB")
    pdf.set_text_color(*TERRA)
    pdf.cell(62, 13, _txt(formater(solde_final) + " FCFA  "), fill=True, align="R", border="RTB")
    pdf.ln(18)

    if interets:
        pdf.set_x(18)
        pdf.set_font("Helvetica", "I", 9)
        pdf.set_text_color(*GREY)
        pdf.multi_cell(
            172, 5,
            _txt("Les intérêts sont un calcul annuel théorique (solde x 3 / 100) : "
                 "ils ne sont pas ajoutés au solde et n'entrent pas dans les totaux ci-dessus."),
        )
    return bytes(pdf.output())
