from pathlib import Path

from src.train import METRICS_PATH, MODEL_PATH, train_model


def test_train_model_creates_artifacts(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    metrics = train_model(random_state=7)

    assert Path(MODEL_PATH).exists()
    assert Path(METRICS_PATH).exists()
    assert metrics["r2_score"] > 0.5
    assert metrics["mean_absolute_error"] > 0
    assert metrics["train_rows"] > metrics["test_rows"]
