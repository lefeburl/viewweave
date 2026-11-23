# ViewWeave — Support & Privacy (GitHub Pages)

Pages statiques pour App Store Connect / Play Console.

## Fichiers

| Fichier | Usage App Store |
|---|---|
| `support.html` | **URL de l’assistance** (point d’entrée) |
| `privacy.html` | **URL de la Politique de confidentialité** (point d’entrée) |
| `index.html` | Hub (legal + lien guide) |
| `guide/index.html` | Guide utilisateur (16 langues) + captures |
| `guide/assets/{locale}/` | Captures UI (home/create/waiting/join/library/license) |
| `headers/` | Bannières App Store (par langue) en tête des pages |
| `thumbs/` | Miniatures des vidéos (popup lecture) |
| `*.MP4` | Vidéos du parcours (racine `docs/legal/`) |
| `js/i18n.js` | Traductions legal/support/privacy |
| `js/guide_i18n.js` | Traductions du guide |
| `js/legal.js` | Sélecteur de langue + rendu |

## Langues

Sélecteur en haut à droite sur chaque page. **Défaut = English**.

Langues : `en`, `de`, `el`, `es`, `fr`, `it`, `ja`, `ko`, `nl`, `pl`, `pt`, `pt_BR`, `th`, `tr`, `zh`, `zh_TW`.

- Persistance : `localStorage` (`vw_legal_lang`)
- Lien direct : `privacy.html?lang=fr`, `support.html?lang=ja`, etc.

Le contenu anglais reste dans le HTML (fallback sans JS).

## Régénérer les traductions

```bash
cd docs/legal/js
python3 _gen_i18n.py
```

Sources : `_gen_i18n.py` (en + fr) + `_i18n_data.json` (autres locales).

## Avant publication

1. Contact support : `viewweave78@gmail.com` (déjà dans les pages).
2. Relis la privacy : elle doit coller aux réponses « Confidentialité de l’app » dans App Store Connect.

## Publier (GitHub Pages)

### Option A — dépôt dédié (simple)

1. Crée un dépôt GitHub **public** `viewweave-legal`.
2. Copie le contenu de ce dossier à la racine du dépôt (y compris `js/`).
3. Settings → **Pages** → Source: Deploy from a branch → `main` / `(root)`.
4. URLs (exemple) :
   - Support : `https://TON_PSEUDO.github.io/viewweave-legal/support.html`
   - Privacy : `https://TON_PSEUDO.github.io/viewweave-legal/privacy.html`

### Option B — depuis ce monorepo

Si tu actives Pages sur `ViewWeave-v2` avec dossier `/docs` :

- Support : `https://TON_PSEUDO.github.io/ViewWeave-v2/legal/support.html`
- Privacy : `https://TON_PSEUDO.github.io/ViewWeave-v2/legal/privacy.html`

(Settings → Pages → Branch `main` → folder `/docs`.)

Colle ces URLs dans App Store Connect → Confidentialité / fiche version.
