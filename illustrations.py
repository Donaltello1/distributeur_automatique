"""Illustrations et icônes vectorielles (SVG) — aplats, formes géométriques, mêmes couleurs que le thème."""

TERRA, TINT, CREAM, SAND, INK, GREY, GREEN, RED = (
    "#D97757", "#FBEBE3", "#F5F4ED", "#EDEADF", "#141413", "#6B6A63", "#5E8B5A", "#B5483A",
)

_STROKE = f'fill="none" stroke="{TERRA}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'

# Pictos 48x48 : disque teinté + pictogramme en traits arrondis + petit aplat décoratif
_PICTOS = {
    "solde": (
        f'<path d="M10 24C14 16 19 13 24 13s10 3 14 11c-4 8-9 11-14 11S14 32 10 24z" {_STROKE}/>'
        f'<circle cx="24" cy="24" r="4.5" fill="{TERRA}"/>'
    ),
    "depot": (
        f'<path d="M24 32V15M16 22l8-8 8 8" {_STROKE}/>'
        f'<path d="M14 35h20" {_STROKE}/>'
    ),
    "retrait": (
        f'<path d="M24 15v17M16 25l8 8 8-8" {_STROKE}/>'
        f'<path d="M14 13h20" {_STROKE}/>'
    ),
    "interets": (
        f'<circle cx="17" cy="17" r="4" {_STROKE}/><circle cx="31" cy="31" r="4" {_STROKE}/>'
        f'<path d="M33 13L15 35" {_STROKE}/>'
    ),
    "historique": (
        f'<path d="M15 16h18M15 24h18M15 32h11" {_STROKE}/>'
        f'<circle cx="34" cy="32" r="2.5" fill="{TERRA}"/>'
    ),
    "quitter": (
        f'<path d="M20 14h-6v20h6" {_STROKE}/><path d="M23 24h14M32 18l6 6-6 6" {_STROKE}/>'
    ),
}


def picto(nom, taille=52):
    """Icône ronde : fond teinté, pictogramme terracotta, petit satellite décoratif."""
    return (
        f'<svg width="{taille}" height="{taille}" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" role="img">'
        f'<circle cx="24" cy="24" r="23" fill="{TINT}"/>'
        f'<circle cx="40" cy="9" r="3.5" fill="{TERRA}" opacity=".35"/>'
        f'{_PICTOS[nom]}</svg>'
    )


def logo(taille=30):
    """Logo : baobab stylisé (tronc + couronne) dans un rond."""
    return (
        f'<svg width="{taille}" height="{taille}" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">'
        f'<circle cx="24" cy="24" r="23" fill="{TERRA}"/>'
        f'<path d="M20 40c1-6 1-9 0-13h8c-1 4-1 7 0 13z" fill="{CREAM}"/>'
        f'<path d="M10 24c0-5 5-9 14-9s14 4 14 9c0 3-3 4-6 3-3 2-7 2-8 0-3 1-6 1-8-1-3 1-6 0-6-2z" fill="{CREAM}"/>'
        f'</svg>'
    )


def heros():
    """Bandeau d'accueil : collines, baobab, distributeur et pièces — formes plates, palette du thème."""
    return f"""
<svg viewBox="0 0 800 190" width="100%" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Illustration : baobab et distributeur">
  <rect width="800" height="190" rx="22" fill="{TINT}"/>
  <circle cx="660" cy="52" r="30" fill="{TERRA}" opacity=".9"/>
  <path d="M0 150c90-40 170-40 270-10s190 30 290-12 160-30 240 6v56H0z" fill="{SAND}"/>
  <path d="M0 170c120-30 230-24 340-4s300 20 460-16v40H0z" fill="{TERRA}" opacity=".85"/>
  <!-- baobab -->
  <path d="M108 172c5-26 6-44 2-66h34c-4 22-3 40 2 66z" fill="{INK}"/>
  <path d="M60 104c-6-24 18-44 66-44s72 20 66 44c-4 14-22 14-34 6-12 12-34 12-44 0-14 8-50 12-54-6z" fill="{GREEN}"/>
  <circle cx="90" cy="86" r="5" fill="{CREAM}" opacity=".7"/><circle cx="150" cy="78" r="4" fill="{CREAM}" opacity=".7"/>
  <!-- distributeur -->
  <rect x="318" y="34" width="132" height="132" rx="16" fill="{INK}"/>
  <rect x="332" y="48" width="104" height="52" rx="8" fill="{CREAM}"/>
  <path d="M344 84l18-16 14 10 20-22 22 18" fill="none" stroke="{TERRA}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="332" y="112" width="48" height="10" rx="5" fill="{TERRA}"/>
  <rect x="332" y="132" width="104" height="22" rx="6" fill="{GREY}"/>
  <rect x="352" y="138" width="64" height="8" rx="4" fill="{CREAM}"/>
  <circle cx="414" cy="117" r="6" fill="{CREAM}"/>
  <!-- pièces -->
  <circle cx="520" cy="136" r="22" fill="{TERRA}"/><circle cx="520" cy="136" r="14" fill="none" stroke="{CREAM}" stroke-width="3"/>
  <circle cx="568" cy="150" r="16" fill="{TERRA}" opacity=".75"/><circle cx="568" cy="150" r="9" fill="none" stroke="{CREAM}" stroke-width="3"/>
  <circle cx="486" cy="112" r="12" fill="{CREAM}"/><circle cx="486" cy="112" r="6" fill="none" stroke="{TERRA}" stroke-width="3"/>
  <!-- billets -->
  <g transform="rotate(-8 700 140)"><rect x="650" y="118" width="96" height="52" rx="8" fill="{CREAM}" stroke="{INK}" stroke-width="3"/>
  <circle cx="698" cy="144" r="13" fill="{TERRA}"/><rect x="660" y="128" width="14" height="6" rx="3" fill="{GREY}"/><rect x="722" y="154" width="14" height="6" rx="3" fill="{GREY}"/></g>
</svg>"""


def deco_resultat():
    """Formes plates décoratives placées en coin des cartes de résultat."""
    return (
        f'<svg class="deco" width="120" height="70" viewBox="0 0 120 70" xmlns="http://www.w3.org/2000/svg">'
        f'<circle cx="100" cy="14" r="26" fill="{TERRA}" opacity=".18"/>'
        f'<circle cx="62" cy="52" r="12" fill="{TERRA}" opacity=".28"/>'
        f'<rect x="20" y="30" width="22" height="22" rx="6" fill="{TERRA}" opacity=".14" transform="rotate(18 31 41)"/>'
        f'</svg>'
    )
