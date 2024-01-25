from github import Github
import sys


def get_comment(token, repo_owner, repo_name):
    github = Github(token)
    repo = github.get_repo(f"{repo_owner}/{repo_name}")
    open_prs = repo.get_pulls(state="open")

    for pr in open_prs:
        print(f"PR #{pr.number} - {pr.title}")
        comments = pr.get_issue_comments()

        for comment in comments:
            reactions = comment.get_reactions()

            for reaction in reactions:
                print(f"  - {reaction.content} by {reaction.user.login}")

                if pr.user == reaction.user and reaction.content == "-1":
                    comment.delete()


if __name__ == "__main__":
    token: str = sys.argv[1]
    repo_owner: str = sys.argv[2]
    repo_name: str = sys.argv[3]

    get_comment(token, repo_owner, repo_name)
