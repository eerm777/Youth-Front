def builder():
    """Reads jobs.txt and converts each line into a job dictionary."""

    # Read and clean file lines
    with open("jobs.txt", "r") as file:
        content = file.readlines()
        clean_content = [line.strip() for line in content]

    # First line contains column titles (not used directly)
    titles = clean_content[0].split(",")

    jobs = []

    # Convert each remaining line into a job dictionary
    for i in range(1, len(clean_content)):
        items = clean_content[i].split(",")

        job = {
            "company": items[0],
            "title": items[1],
            "age_min": int(items[2]),
            "interest": items[3],
            "location": items[4],
            "pay": items[5],
            "contact": items[6]
        }

        jobs.append(job)

    return jobs



