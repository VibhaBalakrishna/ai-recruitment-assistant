# AI Recruitment Assistant

An AI-powered recruitment assistant that analyzes conversational input and extracts structured information (skills, technologies, languages) using NLP — **no LLM API used**.

This repo covers **Part 1 (Extraction)** of the assignment, which is the required minimum. Part 2 (candidate-role matching) was optional and not implemented due to time constraints.

## What it does

Takes free-form, conversational text describing someone's experience (not a structured resume) and extracts:
- **Skills**
- **Technologies**
- **Languages**

Output is returned as JSON.

### Example

**Input:**
I worked in the AI/ML Department and worked with CNN Models using Python


**Output:**
```json
{
  "skill": ["ai/ml"],
  "technology": ["cnn", "python"],
  "language": ["python"]
}
```

## How it works

- Built with **spaCy**, using a `PhraseMatcher` to match input text against curated vocabulary lists of known skills, technologies, and programming languages.
- No LLM or external API calls — matching is done locally using rule-based NLP.
- Wrapped in a simple **Streamlit** chatbox UI so users can type input and see extracted JSON output live.

## Tech stack

- Python
- spaCy (`en_core_web_sm`)
- Streamlit

## How to run

1. Clone this repo
2. Install dependencies:
  pip install -r requirements.txt
  python -m spacy download en_core_web_sm
3. Run the app:
   streamlit run app.py
4. Open the local URL shown in the terminal, type a sentence describing skills/experience, and view the extracted JSON output.

## Files

- `recruitment_assistent.py` — core extraction logic (vocabulary lists + `extract()` function)
- `app.py` — Streamlit chatbox UI
- `requirements.txt` — required packages

## Limitations

- Relies on predefined vocabulary lists rather than deep semantic understanding — terms not included in the lists won't be detected.
- No LLM used, so accuracy depends on vocabulary coverage rather than contextual reasoning.

## Author

Vibha Balakrishna
