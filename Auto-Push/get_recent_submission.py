import json
import os.path
import query
import requests as req
import schedule
import subprocess
import time

with open("user_info.json", "r") as f:
    user_info = json.load(f)

request_url = "https://leetcode.com/graphql"

def get_recent_submission(user):
    id_query = query.recent_submission_id

    user_data = {
        "query": id_query,
        "variables": {"username": user}
    }

    res = req.post(request_url, json=user_data).json()

    return res["data"]["recentAcSubmissionList"][0]



def get_recent_submission_code(submission_id):
    code_query = query.recent_submission_code

    submission_data = {
        "query": code_query,
        "variables" = {"submissionId" : submission_id}
    }

    cookies = {
        "LEETCODE_SESSION": user_info["session_id"]
    }

    res = req.post(url, json=submission_data).json()

    return res["data"]["submissionDetails"]["code"]

def write_code_to_file(title, id):
    code = get_recent_submission_code(id)

    with open(f"{title}.py", "w") as f:
        f.write(code)

def update():
    recent_submission = get_recent_submission(user_info["username"])
    sub_id = recent_submission["id"]
    title = recent_submission["title"]

    recent_code = get_recent_submission_code(sub_id)
    
    if not os.path.isfile("prev_submission_id.txt"):
        with open("prev_submission_id.txt", "w") as f:
            f.write(sub_id)
        
        write_code_to_file(title, sub_id)

        subprocess.run(["git", "add", "."], cwd="..")
        subprocess.run(["git", "commit", "-m", title], cwd="..")
        subprocess.run(["git", "push"])

schedule.every(30).seconds.do(update)

while True:
    schedule.run_pending()
    time.sleep(1)