# Intern Performance Prediction Model

A beginner-friendly Machine Learning internship task that predicts a numeric intern performance score (0-100) from task completion, feedback, attendance, and average task completion time.

**Important:** The supplied dataset is synthetic and is intended for learning/demo purposes only. Results are not validated against real intern data.

## Files
- `main.py` — trains a Random Forest Regression model, evaluates it, and predicts an example score.
- `intern_performance_sample.csv` — 20 rows of synthetic sample data.
- `requirements.txt` — required Python libraries.

## Features and target
- Tasks completed (%) — input feature
- Feedback rating (1-5) — input feature
- Attendance (%) — input feature
- Average task time (hours) — input feature
- Performance score (0-100) — target

## Run on your computer
1. Install Python 3.10+.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run:
   ```bash
   python main.py
   ```
6. The terminal prints MAE, RMSE, R², and an example predicted score. Use the actual output from your run in any submission.

## GitHub upload (using website)
1. Sign in at https://github.com.
2. Press the **+** at the top right, then choose **New repository**.
3. Name it `intern-performance-prediction-model`.
4. Select **Public** or **Private** as required by your internship instructions.
5. Press **Create repository**.
6. On the repository page, use **Add file → Upload files**.
7. Upload `main.py`, `intern_performance_sample.csv`, `requirements.txt`, and `README.md`.
8. Press **Commit changes**.

## Submit on Internee.pk
1. Open the internship task page.
2. Select **Submission**.
3. Paste your GitHub repository link (if the submission asks for a link) or upload the required file(s).
4. Make sure the repository is visible/access permitted and that your files are uploaded.
5. Submit, then check whether the status changes.

## Model evaluation
- MAE: average absolute prediction error (lower is generally better).
- RMSE: emphasizes larger errors (lower is generally better).
- R²: compares the model with a baseline; it may be negative and should not be interpreted alone.

## Responsible use
This model should be used only as a learning/demo tool and to guide supportive feedback. Avoid using predictions as the sole basis for consequential decisions about people.
