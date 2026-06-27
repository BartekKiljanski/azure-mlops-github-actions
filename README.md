# Azure MLOps GitHub Actions

Projekt przedstawia podstawowy proces MLOps dla Azure Machine Learning z wykorzystaniem GitHub Actions.

Autor: Bartlomiej Kiljanski

Celem cwiczenia jest pokazanie automatyzacji typowego cyklu pracy ML:

- wersjonowanie kodu w repozytorium GitHub,
- instalacja zaleznosci projektu,
- uruchomienie testow,
- trening modelu uczenia maszynowego,
- zapis metryk treningu,
- zapis wytrenowanego modelu jako artefaktu pipeline'u,
- przygotowanie projektu do dalszej integracji z Azure Machine Learning.

## Struktura projektu

```text
.
├── .github/workflows/mlops.yml
├── src/
│   ├── __init__.py
│   └── train.py
├── tests/
│   └── test_training.py
├── azure/
│   └── azure-ml-notes.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Jak dziala pipeline

Workflow GitHub Actions uruchamia sie po kazdym pushu do galezi `main` oraz po pull requestach.

Etapy workflow:

1. Pobranie kodu z repozytorium.
2. Instalacja Pythona.
3. Instalacja zaleznosci z `requirements.txt`.
4. Uruchomienie testow jednostkowych.
5. Trening modelu ML.
6. Zapis plikow wynikowych w katalogu `outputs/`.
7. Publikacja artefaktow pipeline'u.

## Uruchomienie lokalne

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
python src/train.py
```

Na Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
python src\train.py
```

Po uruchomieniu treningu powstanie katalog `outputs/` zawierajacy:

- `model.pkl` - wytrenowany model,
- `metrics.json` - metryki jakosci modelu.

## Powiazanie z Azure Machine Learning

Projekt jest przygotowany jako uproszczony przyklad MLOps. W praktycznym scenariuszu kolejnym krokiem byloby dodanie sekretow Azure w GitHub Actions i opublikowanie modelu do Azure Machine Learning Workspace.

Przykladowe sekrety, ktore mozna dodac w GitHub:

- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`
- `AZURE_CREDENTIALS`

Szczegoly znajduja sie w pliku [azure/azure-ml-notes.md](azure/azure-ml-notes.md).
