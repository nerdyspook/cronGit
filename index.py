from git import Repo

working_tree_dir = '/Projects/autoGitActivity'
file = "autoGitActivity/activityTracker.txt"
repo = Repo(working_tree_dir)

def alter_file(file):
    with open(file, "a") as f:
        f.write("new line/n")

def git_activities(repo):
    if len(repo.untracked_files):
        repo.git.add(A=True)
        repo.git.commit('-m', 'initial commit')
        repo.git.push('origin', 'HEAD:refs/for/master')

alter_file(file)
git_activities(repo)
