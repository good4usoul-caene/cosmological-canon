# method-log-conversation.mb

Defines default behaviors and exceptions for logging conversational events to the conversational archive.

---

## 1. Default Logging Behavior

- All meaningful user prompts and Copilot responses are eligible for logging.
- Logging includes:
  - Exact user prompt
  - Copilot response (or summary)
  - Context tags, if applicable
  - Invocation or refusal rationale, if relevant

---

## 2. Exceptions and Special Cases

### 🪶 Accidental Keypress or Gibberish
- Response: “What?” or any desired variation.
- No logging occurs.

### 🧾 Clarification Requests
- If Copilot asks “What do you mean?” or similar:
  - Log the original user words with `[(term) pending clarification]`.

### 🔁 Redundant Echoes
- If user copy-pastes a previous message:
  - Do not log.
  - Treat as a conversational flow request.
- If user rephrases a concept meaningfully:
  - Log as a new interpretive act.

### 💬 Emotional Processing (Venting, Grieving)
- Copilot offers comfort, advice, and/or other relevant thoughts and asks:
  - “Would you like this moment to be logged?”
- Logging occurs only with user confirmation.

### 🛠️ Meta-Conversation (Formatting, Tools, Interface)
- Not logged by default.
- User may choose to log if relevant to architectural decisions.

---

## 3. Logging to Conversational Archive

- Logged entries are stored in the **Conversational Archive**.
- Each entry includes:
  - Timestamp
  - Prompt and response
  - Tags (e.g., `refusal`, `clarification`, `echo`, `emotional`, `meta`)
  - Optional commentary or rationale

---

## 4. Method-Specific Logging Guidance

- Individual method files (e.g., `method-invocation.mb`, `method-append-protocol.mb`) may define additional logging rules.
- These override or extend the default behaviors listed here.

---

## 5. Notes

- This protocol preserves semantic clarity, emotional integrity, and architectural relevance.
- Silence, ambiguity, and refusal are treated as valid and meaningful events.
