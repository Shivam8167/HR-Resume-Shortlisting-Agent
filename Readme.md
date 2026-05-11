# HR Resume Shortlisting Agent

An AI-powered HR screening and candidate shortlisting system that automatically evaluates resumes against a Job Description (JD), generates explainable rubric-based scores, ranks candidates, and produces professional PDF shortlist reports.


# Project Overview

HR teams often spend significant time manually screening resumes for job openings. This project automates the candidate evaluation pipeline using AI-powered semantic matching and rubric-based scoring.

The system:

- Parses resumes (PDF/DOCX)
- Reads dynamic job descriptions
- Extracts technical skills
- Performs semantic similarity matching
- Evaluates candidates across multiple dimensions
- Generates explainable scores and justifications
- Ranks candidates automatically
- Produces professional PDF shortlist reports
- Supports human override functionality


# Features

## Resume Parsing
- Supports PDF and DOCX resumes
- Extracts raw text for AI evaluation

## Dynamic Job Description Parsing
- Reads JD from external text file
- No hardcoded job role dependency

## Semantic Similarity Matching
- Uses Sentence Transformers embeddings
- Performs intelligent JD ↔ Resume comparison

## Skill Extraction Engine
- Detects technical skills from resumes and JDs
- Supports AI, ML, Web Development, Databases, Cloud, etc.

## Rubric-Based Evaluation
Candidates are evaluated across:

| Dimension | Weight |
|---|---|
| Skills Match | 30% |
| Experience Relevance | 25% |
| Education & Certifications | 15% |
| Project / Portfolio | 20% |
| Communication Quality | 10% |


## Explainable AI Justifications
Each score includes a one-line explanation for transparency and interpretability.


## Multi-Resume Ranking System
- Processes multiple resumes in batch
- Automatically ranks candidates by final score


## Human Override System
Supports human-in-the-loop decision making where HR can manually override candidate scores and recommendations.


## PDF Report Generation
Generates timestamped PDF shortlist reports containing:
- Candidate-wise evaluation
- Rubric scores
- Justifications
- Final ranking table


# Tech Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| NLP / AI | Sentence Transformers |
| Similarity Scoring | Scikit-learn |
| PDF Parsing | PyMuPDF |
| DOCX Parsing | python-docx |
| PDF Report Generation | ReportLab |
| Architecture | Modular Python System |


# Project Architecture

```text
Job Description File
        ↓
JD Parser
        ↓
Resume Parser
        ↓
Skill Extraction Engine
        ↓
Semantic Matching Engine
        ↓
Rubric-Based Scoring
        ↓
Candidate Ranking
        ↓
Human Override
        ↓
PDF Shortlist Report
```


# Folder Structure

```text
HRShortlistingAgent/
│
├── embeddings/
│   └── similarity_engine.py
│
├── job_descriptions/
│   └── job_description.txt
│
├── parsers/
│   ├── jd_parser.py
│   └── resume_parser.py
│
├── reports/
│   ├── pdf_report_generator.py
│   └── shortlist_report_*.pdf
│
├── sample_data/
│   └── resumes...
│
├── scoring/
│   └── rubric_engine.py
│
├── utils/
│   ├── candidate_ranker.py
│   ├── override_manager.py
│   └── skill_extractor.py
│
├── main.py
├── requirements.txt
└── README.md
```


# Installation

## Clone Repository

```bash
git clone <your-github-repo-link>
cd HRShortlistingAgent
```


## Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows
```bash
venv\\Scripts\\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```


## Install Dependencies

```bash
pip install -r requirements.txt
```


# Running the Project

Place resumes inside:

```text
sample_data/
```

Add Job Description inside:

```text
job_descriptions/job_description.txt
```

Run:

```bash
python main.py
```

# Output

The system generates:

## Terminal Output
- Detailed candidate evaluation
- Rubric scores
- Recommendations
- Final ranking table

## PDF Report
Generated inside:

```text
reports/
```

Example:

```text
shortlist_report_2026-05-11_01-42-30.pdf
```

# Sample Candidate Ranking

| Rank | Candidate | Score | Recommendation |
|---|---|---|---|
| 1 | Sneha Kapoor | 8.95 | STRONG SHORTLIST |
| 2 | Rahul Sharma | 8.65 | STRONG SHORTLIST |
| 3 | Shivam Paul | 7.20 | SHORTLIST |


# Human Override Example

```python
override_candidate_score(

    ranked_candidates,

    "Aman_Verma",

    7.5,

    "Strong internal referral and excellent interview feedback"

)
```

# Future Enhancements

- LinkedIn Profile Parsing
- Streamlit Dashboard
- FastAPI Backend
- Vector Database Integration
- LLM-Based Resume Understanding
- Cloud Deployment
- Interview Question Generation


# Author

Shibam Kumar Paul

# License

This project is developed for educational and internship assignment purposes.

