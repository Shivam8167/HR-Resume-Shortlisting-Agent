import os

from parsers.resume_parser import parse_resume

from embeddings.similarity_engine import calculate_similarity

from reports.pdf_report_generator import generate_pdf_report

from utils.override_manager import override_candidate_score

from parsers.jd_parser import parse_job_description

from scoring.rubric_engine import (

    calculate_skills_score,
    calculate_experience_score,
    calculate_education_score,
    calculate_project_score,
    calculate_communication_score,
    calculate_final_score

)

from utils.candidate_ranker import rank_candidates


job_description = parse_job_description(
    "job_descriptions/job_description.txt"
)



resume_folder = "sampleData"



all_candidates = []



for file_name in os.listdir(resume_folder):

    if file_name.endswith(".pdf") or file_name.endswith(".docx"):

        resume_path = os.path.join(
            resume_folder,
            file_name
        )

        print("\n")
        print("=" * 60)
        print(f"PROCESSING CANDIDATE: {file_name}")
        print("=" * 60)


        resume_text = parse_resume(resume_path)


        similarity_score = calculate_similarity(
            job_description,
            resume_text
        )


        skills_score, skills_justification = (
            calculate_skills_score(
                job_description,
                resume_text
            )
        )


        experience_score, experience_justification = (
            calculate_experience_score(
                job_description,
                resume_text
            )
        )


        education_score, education_justification = (
            calculate_education_score(
                job_description,
                resume_text
            )
        )


        project_score, project_justification = (
            calculate_project_score(
                job_description,
                resume_text
            )
        )


        communication_score, communication_justification = (
            calculate_communication_score(
                resume_text
            )
        )


        final_score = calculate_final_score(

            skills_score,
            experience_score,
            education_score,
            project_score,
            communication_score

        )


        if final_score >= 8:

            recommendation = "STRONG SHORTLIST"

        elif final_score >= 6:

            recommendation = "SHORTLIST"

        else:

            recommendation = "NOT RECOMMENDED"



        print(f"\nSemantic Match Score: {similarity_score}%\n")


        print("1. Skills Match")
        print(f"Score: {skills_score}/10")
        print(f"Justification: {skills_justification}\n")


        print("2. Experience Relevance")
        print(f"Score: {experience_score}/10")
        print(f"Justification: {experience_justification}\n")


        print("3. Education & Certifications")
        print(f"Score: {education_score}/10")
        print(f"Justification: {education_justification}\n")


        print("4. Project / Portfolio")
        print(f"Score: {project_score}/10")
        print(f"Justification: {project_justification}\n")


        print("5. Communication Quality")
        print(f"Score: {communication_score}/10")
        print(f"Justification: {communication_justification}\n")


        print("-" * 60)

        print(f"Final Weighted Score: {final_score}/10")

        print(f"Recommendation: {recommendation}")

        print("-" * 60)


        candidate_data = {

            "candidate_name": file_name,

            "semantic_score": similarity_score,

            "skills_score": skills_score,
            "skills_justification": skills_justification,

            "experience_score": experience_score,
            "experience_justification": experience_justification,

            "education_score": education_score,
            "education_justification": education_justification,

            "project_score": project_score,
            "project_justification": project_justification,

            "communication_score": communication_score,
            "communication_justification": communication_justification,

            "final_score": final_score,

            "recommendation": recommendation

        }

        all_candidates.append(candidate_data)


ranked_candidates = rank_candidates(all_candidates)

override_candidate_score(

    ranked_candidates,

    "Aman_Verma",

    7.5,

    "Strong internal referral and excellent interview feedback"
)

generate_pdf_report(ranked_candidates)


print("\n\n")
print("=" * 70)
print("FINAL CANDIDATE RANKING")
print("=" * 70)


print(

    f"{'Rank':<8}"
    f"{'Candidate':<45}"
    f"{'Score':<12}"
    f"{'Recommendation'}"

)


print("-" * 70)


for index, candidate in enumerate(ranked_candidates, start=1):

    print(

        f"{index:<8}"
        f"{candidate['candidate_name']:<45}"
        f"{candidate['final_score']:<12}"
        f"{candidate['recommendation']}"

    )