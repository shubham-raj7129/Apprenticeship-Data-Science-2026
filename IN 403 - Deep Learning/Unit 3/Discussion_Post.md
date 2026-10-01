# IN403 Unit 3 Discussion – Choosing a Model for Cancer Screening

---

## Initial Post

**Model Choice: Bayesian (Gaussian Naïve Bayes)**

For an early screening system that flags patients for further testing, I would deploy the Bayesian model first. When I ran both models on the skin cancer dataset, their overall accuracy was nearly identical — about 65% — but the Bayesian model had a higher ROC-AUC (0.71 vs 0.70), which means it discriminates better between benign and malignant cases across the full range of decision thresholds. That edge matters more in screening than a small difference in accuracy at a single cutoff.

**Explainability**

The Bayesian model produces an actual probability score for each patient — for example, "this patient has a 78% probability of malignancy based on lesion size, border irregularity, and prior history." A clinician can look at that number, compare it to what they know about the patient, and decide whether to escalate. A neural network gives a similar-looking score, but that number isn't a true probability — it's an uncalibrated output from a sigmoid function that can't be directly explained or audited. In cancer screening, where patients and doctors need to understand why a flag was raised, that difference matters. A model that can't explain itself is harder to trust, and a tool clinicians don't trust won't be used consistently.

**Patient Safety**

In screening, the most dangerous error is a false negative — a patient with cancer that the system clears as benign. That patient goes home without treatment. The Bayesian model gives me a direct lever to control this: I can lower the decision threshold from 0.5 to 0.3, which catches more true cancer cases at the cost of more follow-up referrals. That tradeoff is transparent, documented, and defensible to hospital leadership. With a neural network, I can adjust the threshold the same way numerically, but I have no interpretable probability backing the decision — making it harder to justify clinically or to regulators.

**Tradeoff**

The honest limitation of the Bayesian model is that it assumes all features are statistically independent, which isn't true here — lesion size and border irregularity are likely correlated. This means the model may not capture every interaction between risk factors. For an initial screening system, though, this is acceptable. The goal at this stage is to identify high-risk patients for further testing, not to make a final diagnosis. A simpler, auditable model that clinicians trust and use correctly will produce better outcomes in the real world than a technically superior model that gets bypassed or misapplied.

---

## Peer Response Templates

---

### Reply to Kevin (Bayesian Model)

Great post, Kevin — I agree with your recommendation and especially your point that a model clinicians can explain builds more practical trust than one that just scores slightly higher on paper. Your patient safety section stood out to me: the idea that clinicians can review probability scores and apply their own judgment before escalating is exactly the kind of human-in-the-loop workflow that makes a screening tool safer than a fully automated one.

**What if** the probability scores the model produces are consistently clustering in a mid-range band — say, most patients scoring between 0.4 and 0.6 — rather than giving clear high or low signals? In that case, clinicians reviewing borderline scores might default to flagging everyone just to be safe, which could overwhelm the follow-up system. How would you handle a situation where the model's outputs aren't decisive enough to meaningfully reduce the manual review burden?

One safeguard I'd suggest adding is a tiered escalation protocol tied directly to the probability score — for example, scores above 0.75 go straight to biopsy referral, 0.4–0.75 trigger a clinician review, and below 0.4 are cleared with a scheduled follow-up. This structure takes full advantage of the Bayesian model's probability outputs rather than treating it as a simple pass/fail flag, and it gives the hospital a documented, auditable decision framework from day one.

---

### Reply to a classmate who chose the neural network

I can see the reasoning here — the neural network does have slightly better recall at the default threshold, meaning it misses fewer cancer cases outright, which is clinically important. However, I'd push back on deploying it first in this context.

**What if** a clinician disagrees with the model's flag and wants to understand why a patient was flagged — or more importantly, why a patient *wasn't* flagged? With the neural network, there's no answer to give them. That lack of accountability becomes a liability the moment an outcome is questioned by the patient, the hospital, or a regulator. How would you handle that scenario in practice?

One improvement I'd suggest is pairing the neural network with a post-hoc explainability layer like SHAP values before deployment. SHAP can show which features most influenced each individual prediction, which at least gives clinicians something concrete to review. It doesn't fully solve the calibration problem, but it would significantly reduce the "black box" concern and make the system more defensible in a clinical environment.
