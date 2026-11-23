#!/usr/bin/env python3
"""Generate docs/legal/js/i18n.js from embedded translations."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).with_name("i18n.js")

LOCALES = [
    ("en", "English"),
    ("de", "Deutsch"),
    ("el", "Ελληνικά"),
    ("es", "Español"),
    ("fr", "Français"),
    ("it", "Italiano"),
    ("ja", "日本語"),
    ("ko", "한국어"),
    ("nl", "Nederlands"),
    ("pl", "Polski"),
    ("pt", "Português"),
    ("pt_BR", "Português (Brasil)"),
    ("th", "ไทย"),
    ("tr", "Türkçe"),
    ("zh", "中文（简体）"),
    ("zh_TW", "中文（繁體）"),
]


def ui(
    home,
    support,
    privacy,
    language,
    legal_support,
    public_pages,
    support_label,
    privacy_label,
    guide="Guide",
    guide_label="Guide:",
):
    return {
        "nav_home": home,
        "nav_support": support,
        "nav_privacy": privacy,
        "nav_guide": guide,
        "lang_label": language,
        "index_title": "ViewWeave — Legal",
        "privacy_title": "ViewWeave — Privacy Policy",
        "support_title": "ViewWeave — Support",
        "footer_copy": "© 2026 ViewWeave",
        "index_h1": legal_support,
        "index_lead": public_pages,
        "index_support_strong": support_label,
        "index_privacy_strong": privacy_label,
        "index_guide_strong": guide_label,
    }


def pack(ui_args, index_tag, privacy, support):
    return {
        "ui": ui(*ui_args),
        "index": {"tag": index_tag},
        "privacy": privacy,
        "support": support,
    }


def P(**k):
    return k


def S(**k):
    return k


T: dict[str, dict] = {}

T["en"] = pack(
    (
        "Home",
        "Support",
        "Privacy Policy",
        "Language",
        "Legal & support",
        "Public pages for App Store / Play listing.",
        "Support:",
        "Privacy:",
        "Guide",
        "Guide:",
    ),
    "Multi-camera filming on local Wi‑Fi — no cloud.",
    P(
        tag="Privacy Policy",
        h1="Privacy Policy",
        effective="Effective date: 15 November 2026",
        intro="This policy describes how the <strong>ViewWeave</strong> mobile app (“the App”) handles information. ViewWeave is a local multi-camera filming tool. It does <strong>not</strong> operate a ViewWeave cloud backend for your videos.",
        h2_1="1. Who we are",
        p_1='ViewWeave is published as an independent app (bundle ID <code>com.viewweave.app</code>). Contact: <a href="mailto:viewweave78@gmail.com">viewweave78@gmail.com</a>.',
        h2_2="2. Data the App stores on your device",
        li_2a="<strong>Videos and library metadata</strong> created by you (sessions, takes, edits) — stored in the app’s private documents / media folders on the device.",
        li_2b="<strong>License state</strong> (trial / Free / Basic) in a local file on the device.",
        li_2c="<strong>Preferences</strong> such as export settings, also stored locally.",
        p_2="Uninstalling the App deletes this sandbox data. We do not receive a copy of your videos on ViewWeave servers.",
        h2_3="3. Local network",
        p_3="When you run a multi-phone session, devices communicate on your <strong>local Wi‑Fi or hotspot</strong> (HTTP on the LAN) to sync capture and transfer rushes to the Master. This traffic stays on your network; it is not uploaded to a ViewWeave cloud.",
        h2_4="4. Purchases (Basic)",
        p_4="Unlocking <strong>Basic</strong> uses Apple App Store / Google Play in-app purchase. Payment data is processed by Apple or Google under their privacy policies. ViewWeave does not receive your full payment card details.",
        h2_5="5. What we do not do",
        li_5a="No ViewWeave user account required to film.",
        li_5b="No sale of personal data.",
        li_5c="No advertising ID tracking for ads in the App.",
        li_5d="No analytics / crash cloud service is required for core filming (if platform diagnostics are enabled by you in iOS/Android settings, that is controlled by the OS vendors).",
        h2_6="6. Children",
        p_6="The App is not directed at children under 13 (or the equivalent minimum age in your country). Do not use it to provide personal data of children to us.",
        h2_7="7. Your choices",
        li_7a="Delete library items inside the App.",
        li_7b="Uninstall the App to remove local sandbox data.",
        li_7c="Manage App Store / Play purchases and subscriptions (if any) in your store account settings.",
        li_7d="Contact us to ask questions about this policy.",
        h2_8="8. Changes",
        p_8="We may update this page when the App’s practices change. The effective date at the top will be revised.",
    ),
    S(
        tag="Support",
        h1="Support",
        intro="ViewWeave lets you film the same scene with several phones on a <strong>local Wi‑Fi or hotspot</strong>. One Master starts/stops recording; other phones join as Cameras. Footage stays on your devices — there is <strong>no ViewWeave cloud</strong>.",
        contact="Contact",
        h2="Common topics",
        li_a="<strong>Join session:</strong> same Wi‑Fi/hotspot as the Master, then scan the QR (or enter IP / link).",
        li_b="<strong>Library / rushes:</strong> stored in the app sandbox on the Master. Uninstalling the app deletes them.",
        li_c="<strong>Basic license:</strong> 7-day Basic trial, then Free. Unlock Basic via in-app purchase (App Store / Play) or Restore purchases.",
        li_d="<strong>Free limits:</strong> up to 2 phones per session; Free exports use 720p with a small watermark.",
    ),
)

T["fr"] = pack(
    (
        "Accueil",
        "Assistance",
        "Politique de confidentialité",
        "Langue",
        "Mentions légales & assistance",
        "Pages publiques pour les fiches App Store / Play.",
        "Assistance :",
        "Confidentialité :",
        "Guide",
        "Guide :",
    ),
    "Captation multi-caméras en Wi‑Fi local — sans cloud.",
    P(
        tag="Politique de confidentialité",
        h1="Politique de confidentialité",
        effective="Date d’entrée en vigueur : 15 novembre 2026",
        intro="Cette politique décrit comment l’application mobile <strong>ViewWeave</strong> (« l’App ») traite les informations. ViewWeave est un outil de captation multi-caméras locale. Elle n’exploite <strong>pas</strong> de serveur cloud ViewWeave pour vos vidéos.",
        h2_1="1. Qui nous sommes",
        p_1='ViewWeave est publiée comme application indépendante (bundle ID <code>com.viewweave.app</code>). Contact : <a href="mailto:viewweave78@gmail.com">viewweave78@gmail.com</a>.',
        h2_2="2. Données stockées sur votre appareil",
        li_2a="<strong>Vidéos et métadonnées de bibliothèque</strong> créées par vous (sessions, prises, montages) — dans les dossiers documents / médias privés de l’app sur l’appareil.",
        li_2b="<strong>État de licence</strong> (essai / Free / Basic) dans un fichier local sur l’appareil.",
        li_2c="<strong>Préférences</strong> telles que les réglages d’export, également locales.",
        p_2="Désinstaller l’App efface ces données du bac à sable. Nous ne recevons pas de copie de vos vidéos sur des serveurs ViewWeave.",
        h2_3="3. Réseau local",
        p_3="Lors d’une session multi-téléphones, les appareils communiquent sur votre <strong>Wi‑Fi local ou hotspot</strong> (HTTP sur le LAN) pour synchroniser la captation et transférer les rushes vers le Master. Ce trafic reste sur votre réseau ; il n’est pas envoyé vers un cloud ViewWeave.",
        h2_4="4. Achats (Basic)",
        p_4="Le déblocage de <strong>Basic</strong> passe par l’achat intégré App Store / Google Play. Les données de paiement sont traitées par Apple ou Google selon leurs politiques. ViewWeave ne reçoit pas vos coordonnées bancaires complètes.",
        h2_5="5. Ce que nous ne faisons pas",
        li_5a="Aucun compte utilisateur ViewWeave requis pour filmer.",
        li_5b="Aucune vente de données personnelles.",
        li_5c="Pas de suivi d’identifiant publicitaire pour de la pub dans l’App.",
        li_5d="Aucun service cloud d’analytique / crash n’est requis pour filmer (si vous activez les diagnostics iOS/Android, cela dépend des éditeurs du système).",
        h2_6="6. Enfants",
        p_6="L’App ne s’adresse pas aux enfants de moins de 13 ans (ou l’âge minimum équivalent dans votre pays). Ne l’utilisez pas pour nous transmettre des données personnelles d’enfants.",
        h2_7="7. Vos choix",
        li_7a="Supprimer des éléments de la bibliothèque dans l’App.",
        li_7b="Désinstaller l’App pour effacer les données locales du bac à sable.",
        li_7c="Gérer les achats App Store / Play dans les réglages de votre compte store.",
        li_7d="Nous contacter pour toute question sur cette politique.",
        h2_8="8. Modifications",
        p_8="Nous pouvons mettre à jour cette page si les pratiques de l’App changent. La date d’entrée en vigueur en haut sera révisée.",
    ),
    S(
        tag="Assistance",
        h1="Assistance",
        intro="ViewWeave permet de filmer la même scène avec plusieurs téléphones sur un <strong>Wi‑Fi local ou hotspot</strong>. Un Master démarre/arrête l’enregistrement ; les autres rejoignent en Caméras. Les rushes restent sur vos appareils — il n’y a <strong>pas de cloud ViewWeave</strong>.",
        contact="Contact",
        h2="Sujets fréquents",
        li_a="<strong>Rejoindre une session :</strong> même Wi‑Fi/hotspot que le Master, puis scanner le QR (ou saisir l’IP / le lien).",
        li_b="<strong>Bibliothèque / rushes :</strong> stockés dans le bac à sable de l’app sur le Master. Désinstaller l’app les efface.",
        li_c="<strong>Licence Basic :</strong> essai Basic 7 jours, puis Free. Débloquez Basic via achat intégré (App Store / Play) ou Restaurer les achats.",
        li_d="<strong>Limites Free :</strong> jusqu’à 2 téléphones par session ; exports Free en 720p avec un petit filigrane.",
    ),
)

# Remaining locales loaded from companion JSON for maintainability of this generator.
DATA = Path(__file__).with_name("_i18n_data.json")
extra = json.loads(DATA.read_text(encoding="utf-8"))
for code, payload in extra.items():
    T[code] = pack(
        tuple(payload["ui"]),
        payload["index_tag"],
        payload["privacy"],
        payload["support"],
    )

missing = [c for c, _ in LOCALES if c not in T]
if missing:
    raise SystemExit(f"Missing locales: {missing}")

js = f"""/* Auto-generated by _gen_i18n.py — do not edit by hand. */
window.VW_LEGAL_LOCALES = {json.dumps([{"id": a, "label": b} for a, b in LOCALES], ensure_ascii=False, indent=2)};
window.VW_LEGAL_I18N = {json.dumps(T, ensure_ascii=False, indent=2)};
"""
OUT.write_text(js, encoding="utf-8")
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes), locales={len(T)}")
