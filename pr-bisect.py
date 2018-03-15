from github import Github
import os
import sys
import subprocess

args = sys.argv
if len(args) < 6:
  print("python3 pr-bisect.py org_name repo_name <good_PR_id> <bad_PR_id> test_script.sh")
  print("If script.sh returns 0, the pr is good and if script.sh returns non-zero, pr is bad")
  sys.exit()

org_name = args[1]
repo_name = args[2]
good = int(args[3])
bad = int(args[4])
script = args[5]

# git's message is annoying
FNULL = open(os.devnull, 'w')

git = Github()
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

  res = subprocess.call(script)
  if res == 0:
  # it means this pr is good
    good = mid
  else:
    bad = mid
