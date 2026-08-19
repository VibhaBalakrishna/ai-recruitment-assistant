import spacy
from spacy.matcher import PhraseMatcher

# ---------- DATA ----------
SKILLS = [
    "machine learning", "deep learning", "nlp", "natural language processing",
    "ai/ml", "ai", "ml", "data analysis", "data science", "computer vision",
    "artificial intelligence", "neural networks", "backend development",
    "frontend development", "web development", "cloud computing",
    "devops", "database management", "api development", "testing",
    "project management", "problem solving", "communication","robotics", 
    "data visualization", "big data", "data mining", "reinforcement learning","iot", "edge computing",
    "cybersecurity", "blockchain", "quantum computing","engineering", 
    "software engineering", "mobile development", "game development","leadership", "teamwork",
    "critical thinking", "adaptability", "time management","automation", "data engineering",
    "data warehousing", "etl", "data modeling","algorithms", "data structures",
    "object-oriented programming", "functional programming","api design", "microservices",
    "containerization", "orchestration","cloud architecture", "cloud security","networking", 
    "virtualization", "serverless computing","agile methodologies", "scrum", "kanban","ui/ux design",
    "user experience", "user interface design","version control", "git", "github",
    "continuous integration", "continuous deployment","testing frameworks", "unit testing", 
    "integration testing","performance optimization", "scalability"
]

TECHNOLOGIES = [
    "python", "cnn", "rnn", "lstm", "tensorflow", "pytorch", "keras",
    "scikit-learn", "opencv", "react", "node.js", "django", "flask",
    "docker", "kubernetes", "aws", "azure", "gcp", "git", "mysql",
    "postgresql", "mongodb", "spacy", "pandas", "numpy", "html", "css",
    "rest api", "graphql", "linux","pytorch lightning", "fastapi", "streamlit",
    "flask-restful", "celery","google cloud", "amazon web services", "microsoft azure",
    "heroku", "digital ocean","firebase", "oracle cloud", "ibm cloud", "cloudflare",
    "vercel", "netlify","apache spark", "hadoop", "kafka", "airflow", "jenkins", "ansible"
]

LANGUAGES = [
    "python", "java", "c++", "c", "javascript", "typescript", "sql",
    "r", "go", "rust", "swift", "kotlin", "php", "ruby", "c#","matlab", "scala", "perl",
    "haskell", "lua", "dart", "elixir", "clojure","shell scripting", "bash", "powershell",
    "assembly", "fortran", "cobol","html", "css", "xml","html", "css3", "json", "yaml","markdown",
    "latex", "graphql","vhdl", "verilog", "f#","objective-c", "racket", "smalltalk","prolog",
    "lisp", "scheme","ada", "pascal", "delphi","julia", "nim", "crystal","groovy", "apex",
    "abap","sas", "stata", "spss","scratch", "logo", "basic"
]

# ---------- EXTRACTOR ----------
nlp = spacy.load("en_core_web_sm")

def make_matcher(terms):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(t) for t in terms]
    matcher.add("TERMS", patterns)
    return matcher

skill_matcher = make_matcher(SKILLS)
tech_matcher = make_matcher(TECHNOLOGIES)
lang_matcher = make_matcher(LANGUAGES)

def get_matches(doc, matcher):
    spans = [doc[start:end].text for _, start, end in matcher(doc)]
    return sorted(set(s.lower() for s in spans))

def extract(text):
    doc = nlp(text)
    return {
        "skill": get_matches(doc, skill_matcher),
        "technology": get_matches(doc, tech_matcher),
        "language": get_matches(doc, lang_matcher)
    }

# ---------- TEST ----------
if __name__ == "__main__":
    test = input("Enter your experience/skills: ")
    print(extract(test))