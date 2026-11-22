"""Extra checks for my Unit 9 write-up (not part of the required assignment code).

Uses the same data, feature, 70/30 split (random_state=1), and models as
IN404_Unit9.py, then adds measures that suit a numeric target:
  - mean absolute error (MAE) and R-squared on the test split for all three models
  - the share of test days each model predicted within 5 and 10 uninstalls
  - the most-frequent-value baseline for exact-match accuracy
  - the random forest's top votes for 25, 51, and 90 installs
  - a RandomForestRegressor for comparison with the classifier
  - decision tree vs. random forest test accuracy over 30 different splits
  - the break-even install level where predicted uninstalls equal installs
"""
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

warnings.simplefilter("ignore")

col_names = ['Date', 'Package_Name', 'Daily_Device_Installs', 'Daily_Device_Uninstalls',
             'Daily_Device_Upgrades', 'Total_User_Installs', 'Daily_User_Installs',
             'Daily_User_Uninstalls']
data = pd.read_csv(Path(__file__).resolve().parent / "IN404_Installs.csv", names=col_names)
X = data[["Daily_Device_Installs"]]
y = data.Daily_Device_Uninstalls
inputs = np.array([[25], [51], [90]])

print("== Data set ==")
print("Days:", len(data), "| installs range:", X.min().item(), "to", X.max().item())
print("Correlation (installs vs. uninstalls):", round(X.Daily_Device_Installs.corr(y), 4))
print("Total installs:", X.Daily_Device_Installs.sum(), "| total uninstalls:", y.sum(),
      "| ratio:", round(y.sum() / X.Daily_Device_Installs.sum(), 4))
print("Distinct uninstall values (classes):", y.nunique())
for v in (25, 51, 90):
    near = y[X.Daily_Device_Installs.between(v - 2, v + 2)]
    print(f"Actual uninstalls on days with {v - 2}-{v + 2} installs: n={len(near)}, mean={near.mean():.1f}")

# Full-data linear regression, as in IN404_Unit9.py
linreg = LinearRegression().fit(X, y)
b0, b1 = linreg.intercept_, linreg.coef_[0]
print("\n== Linear regression (all data) ==")
print("Intercept:", round(b0, 4), "| coefficient:", round(b1, 4), "| R-squared:", round(linreg.score(X, y), 4))
print("Break-even installs (predicted uninstalls = installs):", round(b0 / (1 - b1), 2))
for v, p in zip((25, 51, 90), linreg.predict(inputs)):
    print(f"  {v} installs -> {p:.2f} uninstalls ({p / v:.1%} of installs)")

# Same split and models as IN404_Unit9.py
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
tree = DecisionTreeClassifier(random_state=1).fit(X_train, y_train)
rf = RandomForestClassifier(n_estimators=100, random_state=1).fit(X_train, y_train)
lr_split = LinearRegression().fit(X_train, y_train)

print("\n== Test split comparison (622 test days) ==")
mode = y_train.mode()[0]
print(f"Baseline: always predict the most common training value ({mode}) -> accuracy",
      round((y_test == mode).mean(), 4))
for name, pred in [("Linear regression", lr_split.predict(X_test)),
                   ("Decision tree", tree.predict(X_test)),
                   ("Random forest", rf.predict(X_test))]:
    err = np.abs(y_test - pred)
    print(f"{name:18s} exact={np.mean(np.round(pred) == y_test):.4f}  MAE={err.mean():.2f}  "
          f"R2={metrics.r2_score(y_test, pred):.3f}  within5={np.mean(err <= 5):.3f}  "
          f"within10={np.mean(err <= 10):.3f}")
print("Tree depth:", tree.get_depth(), "| leaves:", tree.get_n_leaves())
best_train = (y_train.groupby(X_train.Daily_Device_Installs)
              .agg(lambda s: s.value_counts().iloc[0]).sum() / len(y_train))
print("Highest training accuracy any model could reach with this one feature:", round(best_train, 4))

print("\n== Random forest votes ==")
for v in (25, 51, 90):
    seen = sorted(y_train[X_train.Daily_Device_Installs == v].tolist())
    top = sorted(zip(rf.predict_proba([[v]])[0], rf.classes_), reverse=True)[:3]
    print(f"{v} installs: training days with exactly {v} installs = {len(seen)} {seen}")
    print("   top classes:", ", ".join(f"{c} ({p:.1%})" for p, c in top))

rfr = RandomForestRegressor(n_estimators=100, random_state=1).fit(X_train, y_train)
print("\n== RandomForestRegressor (for comparison) ==")
print("Test MAE:", round(metrics.mean_absolute_error(y_test, rfr.predict(X_test)), 2),
      "| R2:", round(metrics.r2_score(y_test, rfr.predict(X_test)), 3))
print("Predictions for 25, 51, 90:", np.round(rfr.predict(inputs), 2))

print("\n== Decision tree vs. random forest test accuracy over 30 splits ==")
rf_wins = tree_wins = ties = 0
for seed in range(30):
    a, b, c, d = train_test_split(X, y, test_size=0.3, random_state=seed)
    t_acc = DecisionTreeClassifier(random_state=1).fit(a, c).score(b, d)
    f_acc = RandomForestClassifier(n_estimators=100, random_state=1).fit(a, c).score(b, d)
    rf_wins += f_acc > t_acc
    tree_wins += t_acc > f_acc
    ties += t_acc == f_acc
print(f"Random forest higher: {rf_wins} | decision tree higher: {tree_wins} | tied: {ties}")
