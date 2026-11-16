# TP1 — Sécuriser un dépôt Python avec pre-commit

Le rapport du TP est dans [RAPPORT.md](RAPPORT.md).

## Installation

Il faut Python 3.15 (même version qu'en CI) et Git.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
cp .env.example .env   # puis renseigner APP_PASSWORD
```

## Lancer les contrôles

```bash
pre-commit run --all-files
```

Les hooks `pytest` et `pip-audit` utilisent l'environnement actif : le venv doit être activé au moment du commit.

Les contrôles sont rejoués en CI ([.github/workflows/ci.yml](.github/workflows/ci.yml)). La branche `main` est protégée : passage par une pull request et CI verte obligatoires.
