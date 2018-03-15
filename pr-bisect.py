from github import Github
import os
import sys
import subprocess

# python3 pr-bisect.py org_name repo_name <your_token> <good_PR_id> <bad_PR_id>

args = sys.argv
if len(args) < 6:
  print("python pr-bisect.py org_name repo_name <your_github_token> <good_PR_id> <bad_PR_id>")
  sys.exit()

org_name = args[1]
repo_name = args[2]
token = args[3]
good = int(args[4])
bad = int(args[5])

# git's message is annoying
FNULL = open(os.devnull, 'w')

git = Github(token)
repo = git.get_organization(org_name).get_repo(repo_name)

while True:
  mid = int((good + bad)/2)
  if good == bad:
    print("Bad pull request is " + mid)
    break
  pull = repo.get_pull(mid)
  while pull.merged == False:
    mid = mid + 1
    pull = repo.get_pull(mid)

  merge_sha = pull.merge_commit_sha
  e = "git checkout " + merge_sha
  subprocess.Popen(e, shell=True, stdout = FNULL, stderr = subprocess.STDOUT)

  res = input("Type \"Good\" or \"Bad\": ")
  if res == "Good":
    good = mid
  elif res == "Bad":
    bad = mid
  else:
    print("Type Good or Bad")
