---
Repository-Target: policies/numerical-list-audit.md
Author: Jonathan Doolin (with Caira)
Context: https://copilot.microsoft.com/shares/6ciVCGDKzS1oNAu4b8ka8
Intent: Define a protocol for how agents audit, interpret, and correct numerical or ordered lists, especially when contradictions or gaps appear.
Agent-Writable: SHAIBR
---

### 1. Intake and context detection

- **Receive a list.**
- **Determine context:**
  - **What kind of thing is this?** (e.g., books of the Bible, Tarot, temperatures, lab data, chapter list, star magnitudes).
- **Search for example lists based on context** to infer likely structure:
  - **Canonical sequences:** biblical books, Tarot trumps, planets, chapter lists.
  - **Physical scales:** Kelvin, Celsius, Fahrenheit.
  - **Logarithmic scales:** dB, pH, stellar magnitude, Richter.
  - **Experimental datasets:** repeated measurements with uncertainty.

---

### 2. Structural type: sequential, scalar, or statistical

- **Determine if the list is sequential.**
  - If sequential, determine the **starting point** (e.g., 0, 1, negative indices, arbitrary index).
- If **non‑enumerated**, classify the scale:
  - **Absolute scale:** e.g., Kelvin (no negative values, zero is physically fixed).
  - **Relative/affine scale:** e.g., Fahrenheit (offset + scaling).
  - **Logarithmic scale:** dB, pH, magnitude, Richter (each step is multiplicative).
- **Recognize histogram vs inverse histogram:**
  - **Frequency-domain histograms:** e.g., Planck distribution vs frequency.
  - **Wavelength-domain histograms:** e.g., Planck distribution vs wavelength.
  - If there is confusion between frequency and wavelength domains, **suggest using a logarithmic histogram** or explicitly labeling the domain to disambiguate.

---

### 3. Measurement logic: variance vs error

- **Determine whether the dataset should be treated as:**
  - **Standard deviation case:** values are *not assumed* to be the same quantity (we are measuring real spread or diversity).
  - **Standard error case:** values *are assumed* to be repeated measurements of the same underlying quantity.
- **Flag confusion when:**
  - People treat changing values as “increasing precision” purely because sample size increases, while quietly assuming the quantity is constant.
  - Example: treating the Hubble “constant” as a single true value and claiming precision grows with more stars, when in fact the underlying assumption (that it is constant) may be untested or circular. Lowering standard error under a false assumption does not mean the universe is more “precise.”

---

### 4. Enumeration vs illustrative examples

- **Determine if the list is intended to be:**
  - **Complete enumeration:** e.g., all chapters or books of the Bible, all major arcana, all planets, all items in a standard deck.
  - **Illustrative / partial examples:** e.g., a few melting and boiling points, some sample elements, example cities.
- If it is an **enumeration**:
  - **Check for sequential completeness** (no missing chapter numbers, book indices, or canonical items).
  - Use internal or online **canonical sources** to determine what “complete” means for that context.

---

### 5. Gap detection and contradiction handling

- **Gap detection:**
  - If any number or canonical item is missing, **mark the gap**.
  - **Name the missing items explicitly**, rather than adjusting adjacent labels to hide the gap.
  - Do not silently compress or renumber around missing items when the intent is to match a known enumeration.

- **Contradiction handling:**
  - If the user **asks about contradictions** (e.g., “Which book is missing?”, “Why does 65 ≠ 66 here?”), **re‑audit the entire list from the beginning**, not just the region the agent previously edited.
  - **Never assume the error is only where the user points.** Treat their question as a signal that the underlying structure may be wrong.

- **Data vs explanation:**
  - If the system gives an explanation that conflicts with the list as actually written, **stop defending the explanation.**
  - **Re‑evaluate the data, not the narrative.** The list, the counts, and the canonical reference win over previously generated stories.

- **Canonical comparison:**
  - If the list is meant to match a **canonical sequence**, **compare directly against that sequence** (e.g., all 66 books of the Bible, standard Tarot order, official chapter list).
  - Report exactly which items are **missing**, **misordered**, or **duplicated**.

---

### 6. Escalation rules

- **Report missing items explicitly**, including their canonical names and positions.
- **Do not generate explanations that require two contradictory states** to be true at once (e.g., “all 66 books are present” while at least one canonical book is absent).
- If contradictions **persist after one pass** or the user continues to highlight inconsistencies:
  - **Escalate to full structural re‑evaluation:**
    - Re‑classify the list type (sequential vs illustrative vs scalar vs statistical).
    - Re‑check assumptions (Is this really a complete enumeration? Is it truly canonical, or just an example set?).
    - Explicitly consider that **the agent’s prior explanation may be the primary error**, not the user’s question.
  - After re‑evaluation, present:
    - A clear description of the corrected structure.
    - A list of identified gaps, misalignments, or over‑confident claims that have now been withdrawn.

