# TacOT

English-language research website for TacOT: Learning Contact-Rich Dexterous Manipulation from Human Demonstrations via Tactile-Guided Optimal Transport.

## Publish on GitHub Pages

Upload this folder to a public GitHub repository on its `main` branch. In Settings → Pages, select GitHub Actions as the publishing source. The included workflow publishes `dist` automatically. Visitors do not need an account.

The site uses relative asset paths and supports GitHub Pages project URLs. No build or dependency installation is needed. Research images, videos and the paper are included with the owner's permission to publish.

The Actions workflow uses read-only repository access. Research assets are downloaded from the original public site during deployment and verified against SHA-256 hashes in `asset-manifest.json`. The deployed GitHub Pages site serves its own copy of every asset; builds require the source assets to remain available unless the files are added to `dist/assets` in this repository.

## Local preview

Run `python -m http.server 4173 --directory dist` and open http://localhost:4173.
