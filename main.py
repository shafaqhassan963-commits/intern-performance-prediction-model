import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_FILE = "intern_performance_sample.csv"

def main():
    df = pd.read_csv(DATA_FILE)
    features = [
        "tasks_completed_pct",
        "feedback_rating",
        "attendance_pct",
        "avg_task_time_hours",
    ]
    target = "performance_score"

    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("=== Evaluation ===")
    print(f"MAE: {mean_absolute_error(y_test, predictions):.2f}")
    print(f"RMSE: {mean_squared_error(y_test, predictions) ** 0.5:.2f}")
    print(f"R2: {r2_score(y_test, predictions):.2f}")

    example = pd.DataFrame([{
        "tasks_completed_pct": 85,
        "feedback_rating": 4.4,
        "attendance_pct": 92,
        "avg_task_time_hours": 22,
    }])
    print("\nExample predicted score (synthetic input):")
    print(f"{model.predict(example)[0]:.2f} / 100")

if __name__ == "__main__":
    main()
