from reportlab.platypus import (

    SimpleDocTemplate,
    Paragraph,
    Spacer

)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import letter

from datetime import datetime


def generate_pdf_report(ranked_candidates):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    pdf_file_path = (
        f"reports/shortlist_report_{timestamp}.pdf"
    )


    doc = SimpleDocTemplate(

        pdf_file_path,

        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []



    title = Paragraph(

        "HR AI SHORTLIST REPORT",

        styles['Title']

    )

    elements.append(title)

    elements.append(Spacer(1, 20))



    for index, candidate in enumerate(

        ranked_candidates,

        start=1

    ):

        candidate_title = Paragraph(

            f"<b>{index}. "
            f"{candidate['candidate_name']}</b>",

            styles['Heading2']

        )

        elements.append(candidate_title)

        elements.append(Spacer(1, 10))


        details = f"""

        <b>Final Score:</b>
        {candidate['final_score']}/10
        <br/><br/>

        <b>Recommendation:</b>
        {candidate['recommendation']}
        <br/><br/>

        <b>Skills Match:</b>
        {candidate['skills_score']}/10
        <br/>
        {candidate['skills_justification']}
        <br/><br/>

        <b>Experience Relevance:</b>
        {candidate['experience_score']}/10
        <br/>
        {candidate['experience_justification']}
        <br/><br/>

        <b>Education & Certifications:</b>
        {candidate['education_score']}/10
        <br/>
        {candidate['education_justification']}
        <br/><br/>

        <b>Project / Portfolio:</b>
        {candidate['project_score']}/10
        <br/>
        {candidate['project_justification']}
        <br/><br/>

        <b>Communication Quality:</b>
        {candidate['communication_score']}/10
        <br/>
        {candidate['communication_justification']}
        <br/><br/>

        """

        paragraph = Paragraph(

            details,

            styles['BodyText']

        )

        elements.append(paragraph)

        elements.append(Spacer(1, 25))


    ranking_title = Paragraph(

        "<b>FINAL CANDIDATE RANKING</b>",

        styles['Heading1']

    )

    elements.append(ranking_title)

    elements.append(Spacer(1, 20))


    ranking_text = ""


    for index, candidate in enumerate(

        ranked_candidates,

        start=1

    ):

        ranking_text += (

            f"<b>Rank {index}</b>: "

            f"{candidate['candidate_name']}"

            f" | Score: {candidate['final_score']}"

            f" | Recommendation: "

            f"{candidate['recommendation']}"

            f"<br/><br/>"

        )


    ranking_paragraph = Paragraph(

        ranking_text,

        styles['BodyText']

    )

    elements.append(ranking_paragraph)

    elements.append(Spacer(1, 20))


    doc.build(elements)


    print(
    f"\nPDF report generated successfully!"
    f"\nSaved at: {pdf_file_path}"
    )