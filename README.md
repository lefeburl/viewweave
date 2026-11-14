# ViewWeave — Support & Privacy (GitHub Pages)

Pages statiques pour App Store Connect / Play Console.

## Fichiers

| Fichier | Usage App Store |
|---|---|
| `support.html` | **URL de l’assistance** |
| `privacy.html` | **URL de la Politique de confidentialité** |
| `index.html` | Hub optionnel |

## Avant publication

1. Remplace `support@viewweave.app` par **ton vrai e-mail** dans `support.html` et `privacy.html`.
2. Relis la privacy : elle doit coller aux réponses « Confidentialité de l’app » dans App Store Connect.

## Publier (GitHub Pages)

### Option A — dépôt dédié (simple)

1. Crée un dépôt GitHub **public** `viewweave-legal`.
2. Copie le contenu de ce dossier à la racine du dépôt.
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
