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

## Propozycja zrzutow ekranu do dokumentacji

Do raportu w Wordzie warto wykonac 10-15 zrzutow ekranu:

1. Widok utworzonego repozytorium GitHub.
2. Struktura plikow projektu.
3. Plik `src/train.py`.
4. Plik `.github/workflows/mlops.yml`.
5. Plik `requirements.txt`.
6. Zakladka Actions w repozytorium.
7. Uruchomiony workflow `MLOps pipeline`.
8. Krok instalacji zaleznosci.
9. Krok uruchomienia testow.
10. Krok treningu modelu.
11. Zielony status zakonczonego workflow.
12. Widok artefaktu `mlops-model-artifacts`.
13. Plik `metrics.json` z wynikami modelu.
14. Koncowy widok repozytorium na GitHubie.
15. Opcjonalnie widok Azure Portal lub Azure Machine Learning Workspace.

## Opis do sprawozdania

W ramach zadania skonfigurowano prosty proces MLOps z wykorzystaniem GitHub Actions. Pipeline automatycznie instaluje zaleznosci, uruchamia testy, wykonuje trening modelu regresyjnego oraz zapisuje wytrenowany model i metryki jako artefakty. Rozwiazanie prezentuje podstawowe elementy MLOps: powtarzalnosc procesu, automatyzacje, kontrole wersji oraz archiwizacje wyniku treningu.

## Notatki z wykonania

Podczas realizacji cwiczenia najpierw przygotowano podstawowy workflow GitHub Actions, a nastepnie poprawiono konfiguracje testow, poniewaz pierwszy przebieg pipeline'u zakonczyl sie bledem importu modulu `src` na runnerze GitHub. Problem zostal rozwiazany przez dodanie `PYTHONPATH` w workflow oraz pliku `pytest.ini`.

Do projektu wybrano prosty model regresji liniowej napisany w Pythonie bez ciezkich bibliotek ML. Dzieki temu pipeline jest szybki, powtarzalny i dobrze nadaje sie do pokazania samego procesu MLOps: testowanie, trening, zapis metryk i publikacja artefaktow.

Najwazniejszy efekt koncowy:

- workflow `MLOps pipeline` konczy sie statusem `success`,
- plik `outputs/model.pkl` jest publikowany jako artefakt,
- plik `outputs/metrics.json` zawiera metryki modelu,
- repozytorium moze zostac rozszerzone o integracje z Azure Machine Learning.
