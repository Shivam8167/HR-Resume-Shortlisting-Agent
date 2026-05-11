import fitz


def parse_job_description(file_path):


    if file_path.endswith(".txt"):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            job_description = file.read()

        return job_description


    elif file_path.endswith(".pdf"):

        text = ""

        pdf_document = fitz.open(file_path)

        for page in pdf_document:

            text += page.get_text()

        return text



    else:

        raise ValueError(
            "Unsupported JD file format."
        )