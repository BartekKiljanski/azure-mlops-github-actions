# Notatki do sprawozdania

## Temat

Skonfigurowanie procesu MLOps dla Azure Machine Learning z wykorzystaniem GitHub Actions.

## Cel

Celem bylo przygotowanie prostego procesu automatyzacji dla projektu uczenia maszynowego. Pipeline ma pokazac, ze po zmianie kodu w repozytorium GitHub mozna automatycznie uruchomic testy, wykonac trening modelu i zapisac wynik jako artefakt.

## Wykonane kroki

1. Utworzono publiczne repozytorium `azure-mlops-github-actions`.
2. Przygotowano strukture projektu Python.
3. Dodano skrypt treningowy `src/train.py`.
4. Dodano test jednostkowy w katalogu `tests`.
5. Utworzono workflow `.github/workflows/mlops.yml`.
6. Uruchomiono pipeline w GitHub Actions.
7. Poprawiono blad pierwszego przebiegu zwiazany z importem modulu `src`.
8. Uzyskano poprawny, zielony przebieg pipeline'u.
9. Sprawdzono, ze GitHub Actions generuje artefakt `mlops-model-artifacts`.

## Napotkany problem

Pierwszy przebieg workflow zakonczyl sie niepowodzeniem podczas uruchamiania testow. Przyczyna byl problem z importem lokalnego modulu `src` na runnerze GitHub Actions. Lokalnie test dzialal, ale w srodowisku CI sciezka projektu nie byla jednoznacznie dostepna dla Pythona.

Rozwiazanie:

- dodano `PYTHONPATH: ${{ github.workspace }}` w krokach testowania i treningu,
- dodano plik `pytest.ini` z ustawieniem `pythonpath = .`.

Po tej zmianie pipeline zakonczyl sie statusem `success`.

## Wnioski

GitHub Actions pozwala w prosty sposob zautomatyzowac podstawowy proces MLOps. Nawet prosty projekt ML moze miec pipeline, ktory zapewnia powtarzalnosc treningu, uruchamianie testow i archiwizacje artefaktow. W kolejnym kroku projekt mozna rozbudowac o logowanie do Azure i rejestracje modelu w Azure Machine Learning Workspace.

## Lista zrzutow ekranu

1. Widok repozytorium GitHub.
2. Struktura plikow repozytorium.
3. Plik `README.md`.
4. Plik `src/train.py`.
5. Plik `tests/test_training.py`.
6. Plik `.github/workflows/mlops.yml`.
7. Zakladka Actions.
8. Pierwszy nieudany workflow.
9. Commit z poprawka importow.
10. Zielony workflow po poprawce.
11. Log kroku `Run tests`.
12. Log kroku `Train model`.
13. Widok metryk w logu.
14. Artefakt `mlops-model-artifacts`.
15. Koncowy widok repozytorium na koncie GitHub.
