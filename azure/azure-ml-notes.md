# Azure Machine Learning - notatki integracyjne

Ten projekt pokazuje uproszczony proces MLOps w GitHub Actions. Moze zostac rozszerzony o integracje z Azure Machine Learning.

## Minimalna koncepcja integracji

1. Utworzenie Azure Machine Learning Workspace.
2. Utworzenie Service Principal lub federated credentials dla GitHub Actions.
3. Dodanie sekretow Azure w repozytorium GitHub.
4. Dodanie kroku logowania do Azure w workflow.
5. Rejestracja modelu `outputs/model.pkl` w Azure ML Workspace.

## Przykladowy krok logowania do Azure

```yaml
- name: Azure login
  uses: azure/login@v2
  with:
    creds: ${{ secrets.AZURE_CREDENTIALS }}
```

## Przykladowe sekrety

W ustawieniach repozytorium GitHub mozna dodac sekrety:

- `AZURE_CREDENTIALS`
- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`

W zadaniu laboratoryjnym najwazniejsze jest pokazanie automatyzacji procesu ML, czyli testow, treningu modelu oraz zapisu artefaktow w GitHub Actions.
