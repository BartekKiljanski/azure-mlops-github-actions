# Notatki do integracji z Azure Machine Learning

Ten projekt na razie konczy sie na GitHub Actions: testuje kod, trenuje model i zapisuje artefakty. To wystarcza do pokazania podstawowego procesu MLOps.

Gdybym mial rozbudowac go dalej pod Azure Machine Learning, zrobilbym to w kilku krokach:

1. Utworzyc Azure Machine Learning Workspace.
2. Przygotowac dostep dla GitHub Actions, np. przez Service Principal albo federated credentials.
3. Dodac wymagane sekrety w ustawieniach repozytorium GitHub.
4. Dodac krok logowania do Azure w workflow.
5. Po treningu zarejestrowac plik `outputs/model.pkl` jako model w Azure ML.

## Przyklad logowania do Azure

```yaml
- name: Azure login
  uses: azure/login@v2
  with:
    creds: ${{ secrets.AZURE_CREDENTIALS }}
```

## Sekrety, ktore bylyby potrzebne

W repozytorium GitHub mozna dodac np.:

- `AZURE_CREDENTIALS`
- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`

W tej wersji nie dodawalem pelnego wdrozenia do Azure ML, zeby nie komplikowac zadania limitami subskrypcji i konfiguracja zasobow. Najwazniejsze bylo pokazanie automatyzacji: testy, trening modelu i zapis artefaktow po kazdej zmianie w repozytorium.
