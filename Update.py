import git
import os
import sys

repo_dir = 'path\to\your\gitclone\of\Lolipop'  # put the path to your Lolipop gitclone here

def update_repo():
    try:
        if not os.path.isdir(repo_dir):
            print("Repository directory doesn't exist. Please clone the repository.")
            return

        repo = git.Repo(repo_dir)
        origin = repo.remotes.origin
        origin.fetch()

        branch = repo.head.ref
        repo.git.merge('origin/' + branch)

        print("Repository has been successfully updated!")

    except git.exc.GitCommandError as e:
        print(f"Git error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    update_repo()
