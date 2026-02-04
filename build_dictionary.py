def builder():
    with open("jobs.txt", "r") as file:
        content = file.readlines()
        clean_content = []
        for line in content:
                clean_content.append(line.strip())
    titles = clean_content[0].split(",")

    jobs = []

    for i in range(1, len(clean_content)):
        items = clean_content[i].split(",")
        job = {}
        job["company"] = items[0]
        job["title"] = items[1]
        job["age_min"] = items[2]
        job["interest"] = items[3]
        job["location"] = items[4]
        job["pay"] = items[5]
        job["contact"] = items[6]

        jobs.append(job)
    return jobs
   
    


