def parse_job_description(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        job_description = file.read()

    return job_description