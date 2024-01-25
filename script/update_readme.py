from github import Github
import sys
import re

from get_pass_pr import get_pass_label_count


def update_readme(token, repo_full_name):
    github = Github(token)
    repo = github.get_repo(repo_full_name)

    # README.md 파일을 가져옵니다.
    readme_file = repo.get_contents("README.md")
    readme_content = readme_file.decoded_content.decode("utf-8")

    # README.md 파일에서 특정 부분을 찾아내고 수정합니다.
    pattern = r"<!-- PR Status Start -->(.*?)<!-- PR Status End -->"
    match = re.search(pattern, readme_content, re.DOTALL)

    if match:
        # 기존 데이터를 그대로 유지합니다.
        pr_status_section = match.group(0)

        # 결과 출력
        pass_label_counts = get_pass_label_count(token, repo_full_name)

        # 기존 데이터를 삭제하고 새로운 데이터로 채웁니다.
        new_content = "<!-- PR Status Start -->\n"
        for user, count in pass_label_counts.items():
            new_content += f"Pass count (auth_id): {user}\nPass count: {count} / 85\n"

        new_content += "<!-- PR Status End -->\n"

        # README.md 파일을 업데이트합니다.
        repo.update_file(
            path=readme_file.path,
            message="Update README.md",
            content=new_content,
            sha=readme_file.sha,
        )
    else:
        print("Pattern not found in README.md")


if __name__ == "__main__":
    token: str = sys.argv[1]
    repo_full_name = sys.argv[2]

    update_readme(token, repo_full_name)
