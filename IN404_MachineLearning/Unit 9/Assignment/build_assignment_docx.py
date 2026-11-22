"""Build IN404_ShubhamRaj_Unit9.docx using the Unit 8 Assignment 1 document as the style template."""
import copy
import sys
from pathlib import Path

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.shared import Inches, Pt

ROOT = Path(sys.argv[1])  # IN404_MachineLearning folder
A9 = ROOT / "Unit 9" / "Assignment"
SHOTS = A9 / "My Screenshots"
TEMPLATE = ROOT / "Unit 8" / "Assignment 1" / "IN404_ShubhamRaj_Unit8_Assignment1.docx"
OUT = A9 / "IN404_ShubhamRaj_Unit9.docx"

doc = docx.Document(TEMPLATE)
body = doc.element.body
for el in list(body):
    if not el.tag.endswith("sectPr"):
        body.remove(el)


def para(text="", style="Normal", indent=True, spacing=2.0, align=None):
    p = doc.add_paragraph(style=style)
    p.paragraph_format.line_spacing = spacing
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.5)
    if align is not None:
        p.alignment = align
    if text:
        add_runs(p, text)
    return p


def add_runs(p, text):
    """Supports **bold** segments inside text."""
    parts = text.split("**")
    for i, part in enumerate(parts):
        if part:
            r = p.add_run(part)
            r.bold = (i % 2 == 1)


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.line_spacing = 2.0
    add_runs(p, text)
    return p


def page_break():
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)


def h1(text):
    doc.add_paragraph(text, style="Heading 1")


def h2(text):
    doc.add_paragraph(text, style="Heading 2")


def code_block(text, size=8):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text.rstrip("\n"))
    r.font.name = "Courier New"
    r.font.size = Pt(size)


def label(number_text, title):
    """APA 7 label: bold number on one line, italic title in title case on the next."""
    n = doc.add_paragraph()
    n.paragraph_format.line_spacing = 2.0
    n.paragraph_format.keep_with_next = True
    n.add_run(number_text).bold = True
    t = doc.add_paragraph()
    t.paragraph_format.line_spacing = 2.0
    t.paragraph_format.keep_with_next = True
    t.add_run(title).italic = True


FIG = [0]
TAB = [0]


def figure(path, title, width=6.0):
    FIG[0] += 1
    label(f"Figure {FIG[0]}", title)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(path), width=Inches(width))


def table(title, rows, widths=None):
    TAB[0] += 1
    label(f"Table {TAB[0]}", title)
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = "Table Grid"
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = t.cell(i, j)
            cell.text = ""
            r = cell.paragraphs[0].add_run(str(val))
            r.font.size = Pt(10)
            r.bold = (i == 0)
            if widths:
                cell.width = Inches(widths[j])
    doc.add_paragraph()
    return t


# ---------------- Title page ----------------
p = para(indent=False, align=WD_ALIGN_PARAGRAPH.CENTER)
p.add_run("IN404 Unit 9 Assignment: Predictions Using Various Models").bold = True
para("Shubham Raj", indent=False, align=WD_ALIGN_PARAGRAPH.CENTER)
para("Purdue University Global\nIN404: Machine Learning\nDr. Sen Baidya\nNovember 4, 2026",
     indent=False, align=WD_ALIGN_PARAGRAPH.CENTER)

# ---------------- Item 1 ----------------
page_break()
h1("Item 1: Python Code and Execution Results")
para("I saved the provided IN404_Installs.csv and IN404_Unit9.py files together in my Unit 9 Assignment "
     "folder and completed every section marked \"YOUR CODE HERE.\" The code I added does the following:")
bullet("**Data overview:** Prints the top 4 rows of the data set with head(4) and its shape, which is "
       "2,073 rows (one per day) and 8 columns.")
bullet("**Scatter plot:** Draws the pandas scatter plot of daily device installs versus daily device "
       "uninstalls with data.plot(kind=\"scatter\").")
bullet("**Linear regression:** Prints the intercept_ and coef_ of the fitted model, and adds the "
       "predictions for 51 and 90 daily device installs, following the provided example for 25.")
bullet("**Decision tree:** Fits the DecisionTreeClassifier on the training split and prints its "
       "accuracy on both the training data and the test data.")
bullet("**Random forest:** Prints the predictions on X_test and the test accuracy with "
       "metrics.accuracy_score, and adds the predictions for 51 and 90 daily device installs "
       "(Pedregosa et al., 2011).")
para("I also made three small changes beyond the placeholders, and I marked each one with a comment in the "
     "code. First, the CSV file is read from the same folder as the script, so the program works no matter "
     "which folder it is run from. Second, I added random_state=1 to the train/test split and to the random "
     "forest. Without it, the split and the forest change every time the program runs, so the accuracy and "
     "predictions in this document could not be reproduced. Third, the comment for the decision tree says "
     "to fit it \"using X and y,\" but I fit it on X_train and y_train so that the 30% test split stays "
     "unseen. I print the tree's training accuracy and its test accuracy, because only the test accuracy "
     "is a fair comparison to the random forest, which is scored on the test split. I explain why this "
     "matters in Item 7.")
h2("Complete Python Code (IN404_Unit9.py)")
code_block((A9 / "IN404_Unit9.py").read_text())
h2("Execution Screenshots")
para("These screenshots are from running IN404_Unit9.py in the VS Code terminal with my main Python 3.14 "
     "environment. The program opens each plot in its own window and continues once the window is closed, "
     "so the terminal output builds up between the plots.")
figure(SHOTS / "exec1_seaborn_plot.png",
       "Seaborn Plot of Daily Device Installs Versus Uninstalls, After the Top 4 Rows and Data Set Shape Were Printed")
figure(SHOTS / "exec2_pandas_plot.png",
       "Pandas Scatter Plot of Daily Device Installs Versus Uninstalls")
figure(SHOTS / "exec3_linreg_plot.png",
       "Linear Regression Predictions on X (Red Line), With the Intercept and Coefficient Printed")
figure(SHOTS / "exec4_terminal_part1.png",
       "Terminal Output After All Three Plots Were Closed")
figure(SHOTS / "exec5_terminal_part2.png",
       "Terminal Output Scrolled Down, Showing the Random Forest Results")
h2("Console Output")
para("The full console output is also shown below as text. The values are identical to the run in the "
     "screenshots. When the output is saved to a file, pandas shortens the top 4 rows to fit a narrower "
     "width, so some columns appear as \"...\" here. Figure 4 shows all eight columns.")
code_block((A9 / "console_output.txt").read_text(), size=7.5)

# ---------------- Item 2 ----------------
page_break()
h1("Item 2: Intercept and Coefficient for the Linear Regression Model")
para("**Intercept:** 8.3902", indent=False)
para("**Coefficient:** 0.7662", indent=False)
para("This gives the fitted equation: predicted daily device uninstalls = 8.3902 + 0.7662 × daily device "
     "installs. Least squares chose these two values because together they minimize the sum of the squared "
     "differences between the actual and predicted uninstalls across all 2,073 days (scikit-learn "
     "developers, n.d.-c). The model's R² on the full data set is 0.8346, so this one line explains about "
     "83% of the day-to-day variation in uninstalls.")

# ---------------- Item 3 ----------------
page_break()
h1("Item 3: What the Intercept and Coefficient Tell Me About the Data Set")
para("The **coefficient of 0.7662** is the slope of the line. It tells me that for each additional daily "
     "device install, the model expects about 0.77 more daily device uninstalls. Put another way, a day with "
     "100 more installs is expected to have about 77 more uninstalls. Because the coefficient is positive, "
     "installs and uninstalls rise and fall together, which matches the scatter plots in Figures 1 to 3. The "
     "correlation between the two columns is 0.91, which is a strong positive relationship. Because the "
     "coefficient is less than 1, uninstalls grow more slowly than installs, so busier days should leave "
     "more net new devices than quiet days.")
para("The **intercept of 8.3902** is the predicted number of uninstalls on a day with zero installs. I would "
     "not read this value too literally, because the data never has a day with zero installs. The lowest "
     "value is 24, so zero is outside the range the model learned from. Still, it makes some sense as a "
     "baseline. Uninstalls come from devices that already have the app, not only from that day's new "
     "installs, so a small number of people would likely uninstall the app even on a day with no new "
     "installs.")
para("One thing I want to be careful about is that the coefficient shows a relationship, not a cause. New "
     "installs do not have to cause uninstalls. It is more likely that both go up when the app gets more "
     "attention. The clearest example in this data is July and August 2016, when the app had 28 days with "
     "300 or more installs, and uninstalls rose to between about 200 and 480 per day at the same time.")

# ---------------- Item 4 ----------------
page_break()
h1("Item 4: Linear Regression Prediction Results for 25, 51, and 90 Daily Device Installs")
table("Linear Regression Predictions for 25, 51, and 90 Daily Device Installs", [
    ["Daily device installs", "Predicted daily device uninstalls", "Uninstalls as a share of installs"],
    ["25", "27.55", "110.2%"],
    ["51", "47.47", "93.1%"],
    ["90", "77.35", "85.9%"],
], widths=[1.8, 2.4, 2.3])
para("Table 1 lists the three predictions. Each value comes from plugging the number of installs into the fitted equation. For example, for 51 "
     "installs: 8.3902 + 0.7662 × 51 = 47.47. As the professor explained in the seminar, the input is written "
     "as [[51]] with double brackets so that it has the same two-dimensional shape (one row and one column) "
     "as the X data frame the model was trained on.")
para("The predictions are decimals because linear regression outputs a continuous number. In practice, "
     "I would read them as about 28, 47, and 77 uninstalls.")

# ---------------- Item 5 ----------------
page_break()
h1("Item 5: Conclusions Based on the Predicted Values for Uninstalls")
para("The main conclusion is that uninstalls increase as installs increase, but at a slower rate, so the "
     "share of installs that are cancelled out by uninstalls goes down as the app gets busier. At 25 installs, "
     "the model predicts more uninstalls (27.55) than installs, which would be a net loss of about 2.5 devices "
     "for the day. At 51 installs, uninstalls are about 93% of installs, and at 90 installs they drop to about "
     "86%, a net gain of about 13 devices. Setting the equation equal to the number of installs shows that the "
     "break-even point is about 36 installs per day (8.3902 / (1 − 0.7662) = 35.89). On days below that, the "
     "app is expected to lose more devices than it gains.")
para("I also compared the predictions to the actual data, to see how much I should trust them (see Table 2):")
table("Linear Regression Predictions Compared With Actual Uninstalls on Similar Days", [
    ["Input", "Linear regression prediction", "Actual average uninstalls on nearby days", "Days used"],
    ["25 installs", "27.55", "37.0 (days with 23–27 installs)", "6"],
    ["51 installs", "47.47", "53.6 (days with 49–53 installs)", "102"],
    ["90 installs", "77.35", "75.3 (days with 88–92 installs)", "148"],
], widths=[1.1, 1.6, 2.6, 1.0])
para("The prediction for 90 installs is very close to what actually happened, but the model predicts too "
     "few uninstalls for 51 and especially for 25 installs. I think there are two reasons for this. First, "
     "25 is at the very edge of the data. Only 9 of the 2,073 days had 30 or fewer installs, so the line has "
     "very little information about that range. Second, the line is pulled by the small number of very high "
     "install days in 2016 (Figure 3), which makes it a compromise across the whole range rather than an "
     "exact fit at the low end. So I am fairly confident in the 51 and 90 predictions, but I would treat the "
     "25 prediction, and the net loss it suggests, with caution.")
para("These predictions are also averages, not exact counts. On the test split, the linear regression "
     "predictions were off by about 13 uninstalls per day on average (a mean absolute error of 13.12), "
     "because days with the same number of installs can still have very different numbers of uninstalls.")

# ---------------- Item 6 ----------------
page_break()
h1("Item 6: Comparing the Linear Regression Predictions to the Random Forest Predictions")
table("Linear Regression and Random Forest Predictions for 25, 51, and 90 Daily Device Installs", [
    ["Daily device installs", "Linear regression", "Random forest (classifier)", "Actual average on nearby days"],
    ["25", "27.55", "24", "37.0"],
    ["51", "47.47", "60", "53.6"],
    ["90", "77.35", "60", "75.3"],
], widths=[1.4, 1.5, 1.8, 1.8])
para("Table 3 shows the two models side by side. They give very different answers, and the reason is in how each one predicts. Linear "
     "regression draws one line through all of the data, so its predictions rise smoothly as installs go up. "
     "The random forest in this code is a RandomForestClassifier, which treats every distinct uninstall count "
     "as its own category. There are 145 different uninstall values in the data. Each of the 100 trees "
     "predicts one of these categories, and the forest returns the category with the highest combined "
     "probability across the trees (scikit-learn developers, n.d.-b). That is why the random forest only "
     "returns whole numbers that already exist in the training data.")
para("I looked more closely at each random forest prediction:")
bullet("**25 installs:** No training day had exactly 25 installs. The closest one was a day with 24 installs "
       "and 24 uninstalls, so most of the trees (68% of the probability) chose 24.")
bullet("**51 installs:** Nine training days had exactly 51 installs, with uninstalls ranging from 37 to 66. "
       "The value 60 appeared twice, which was enough for it to win with only 22.6% of the probability.")
bullet("**90 installs:** Twenty training days had exactly 90 installs, with uninstalls ranging from 52 to 97. "
       "The forest chose 60 with just 10.4% of the probability, barely ahead of 94 at 10.1%. This was close to "
       "a tie, and the winning value happened to be one of the lowest in the group.")
para("The result is that the random forest predicts the same 60 uninstalls for both 51 and 90 installs, even "
     "though days with 90 installs actually averaged about 22 more uninstalls. The linear regression "
     "predictions follow the real trend much better, and for 90 installs the regression (77.35) is close to "
     "the actual average (75.3) while the forest (60) is far below it. Across the whole test split, the "
     "linear regression also had a lower mean absolute error than the random forest (13.12 versus 14.60 "
     "uninstalls).")
para("To check whether the problem was the random forest itself or the classifier version of it, I also "
     "trained a RandomForestRegressor on the same split. Instead of picking one category, it averages the "
     "trees' numeric predictions. It predicted 29.88, 56.33, and 75.94 uninstalls for 25, 51, and 90 installs, "
     "which follow the trend, and its mean absolute error of 12.41 was the lowest of any model I tried. "
     "Breiman (2001) notes that the random forest idea also applies to regression, and this shows that for a "
     "numeric target like uninstalls, the regression version is the better fit.")

# ---------------- Item 7 ----------------
page_break()
h1("Item 7: Which Model Had the Better Accuracy, the Decision Tree or the Random Forest?")
table("Decision Tree and Random Forest Results on the Test Data", [
    ["Measure (622 test days)", "Decision tree", "Random forest"],
    ["Accuracy on the training data", "0.1799", "0.1799"],
    ["Accuracy on the test data (exact matches)", "0.0225 (14 of 622)", "0.0225 (14 of 622)"],
    ["Mean absolute error on the test data", "15.15 uninstalls", "14.60 uninstalls"],
    ["Test predictions within 10 uninstalls", "45.8%", "46.9%"],
    ["R² on the test data", "0.781", "0.796"],
], widths=[2.8, 1.8, 1.8])
para("**In my run, the decision tree and the random forest had exactly the same test accuracy, 0.0225** (Table 4). "
     "Each got 14 of the 622 test days exactly right. The random forest was slightly better on the measures "
     "that look at how close the predictions were: its average error was about half an uninstall smaller, and "
     "a slightly larger share of its predictions landed within 10 uninstalls. So I would give the random forest "
     "a small edge overall, but on the accuracy score itself the two models tied.")
para("I want to point out one thing about the decision tree's accuracy. If the tree is scored on the same "
     "training data it was fit on, its accuracy is 0.1799, which looks about eight times better than the "
     "random forest's 0.0225. However, that comparison is not fair, because the random forest is scored on the "
     "test data. The tree has a depth of 28 and 165 leaves, one for every distinct install value in the "
     "training data, so it has memorized the training rows. This is the overfitting the professor warned about "
     "in the seminar, and it matches the scikit-learn guide's warning that decision trees can create "
     "\"over-complex trees that do not generalize the data well\" (scikit-learn developers, n.d.-a). The "
     "0.1799 is also the highest training accuracy any model could reach with this one feature, because days "
     "with the same number of installs often have different numbers of uninstalls. On new data, the tree "
     "drops to 0.0225.")
para("I expected the random forest to clearly win, so I tested 30 different train/test splits to see whether "
     "my result was just luck. The random forest had higher test accuracy on 12 splits, the decision tree on "
     "13, and they tied on 5, so neither model is consistently better here. I think the reason is that this "
     "model uses only one feature. Breiman (2001) explains that \"the generalization error of a forest of tree "
     "classifiers depends on the strength of the individual trees in the forest and the correlation between "
     "them\" (p. 5). A random forest normally lowers that correlation by letting each tree consider a random "
     "subset of the features at each split (scikit-learn developers, n.d.-b). With only one feature, every "
     "tree has to split on daily device installs, so the only difference between the trees is their bootstrap "
     "sample. The trees end up very similar, and voting among similar trees does not cancel out many errors.")
para("Finally, both accuracy scores are very low because exact-match accuracy is a hard measure for a count. "
     "Predicting 75 when the answer is 76 counts as wrong, the same as predicting 300. A simple baseline that "
     "always guesses the most common uninstall value in the training data (68) would score 0.0241, which is "
     "slightly higher than both models. This tells me that accuracy is not a good way to judge models that "
     "predict a number, and that the mean absolute error gives a much clearer picture.")

# ---------------- Item 8 ----------------
page_break()
h1("Item 8: Final Conclusions on Installs Versus Uninstalls for Daily Devices")
para("Overall, the data shows a strong, positive, and mostly linear relationship between daily device "
     "installs and daily device uninstalls. The correlation is 0.91, and a single straight line explains "
     "about 83% of the variation in uninstalls. Uninstalls rise by about 0.77 for every additional install. "
     "Over the full period, the app had 181,744 device installs and 156,650 device uninstalls, so about 86 "
     "devices were removed for every 100 that were added. The app was still growing, but slowly. On typical "
     "days, the model shows that the app gains more devices when installs are high, while on quiet days below "
     "about 36 installs, it is expected to lose devices. The large spike in July and August 2016 also shows "
     "that a surge in installs comes with a surge in uninstalls, so a jump in installs does not translate into "
     "the same jump in active devices.")
para("In terms of the models, linear regression was the best fit for this data set among the three models in "
     "the assignment. It had the lowest test error of the three (13.12 uninstalls), its predictions followed "
     "the real trend, and its intercept and coefficient tell a clear and simple story. This matches what the "
     "professor said in the seminar: linear regression is the right choice when the trend is roughly a "
     "straight line and we want a simple, explainable result. The decision tree and random forest classifiers "
     "had very low accuracy, but I do not think that means tree models are bad for this data. They were set up "
     "as classifiers for a target that is really a number, and they only had one feature to work with. When I "
     "switched to a RandomForestRegressor, it had the lowest error of all (12.41), although it gives up the "
     "simple equation that makes linear regression so easy to explain.")
para("If I were to continue this analysis, I would try two things. First, I would add more features, such as "
     "the day of the week, the month, or the daily device upgrades, since installs alone leave a lot of the "
     "variation in uninstalls unexplained. That would also give a random forest more features to choose from, "
     "which should make its trees less similar to one another. Second, I would compare the models with "
     "measures made for numeric predictions, like mean absolute error and R², instead of exact-match accuracy. "
     "My main takeaway from this assignment is that choosing the right type of model for the target, "
     "regression for a number and classification for a category, matters as much as choosing the algorithm.")

# ---------------- References ----------------
page_break()
h1("References")
refs = [
    "Breiman, L. (2001). Random forests. Machine Learning, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324",
    "Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., "
    "Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., "
    "Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine "
    "Learning Research, 12, 2825–2830. https://jmlr.org/papers/v12/pedregosa11a.html",
    "scikit-learn developers. (n.d.-a). Decision trees. scikit-learn documentation. Retrieved November 4, "
    "2026, from https://scikit-learn.org/stable/modules/tree.html",
    "scikit-learn developers. (n.d.-b). Ensembles: Gradient boosting, random forests, bagging, voting, "
    "stacking. scikit-learn documentation. Retrieved November 4, 2026, from "
    "https://scikit-learn.org/stable/modules/ensemble.html",
    "scikit-learn developers. (n.d.-c). Linear models. scikit-learn documentation. Retrieved November 4, "
    "2026, from https://scikit-learn.org/stable/modules/linear_model.html",
]
for ref in refs:
    p = doc.add_paragraph(ref)
    pf = p.paragraph_format
    pf.line_spacing = 2.0
    pf.left_indent = Inches(0.5)
    pf.first_line_indent = Inches(-0.5)

doc.core_properties.title = "IN404 Unit 9 Assignment"
doc.core_properties.author = "Shubham Raj"
doc.save(OUT)
print("saved", OUT)
