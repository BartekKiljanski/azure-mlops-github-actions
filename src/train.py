from __future__ import annotations

import json
import pickle
import random
from pathlib import Path


OUTPUT_DIR = Path("outputs")
MODEL_PATH = OUTPUT_DIR / "model.pkl"
METRICS_PATH = OUTPUT_DIR / "metrics.json"


def generate_dataset(rows: int = 200, random_state: int = 42) -> list[tuple[float, float]]:
    """Generate a deterministic regression dataset."""
    random.seed(random_state)
    data = []
    for index in range(rows):
        x = index / 10
        noise = random.uniform(-1.5, 1.5)
        y = 2.7 * x + 8 + noise
        data.append((x, y))
    return data


def fit_linear_regression(data: list[tuple[float, float]]) -> dict[str, float]:
    """Fit a simple y = ax + b regression model."""
    x_values = [row[0] for row in data]
    y_values = [row[1] for row in data]
    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(y_values) / len(y_values)

    numerator = sum((x - x_mean) * (y - y_mean) for x, y in data)
    denominator = sum((x - x_mean) ** 2 for x in x_values)
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    return {"slope": slope, "intercept": intercept}


def predict(model: dict[str, float], x_value: float) -> float:
    return model["slope"] * x_value + model["intercept"]


def mean_absolute_error(data: list[tuple[float, float]], model: dict[str, float]) -> float:
    errors = [abs(y - predict(model, x)) for x, y in data]
    return sum(errors) / len(errors)


def r2_score(data: list[tuple[float, float]], model: dict[str, float]) -> float:
    y_values = [row[1] for row in data]
    y_mean = sum(y_values) / len(y_values)
    residual_sum = sum((y - predict(model, x)) ** 2 for x, y in data)
    total_sum = sum((y - y_mean) ** 2 for y in y_values)
    return 1 - residual_sum / total_sum


def train_model(random_state: int = 42) -> dict[str, float]:
    """Train a regression model and return evaluation metrics."""
    dataset = generate_dataset(random_state=random_state)
    split_index = int(len(dataset) * 0.8)
    train_data = dataset[:split_index]
    test_data = dataset[split_index:]
    model = fit_linear_regression(train_data)

    metrics = {
        "r2_score": round(r2_score(test_data, model), 4),
        "mean_absolute_error": round(mean_absolute_error(test_data, model), 4),
        "train_rows": float(len(train_data)),
        "test_rows": float(len(test_data)),
        "model_slope": round(model["slope"], 4),
        "model_intercept": round(model["intercept"], 4),
    }

    OUTPUT_DIR.mkdir(exist_ok=True)
    MODEL_PATH.write_bytes(pickle.dumps(model))
    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    return metrics


def main() -> None:
    metrics = train_model()
    print("Model training completed.")
    print(json.dumps(metrics, indent=2))
    print(f"Model saved to: {MODEL_PATH}")
    print(f"Metrics saved to: {METRICS_PATH}")


if __name__ == "__main__":
    main()
