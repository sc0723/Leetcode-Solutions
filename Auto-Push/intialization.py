import getpass
from github import Github
from github import Repo
import json
import os.path

username = input('Enter your GitHub username: ')
session_id = getpass.getpass('Enter your leetcode session ID: ')
repo_exists = input('Do you already have an existing repo for leetcode solutions (y/n): ')
if repo_exists.lower() == 'n':
    print("Disclaimer, creating a new PAT solely for the use of this script is highly recommended")
    git_pat = getpass.getpass("Enter your GitHub Personal Access Token (PAT): ")
    repo_name = input("Enter the name you would like for the repository: ")
    repo_description = input("Enter the description you would like to give for the repository (type None if you do not want one): ")
    privacy_status = input("Would you like the repo to be private? (y/n): ")
    if privacy_status.lower() == y:
        privacy_status = True
    else:
        privacy_status = False

    if repo_description.lower() == "none":
        repo_description = ""

    try:
        g = Github(git_pat)
        user = g.get_user()

        repo = user.create_repo(
            name=repo_name,
            description=repo_description,
            private=privacy_status,
            auto_init=True
        )

        print(f"Repository '{repo.full_name}' created")
        print(f"Repository URL: {repo.html_url}")

        path = input("Enter the path for where you would like to clone the repo: ")

        if not os.path.exists(path):
             os.makedirs(path, exist_ok=True)
             print(f"Created local directory: {path}")
        authenticated_clone_url = f"https://{git_pat}@github.com/{user.login}/{github_repo_name}.git
        try:
            Repo.clone_from(repo.clone_url, path)
        except Exception as error:
            print(f"An error occured cloning: {error}")


    except Exception as e:
        print(f"An error occured: {e}")
    


# else:
#     repo_url = input("Enter the path to the repo: ")


user_info = {
    "username": username,
    "session_id": session_id
}

with open("user_info.json", "w") as f:
    json.dump(user_info, f, indent=2)

print('User info is saved to user_info.json')


