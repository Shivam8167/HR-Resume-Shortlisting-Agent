SKILLS_DB = [

    # Programming Languages
    "python",
    "java",
    "c++",
    "javascript",
    "typescript",

    # Frontend
    "react",
    "next.js",
    "html",
    "css",
    "tailwind",

    # Backend
    "node.js",
    "express",
    "fastapi",
    "flask",
    "django",

    # Databases
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "redis",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "computer vision",

    # AI Frameworks
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "langchain",
    "llamaindex",
    "crewai",

    # Data Science
    "pandas",
    "numpy",
    "matplotlib",

    # Dev Tools
    "git",
    "github",
    "docker",

    # CS Fundamentals
    "data structures",
    "algorithms",

    # Cloud
    "aws",
    "azure",
    "gcp"
]



def extract_skills(text):

    text = text.lower()

    extracted_skills = set()


    for skill in SKILLS_DB:

        if skill.lower() in text:

            extracted_skills.add(skill)


    return sorted(list(extracted_skills))