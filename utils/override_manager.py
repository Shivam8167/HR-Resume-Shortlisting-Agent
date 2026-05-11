def override_candidate_score(

    candidates,
    candidate_name,
    new_score,
    reason

):

    for candidate in candidates:

        if candidate_name.lower() in candidate[
            "candidate_name"
        ].lower():

            old_score = candidate[
                "final_score"
            ]

            candidate[
                "final_score"
            ] = new_score


            candidate[
                "override_reason"
            ] = reason


            if new_score >= 8:

                candidate[
                    "recommendation"
                ] = "STRONG SHORTLIST"

            elif new_score >= 6:

                candidate[
                    "recommendation"
                ] = "SHORTLIST"

            else:

                candidate[
                    "recommendation"
                ] = "NOT RECOMMENDED"


            print("\nHR OVERRIDE APPLIED")

            print(
                f"Candidate: {candidate['candidate_name']}"
            )

            print(
                f"Old Score: {old_score}"
            )

            print(
                f"New Score: {new_score}"
            )

            print(
                f"Reason: {reason}"
            )

            return


    print("Candidate not found.")