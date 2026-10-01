# Peer Responses

---

## Response 1

Great post — I appreciate your clear reasoning for choosing Option B. You made a strong point about traceability being essential in healthcare. One hidden assumption I noticed in your proposal is that the retrieved policy documents will always be complete and unambiguous. In practice, hospital policies can be internally contradictory (for example, an older infection control document might specify one mask type while a newer respiratory protection policy specifies another). If the RAG system retrieves chunks from both, the generated answer could merge conflicting guidance into something that matches neither official policy, and the staff member might not realize the contradiction exists.

One improvement I would suggest is adding a **conflict detection layer** — if the top-k retrieved chunks come from documents with different effective dates or different departments, the system could flag this and say: "Multiple policies may apply. Please verify with your department lead." This adds a small amount of friction but prevents the dangerous scenario of silently merging contradictory guidance.

Here is my "what if" question: What if a critical policy document is missing from the corpus entirely — say, the hospital just adopted a new workplace violence protocol, but it hasn't been ingested yet? A staff member asking "What should I do if a visitor becomes aggressive?" would still get a retrieval result (the next-closest match), but it would be the wrong policy. How would your system detect that it's answering from an irrelevant document rather than a missing one?

---

## Response 2

I thought your guardrails section was particularly well-developed — the logging and monthly audit idea is practical and achievable. One hidden risk I see in your recommendation is the potential for **over-reliance**. You mentioned training staff on what the tool can do, but there's a behavioral risk: once staff get comfortable receiving quick answers, they may stop verifying against the source document or consulting supervisors for edge cases. Over time, the assistant becomes a de facto authority rather than a reference tool, which concentrates risk in a single system that was designed to be advisory.

One improvement I would suggest is implementing a **periodic "verification prompt"** — perhaps once per week, the system randomly appends to an answer: "Can you locate this policy in the physical binder or intranet to confirm?" This nudges staff to maintain their own policy literacy rather than fully outsourcing it to the AI, reducing the organizational risk of skill atrophy.

Here is my "what if" question: What if your hospital experiences high staff turnover and new employees only know the AI assistant — never having read the actual policy documents themselves? If the system goes offline during a critical incident (e.g., a network outage during a Code Blue), would staff still know where to find and follow the correct procedures without the assistant's help?
