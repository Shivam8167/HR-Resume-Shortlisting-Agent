from utils.skill_extractor import extract_skills
import re


def calculate_skills_score(job_description, resume_text):

    jd_skills = extract_skills(job_description)

    resume_skills = extract_skills(resume_text)

    matched_skills = list(
        set(jd_skills).intersection(set(resume_skills))
    )

    match_percentage = (
        len(matched_skills)
        / max(len(jd_skills), 1)
    ) * 100

    if match_percentage >= 85:

        score = 10

        justification = (
            f"Excellent skills alignment. "
            f"Matched skills: {', '.join(matched_skills)}"
        )

    elif match_percentage >= 50:

        score = 7

        justification = (
            f"Good skills alignment. "
            f"Matched skills: {', '.join(matched_skills)}"
        )

    else:

        score = 4

        justification = (
            f"Limited skills match. "
            f"Matched skills: {', '.join(matched_skills)}"
        )

    return score, justification



def calculate_experience_score(job_description, resume_text):

    jd_skills = extract_skills(job_description)

    resume_text_lower = resume_text.lower()

    matched_domains = []

    for skill in jd_skills:

        if skill.lower() in resume_text_lower:
            matched_domains.append(skill)

    years_pattern = r'(\d+)\+?\s*(year|years)'
    months_pattern = r'(\d+)\+?\s*(month|months)'

    years_found = re.findall(years_pattern, resume_text_lower)

    months_found = re.findall(months_pattern, resume_text_lower)

    experience_bonus = 0

    if years_found:
        experience_bonus += 3

    if months_found:
        experience_bonus += 1

    total_score = len(matched_domains) + experience_bonus

    if total_score >= 8:

        score = 10

        justification = (
            f"Excellent domain-relevant experience. "
            f"Relevant exposure in: {', '.join(matched_domains)}"
        )

    elif total_score >= 5:

        score = 7

        justification = (
            f"Moderately relevant technical experience. "
            f"Relevant exposure in: {', '.join(matched_domains)}"
        )

    else:

        score = 4

        justification = (
            "Limited domain-relevant experience detected."
        )

    return score, justification



def calculate_education_score(job_description, resume_text):

    jd_text = job_description.lower()

    resume_text_lower = resume_text.lower()



    jd_education_keywords = []

    possible_education_keywords = [

        "bachelor",
        "master",
        "b.tech",
        "computer science",
        "information technology",
        "certification",
        "machine learning",
        "artificial intelligence",
        "data science"
    ]


    for keyword in possible_education_keywords:

        if keyword in jd_text:
            jd_education_keywords.append(keyword)


    matched_education = []

    for keyword in jd_education_keywords:

        if keyword in resume_text_lower:
            matched_education.append(keyword)


    match_percentage = (

        len(matched_education)
        / max(len(jd_education_keywords), 1)

    ) * 100



    if match_percentage >= 85:

        score = 10

        justification = (
            f"Excellent educational alignment. "
            f"Matched: {', '.join(matched_education)}"
        )


    elif match_percentage >= 50:

        score = 7

        justification = (
            f"Good educational alignment. "
            f"Matched: {', '.join(matched_education)}"
        )


    else:

        score = 4

        justification = (
            "Limited educational alignment with job requirements."
        )


    return score, justification



def calculate_project_score(job_description, resume_text):

    jd_skills = extract_skills(job_description)

    resume_text_lower = resume_text.lower()

    matched_project_domains = []

    for skill in jd_skills:

        if skill.lower() in resume_text_lower:
            matched_project_domains.append(skill)

    project_keywords = [
        "project",
        "developed",
        "built",
        "application",
        "system"
    ]

    project_count = 0

    for keyword in project_keywords:

        if keyword in resume_text_lower:
            project_count += 1

    total_score = len(matched_project_domains) + project_count

    if total_score >= 8:

        score = 10

        justification = (
            f"Strong relevant project portfolio. "
            f"Relevant domains: {', '.join(matched_project_domains)}"
        )

    elif total_score >= 5:

        score = 7

        justification = (
            f"Moderately relevant project portfolio. "
            f"Relevant domains: {', '.join(matched_project_domains)}"
        )

    else:

        score = 4

        justification = (
            "Limited relevant project evidence."
        )

    return score, justification



def calculate_communication_score(resume_text):

    word_count = len(resume_text.split())

    if word_count > 300:

        score = 8

        justification = (
            "Resume is detailed, structured, and professionally written."
        )

    elif word_count > 150:

        score = 6

        justification = (
            "Resume communication is reasonably clear."
        )

    else:

        score = 4

        justification = (
            "Resume lacks strong communication clarity."
        )

    return score, justification



def calculate_final_score(

    skills,
    experience,
    education,
    projects,
    communication

):

    final_score = (

        (skills * 0.30) +
        (experience * 0.25) +
        (education * 0.15) +
        (projects * 0.20) +
        (communication * 0.10)

    )

    return round(final_score, 2)