# Azure MLOps GitHub Actions

Autor: Bartlomiej Kiljanski

Repozytorium przygotowane do zadania z konfiguracji procesu MLOps. Zrobilem tutaj prosty przyklad pipeline'u w GitHub Actions, ktory uruchamia testy, trenuje model i zapisuje wynik jako artefakt.

Nie jest to pelne wdrozenie produkcyjne w Azure Machine Learning, tylko mala wersja pokazujaca podstawowy mechanizm MLOps. Taki projekt mozna pozniej rozbudowac o logowanie do Azure i rejestracje modelu w Azure ML Workspace.

## Co jest w projekcie

- prosty skrypt treningowy w Pythonie,
- test sprawdzajacy, czy trening tworzy pliki wynikowe,
- workflow GitHub Actions,
- zapis modelu do `outputs/model.pkl`,
- zapis metryk do `outputs/metrics.json`,
- publikacja wynikow jako artefakt GitHub Actions.

## Struktura

```text
.
├── .github/workflows/mlops.yml
├── azure/
│   └── azure-ml-notes.md
├── src/
│   ├── __init__.py
│   └── train.py
├── tests/
│   └── test_training.py
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

## Jak dziala workflow

Pipeline uruchamia sie po pushu do galezi `main`. W workflow sa wykonane nastepujace kroki:

1. Pobranie repozytorium.
2. Przygotowanie Pythona.
3. Instalacja zaleznosci.
4. Uruchomienie testow.
5. Uruchomienie treningu modelu.
6. Wyswietlenie metryk.
7. Zapis artefaktow.

Po poprawnym przebiegu w zakladce Actions widoczny jest status `success`, a w szczegolach runu dostepny jest artefakt `mlops-model-artifacts`.

## Uruchomienie lokalne

Na Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest -q
python src\train.py
```

Na Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python src/train.py
```

Po uruchomieniu treningu powstaje katalog `outputs/` z plikami:

- `model.pkl` - zapisany model,
- `metrics.json` - metryki po treningu.

## Azure Machine Learning

W tym cwiczeniu skupilem sie na samym procesie MLOps w GitHub Actions. Azure Machine Learning potraktowalem jako kolejny etap rozbudowy projektu.

Zeby podlaczyc ten projekt do Azure ML, trzeba byloby dodac w GitHub sekrety Azure, wykonac logowanie w workflow i zarejestrowac wygenerowany model w Azure ML Workspace. Krotkie notatki do tego sa w pliku [azure/azure-ml-notes.md](azure/azure-ml-notes.md).

## Dokumentacja zadania

Do oddania przygotowywany jest osobny plik Word/PDF ze zrzutami ekranu. W repozytorium zostawilem tylko kod projektu i konfiguracje pipeline'u.
