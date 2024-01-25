from github import Github
import sys


def get_comment(token, repo_full_name):
    github = Github(token)
    repo = github.get_repo(repo_full_name)
    open_prs = repo.get_pulls(state="open")

    for pr in open_prs:
        print(f"PR #{pr.number} - {pr.title}")
        comments = pr.get_issue_comments()

        for comment in comments:
            reactions = comment.get_reactions()

            for reaction in reactions:
                print(f"  - {reaction.content} by {reaction.user.login}")

                if pr.user == reaction.user and reaction.content == "confused":
                    comment.delete()


if __name__ == "__main__":
    token: str = sys.argv[1]
    repo_full_name = sys.argv[2]

    get_comment(token, repo_full_name)
