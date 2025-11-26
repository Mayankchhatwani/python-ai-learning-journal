def generate_report(*scores, **options):
    """
    Generate a simple score report.

    *scores: variable number of numeric scores
    **options:
        include_average: bool (default False)
        rounding: bool (default False)
    """
    print(f"Scores: {scores}")

    # Check if we should include average
    if options.get("include_average", False):
        if len(scores) == 0:
            print("No scores available to compute average.")
            return

        avg = sum(scores) / len(scores)

        # Apply rounding if requested
        if options.get("rounding", False):
            avg = round(avg)

        print(f"Average: {avg}")


if __name__ == "__main__":
    # some manual tests
    generate_report(90, 85, 78, 92, include_average=True, rounding=True)
    generate_report(60, 70, 80, include_average=True, rounding=False)
