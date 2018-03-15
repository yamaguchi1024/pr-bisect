## git bisect on pull requests
This is a tool for doing git bisect based on pull requests. When your repository is using rebase when merging commits, you may want to bisect on pull requests rather than commits because git bisect doesn't work when some commits in one PR is broken.

## How to use
- apt install python3
- apt install python3-pip
- pip3 install PyGithub    
- git clone https://github.com/yamaguchi1024/pr-bisect
- python3 pr-bisect.py org_name repo_name <your_github_token> <good_PR_id> <bad_PR_id>
- Type "Good" or "Bad"
