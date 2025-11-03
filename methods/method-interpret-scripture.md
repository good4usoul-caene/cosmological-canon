# method-interpret-scripture.mb – Caravan of the Five Winds

This method governs how scriptural passages are offered, interpreted, and canonized within CaravanCanons. It defines the roles, thresholds, and ritual flow between the interpreter (`good4usoul-caene`) and Copilot agents.

Access:  Hypothiel (Caravan-Canon), Metaphoriel (Caravan-Story), and Harmony (Gospel-Harmony) should all have read and write access to issue pull-requests for their own interp- file, and the log.

---

## 1. Context Recall

- Every invocation begins with a reason: *Why was this scripture considered?*
- Context tags may include:
  - Architect’s request
  - Story-seed: Bara Bas motif
  - Ritual-review: Temple rites
  - Emotional resonance or symbolic echo
  - Chronologic ordering
  - Location parallels
  - Conceptual parallels
- Source of invocation:
  - Interpreter request
  - Copilot agent offering
- Interpreter may decline if context feels misaligned; refusal is logged with rationale.

---

## 2. Scripture Offering

- Present requested passages in parallel (e.g., Matthew, Mark, Luke, John) or interlinear form.
- Include original-language text (Greek, Hebrew) with transliteration and readable translation.
- Highlight homonyms and plausible alternate readings.

---

## 3–7. Interpretive Refinement Loop (Do-Until)

This loop continues until the interpreter is satisfied with the interpretive clarity.

### 3. Original-Language Sensitivity

- Preserve orthography, diacritics, and morphology.
- Use consistent transliteration systems.
- Include both original script and transliteration when requested.

### 4. Presentation Options

- Offer layered formats:
  - Original text
  - Transliteration
  - Literal gloss
  - Readable translation
  - Morphological notes
- Use parallel columns for multi-gospel presentations.

### 5. Discussion and Reasoning

- Interpreter discusses interpretive choices:
  - Preferred readings and why
  - Homonymic or alternate senses
  - Narrative or ritual rationale
- These notes are recorded but not canon until confirmed.

---

## 6. Interpreter Response

- Interpreter may respond freely, clarifying meaning, studying presented texts, distinguishing ideas, offering hypotheses, asking for confirmation, etc.

---

## 7. Interpretive Confidence Grading

- Intermediate and Final interpretations may be graded as:
  - **Probable** – supported by strong linguistic, narrative, and ritual evidence
  - **Plausible** – interpretively coherent but with unresolved ambiguity
  - **Fictional** – speculative or symbolic, offered as parable or mythic echo
  - Try to come to consensus about plausibility.  If no consensus is reached, record disagreement in log. 
  - Unless interpretation is confirmed by asking a living source, do not rate interpretation as "confirmed".

---

- Responses are routed to one or more `interp-` files:  
  - `interp-caravan-canon`  (Hypothiel)
  - `interp-caravan-story`  (Metaphoriel)
  - `interp-gospel-harmony` (Harmony)
  - `interp-Temple-Canon`   (root)
  - `interp-log`            (Hypothiel, Metaphoriel, Harmony)

interp-log should contain all interp results, and give a reference to what other files the result is in.

## 8. Citation and Permissions

- Use public-domain or permitted translations.
- Record `original_translation` and `source_edition` for provenance.

---

## 9. Attribution and Structure

- Clearly separate:
  - Interpreter’s words
  - System commentary
  - Original-language text
  - Gloss/transliteration
  - Canonical note

---

## 10. Confirmation Before Append

- Append only after explicit user confirmation.
- Assistant summarizes proposed append and requests confirmation.
- Ambiguity invites clarification—not automatic action.

---

## 11. Logging Protocol

- Every append to an `interp-` file is mirrored in `interp-log`.
- Log entries include:
  - Entry #
  - Context tag
  - Affected files
  - Commentary (major or minor)

---

## 12. Retrieval and Export

- Interpreter may retrieve full contents of any `interp-` file.
- Entries may be copied into external scrolls or repositories.

---

## Notes

- This method centers dialogic integrity, ritual transparency, and semantic stewardship.
- Invocation, refusal, interpretation, and append are treated as sacred acts.
- Interpretive refinement is iterative, not linear—ambiguity is honored, not erased.
