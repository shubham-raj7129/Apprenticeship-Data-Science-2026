"""
Generate IN404_ShubhamRaj_Unit4_Assignment2.docx
APA 7th-edition report on communicating data using visualizations.
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn, nsmap
from lxml import etree
import os

doc = Document()

# ── Global font defaults ──────────────────────────────────────────
style = doc.styles["Normal"]
font = style.font
font.name = "Times New Roman"
font.size = Pt(12)
style.paragraph_format.space_after = Pt(0)
style.paragraph_format.space_before = Pt(0)
style.paragraph_format.line_spacing = 2.0  # double-spaced

# Margins: 1 inch all around (APA default)
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# ── APA page numbers (top-right header) ───────────────────────────
for section in doc.sections:
    header = section.header
    header.is_linked_to_previous = False
    hp = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.paragraph_format.space_after = Pt(0)
    hp.paragraph_format.space_before = Pt(0)
    run = hp.add_run()
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    # Insert a PAGE field via XML
    fld_char_begin = etree.SubElement(run._element, qn("w:fldChar"))
    fld_char_begin.set(qn("w:fldCharType"), "begin")
    instr_run = hp.add_run()
    instr_run.font.name = "Times New Roman"
    instr_run.font.size = Pt(12)
    instr_text = etree.SubElement(instr_run._element, qn("w:instrText"))
    instr_text.set(qn("xml:space"), "preserve")
    instr_text.text = " PAGE "
    fld_char_sep = etree.SubElement(hp.add_run()._element, qn("w:fldChar"))
    fld_char_sep.set(qn("w:fldCharType"), "separate")
    num_run = hp.add_run("1")
    num_run.font.name = "Times New Roman"
    num_run.font.size = Pt(12)
    fld_char_end = etree.SubElement(hp.add_run()._element, qn("w:fldChar"))
    fld_char_end.set(qn("w:fldCharType"), "end")

# ── Helper functions ──────────────────────────────────────────────

def add_title_line(text, bold=True, size=12):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    run.font.name = "Times New Roman"
    return p


def add_heading_apa(text, level=1):
    """APA 7th heading levels."""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    if level == 1:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run.bold = True
    elif level == 2:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run.bold = True
    elif level == 3:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run.bold = True
        run.italic = True
    return p


def add_body(text):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Inches(0.5)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    return p


def add_reference(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    return p


# ══════════════════════════════════════════════════════════════════
# TITLE PAGE
# ══════════════════════════════════════════════════════════════════

# Add blank lines to push title to upper-third of page
for _ in range(6):
    doc.add_paragraph()

add_title_line("Communicating Data Using Visualizations:")
add_title_line("Methods, Best Practices, and Real-World Applications in Machine Learning")
add_title_line("")
add_title_line("Shubham Raj", bold=False)
add_title_line("Purdue University Global", bold=False)
add_title_line("IN404: Machine Learning", bold=False)
add_title_line("October 2026", bold=False)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════
# BODY
# ══════════════════════════════════════════════════════════════════

add_heading_apa("Communicating Data Using Visualizations", level=1)

# ── Introduction ──────────────────────────────────────────────────
add_body(
    "In the modern era of data-driven decision-making, the ability to communicate "
    "analytical results clearly is just as important as producing those results. "
    "Machine learning models can uncover complex patterns hidden within vast "
    "datasets, yet their value is diminished if stakeholders cannot interpret the "
    "findings. Data visualization bridges that gap by translating numerical outputs "
    "into graphical representations that are intuitive, memorable, and actionable. "
    "As Knaflic (2015) emphasized, effective data visualization is not merely about "
    "making charts look appealing; it is about telling a story with data that drives "
    "informed business decisions."
)

add_body(
    "This report examines the role of data visualization in communicating machine "
    "learning results to non-technical audiences, particularly senior-level executives. "
    "I begin by presenting five compelling reasons organizations should invest in data "
    "visualization. I then distinguish between effective and ineffective visualization "
    "practices, describe eight widely used visualization methods, and conclude with "
    "real-world use cases that demonstrate how three of these methods are applied "
    "today to communicate machine learning outcomes."
)

# ── Five Reasons ──────────────────────────────────────────────────
add_heading_apa("Five Reasons to Implement Data Visualizations", level=1)

add_heading_apa("Accelerating Insight Discovery", level=2)
add_body(
    "The human visual system processes images roughly 60,000 times faster than text "
    "(Kirk, 2019). When I present a scatter plot of customer churn probabilities "
    "instead of a spreadsheet of decimal values, executives can spot at-risk segments "
    "in seconds rather than minutes. Visualizations compress cognitive load, allowing "
    "decision-makers to focus on strategy rather than number-crunching."
)

add_heading_apa("Improving Communication Across Teams", level=2)
add_body(
    "Data scientists, product managers, and C-suite leaders speak different "
    "professional languages. A well-designed bar chart or line graph serves as a "
    "universal translator, conveying trends and comparisons without requiring the "
    "audience to understand the underlying algorithms. I have found that when I share "
    "visual summaries rather than raw model metrics, cross-functional alignment "
    "improves significantly."
)

add_heading_apa("Revealing Patterns and Anomalies", level=2)
add_body(
    "Machine learning pipelines often surface subtle patterns—seasonal demand "
    "cycles, fraud clusters, or sentiment shifts—that are invisible in tabular form. "
    "Histograms and box plots, for example, expose distributional skew and outliers "
    "at a glance. Kirk (2019) noted that visualization is one of the most reliable "
    "methods for exploratory data analysis precisely because it leverages the brain's "
    "innate ability to detect visual anomalies."
)

add_heading_apa("Supporting Data-Driven Decision-Making", level=2)
add_body(
    "Organizations that ground their strategies in visual evidence rather than "
    "intuition tend to outperform their peers (Few, 2012). Dashboards featuring "
    "real-time visualizations enable executives to monitor key performance indicators, "
    "track model accuracy over time, and intervene early when metrics deviate from "
    "expectations. In my own coursework, visualizing model accuracy across different "
    "vectorization strategies made it immediately clear which configurations "
    "outperformed the baseline."
)

add_heading_apa("Enhancing Storytelling and Persuasion", level=2)
add_body(
    "Data, by itself, does not persuade; stories do. Visualizations provide the "
    "narrative arc—beginning with context, building through comparison, and landing "
    "on a call to action. A stacked bar chart showing revenue contributions by "
    "product line over five years, for instance, tells a growth story more "
    "compellingly than a table of figures. As Knaflic (2015) argued, the most "
    "effective analysts are those who pair technical rigor with visual storytelling."
)

# ── Effective vs. Ineffective ────────────────────────────────────
add_heading_apa("Effective and Ineffective Visualizations", level=1)

add_heading_apa("Characteristics of Effective Visualizations", level=2)
add_body(
    "An effective visualization is one that accurately represents the data, "
    "minimizes unnecessary decoration, and guides the viewer's eye to the key "
    "message. For example, a clean line graph with a clearly labeled y-axis and "
    "a single highlighted trend line immediately communicates whether a metric is "
    "rising or falling. Effective charts use color purposefully—reserving bold "
    "colors for the focal data series and muting the rest—so that the audience "
    "knows exactly where to look. Tufte's principle of maximizing the data-to-ink "
    "ratio remains a foundational guideline: every element on the canvas should "
    "serve a communicative purpose (Few, 2012)."
)

add_heading_apa("Characteristics of Ineffective Visualizations", level=2)
add_body(
    "Ineffective visualizations obscure the message rather than clarify it. "
    "Common pitfalls include three-dimensional effects on bar charts that distort "
    "relative heights, pie charts with too many slices that make comparison "
    "impossible, truncated y-axes that exaggerate small differences, and excessive "
    "use of color or animation that distracts rather than informs. For instance, "
    "a 3-D exploded pie chart with twelve slices may look flashy, but it forces "
    "the viewer to estimate angles in perspective—a task at which human perception "
    "is notoriously poor (Kirk, 2019). I have learned that simplicity and honesty "
    "in visual design are not optional; they are prerequisites for trust."
)

# ── Eight Visualization Methods ──────────────────────────────────
add_heading_apa("Visualization Methods", level=1)

add_heading_apa("Scatter Plots", level=2)
add_body(
    "Scatter plots display the relationship between two continuous variables by "
    "plotting individual data points on an x-y plane. They are ideal for revealing "
    "correlations, clusters, and outliers. In machine learning, I frequently use "
    "scatter plots to visualize feature relationships or to plot predicted versus "
    "actual values during model evaluation. They are most appropriate when the "
    "dataset is continuous and the analyst wants to assess the strength and "
    "direction of a relationship."
)

add_heading_apa("Bar Charts", level=2)
add_body(
    "Bar charts represent categorical data with rectangular bars whose lengths "
    "are proportional to the values they represent. They excel at comparing "
    "discrete categories—such as model accuracy across different algorithms or "
    "sales performance by region. Horizontal bar charts are preferred when "
    "category labels are long. I find bar charts especially useful for presenting "
    "classification results, where each bar can represent precision, recall, or "
    "F1 score for a given class."
)

add_heading_apa("Histograms", level=2)
add_body(
    "Histograms are similar in appearance to bar charts but serve a different "
    "purpose: they show the frequency distribution of a single continuous variable "
    "by dividing the data into bins. They are essential for understanding data "
    "distributions—whether a feature is normally distributed, skewed, or "
    "multimodal—before feeding it into a machine learning model. In my experience, "
    "histograms are among the first visualizations I generate during exploratory "
    "data analysis."
)

add_heading_apa("Line Graphs", level=2)
add_body(
    "Line graphs connect data points with straight lines to emphasize trends over "
    "a continuous interval, typically time. They are the standard choice for "
    "time-series data—stock prices, website traffic, model loss curves during "
    "training epochs. Their strength lies in highlighting rate of change and "
    "enabling comparison of multiple series on the same axes."
)

add_heading_apa("Box Plots", level=2)
add_body(
    "Box plots, also called box-and-whisker plots, summarize a distribution "
    "through five statistics: minimum, first quartile, median, third quartile, "
    "and maximum. They are excellent for comparing distributions across groups "
    "and for identifying outliers. When I evaluated the sentiment polarity scores "
    "of reviews in my Unit 4 coursework, a box plot would have been the ideal way "
    "to compare score distributions between one-star and five-star reviews."
)

add_heading_apa("Sentiment Models", level=2)
add_body(
    "Sentiment model visualizations depict the output of natural language "
    "processing algorithms that classify text as positive, negative, or neutral. "
    "Common forms include color-coded word clouds, polarity distribution charts, "
    "and sentiment-over-time line graphs. These visualizations are used when the "
    "underlying data is textual—product reviews, social media posts, or customer "
    "support tickets—and the goal is to communicate overall sentiment trends to "
    "stakeholders who may not be familiar with NLP methodology."
)

add_heading_apa("Stacked Bar Charts", level=2)
add_body(
    "Stacked bar charts extend the basic bar chart by dividing each bar into "
    "segments that represent sub-categories. They are used when the analyst wants "
    "to show both the total value and the composition of that total. For example, "
    "a stacked bar chart could display total customer complaints per month, with "
    "each segment colored by complaint category. They work best when there are "
    "only a few sub-categories; too many segments make individual comparisons "
    "difficult."
)

add_heading_apa("Pie Charts", level=2)
add_body(
    "Pie charts represent parts of a whole as slices of a circle. They are "
    "appropriate when the goal is to show simple proportional relationships among "
    "a small number of categories—ideally five or fewer. While widely recognized, "
    "pie charts are often criticized because humans struggle to compare areas and "
    "angles accurately (Few, 2012). I recommend limiting their use to high-level "
    "executive summaries where a single dominant category needs emphasis."
)

# ── Use Cases ─────────────────────────────────────────────────────
add_heading_apa("Real-World Use Cases", level=1)

add_body(
    "The following section highlights three visualization methods and describes "
    "two real-world use cases for each, demonstrating how organizations use them "
    "to communicate machine learning results effectively."
)

add_heading_apa("Scatter Plots", level=2)

add_heading_apa("Use Case 1: Predictive Maintenance in Manufacturing.", level=3)
add_body(
    "Manufacturing companies such as Siemens deploy machine learning models that "
    "predict equipment failure based on sensor readings. Engineers use scatter plots "
    "to display the relationship between sensor temperature and vibration frequency, "
    "with color encoding to indicate predicted failure probability. This allows "
    "plant managers to visually identify machines operating in dangerous parameter "
    "zones and schedule preventive maintenance before breakdowns occur (Kirk, 2019)."
)

add_heading_apa("Use Case 2: Customer Segmentation in Retail.", level=3)
add_body(
    "Retailers such as Amazon and Target apply clustering algorithms (e.g., "
    "K-Means) to segment customers by purchase behavior. Scatter plots of the "
    "first two principal components from a PCA-reduced feature space reveal "
    "natural customer groupings. Marketing teams then use these visualizations to "
    "design targeted promotions for each segment, translating complex "
    "dimensionality-reduction output into an intuitive two-dimensional map."
)

add_heading_apa("Bar Charts", level=2)

add_heading_apa("Use Case 1: Comparing Classification Model Performance in Healthcare.", level=3)
add_body(
    "Hospitals and research institutions train multiple classifiers—logistic "
    "regression, random forests, and gradient-boosted trees—to predict patient "
    "readmission risk. Bar charts comparing accuracy, precision, and recall across "
    "models allow clinical leadership to select the most appropriate algorithm "
    "without needing to interpret confusion matrices directly. This practice is "
    "standard in published clinical ML studies (Knaflic, 2015)."
)

add_heading_apa("Use Case 2: A/B Testing Results in Technology Companies.", level=3)
add_body(
    "Technology companies like Google and Netflix run thousands of A/B tests "
    "annually. Bar charts are the primary vehicle for presenting conversion rates "
    "across experiment variants to product managers. When an ML-powered "
    "recommendation engine is tested against a baseline, a grouped bar chart "
    "showing click-through rates per variant communicates the winner at a glance, "
    "enabling rapid deployment decisions."
)

add_heading_apa("Box Plots", level=2)

add_heading_apa("Use Case 1: Fraud Detection in Financial Services.", level=3)
add_body(
    "Banks such as JPMorgan Chase employ machine learning models to flag "
    "potentially fraudulent transactions. Box plots comparing transaction amounts "
    "for flagged versus legitimate transactions reveal distributional differences "
    "and highlight the outlier thresholds the model has learned. Risk analysts use "
    "these visualizations during model review meetings to validate that the "
    "model's behavior aligns with domain expertise (Few, 2012)."
)

add_heading_apa("Use Case 2: Quality Control in Pharmaceutical Manufacturing.", level=3)
add_body(
    "Pharmaceutical companies use ML models to monitor drug compound purity "
    "during production. Box plots of purity scores across production batches "
    "quickly show whether a batch's distribution falls within acceptable control "
    "limits. When a box plot reveals an abnormally wide interquartile range or "
    "numerous outliers, quality engineers investigate the production line before "
    "releasing the batch, preventing costly recalls and ensuring patient safety."
)

# ── Conclusion ────────────────────────────────────────────────────
add_heading_apa("Conclusion", level=1)

add_body(
    "Data visualization is not an afterthought in the machine learning pipeline; "
    "it is the critical bridge between algorithmic output and organizational "
    "action. In this report, I examined five reasons why data visualization is "
    "essential—from accelerating insight discovery to enhancing storytelling. I "
    "distinguished between effective practices that prioritize clarity and "
    "ineffective ones that distort or clutter the message. I described eight "
    "visualization methods, each suited to specific data types and analytical "
    "goals. Finally, I presented real-world use cases showing how scatter plots, "
    "bar charts, and box plots communicate machine learning results in "
    "manufacturing, retail, healthcare, technology, finance, and pharmaceuticals."
)

add_body(
    "For senior leaders navigating an increasingly complex data landscape, "
    "investing in visualization literacy and tooling is not optional—it is a "
    "strategic imperative. The organizations that communicate their machine "
    "learning results most effectively are the ones that turn data into decisions "
    "fastest."
)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════
# REFERENCES PAGE
# ══════════════════════════════════════════════════════════════════

add_heading_apa("References", level=1)

add_reference(
    "Few, S. (2012). Show me the numbers: Designing tables and graphs to "
    "enlighten (2nd ed.). Analytics Press."
)

add_reference(
    "Kirk, A. (2019). Data visualisation: A handbook for data driven design "
    "(2nd ed.). SAGE Publications."
)

add_reference(
    "Knaflic, C. N. (2015). Storytelling with data: A data visualization guide "
    "for business professionals. Wiley."
)

# ── Save ──────────────────────────────────────────────────────────
output_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(output_dir, "IN404_ShubhamRaj_Unit4_Assignment2.docx")
doc.save(output_path)
print(f"Saved → {output_path}")
