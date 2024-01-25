from github import Github


def get_pass_label_count(token, repo_full_name):
    return {
        "tiaz0128": {
            "img": "http",
            "pass": 50,
            "url": "http",
        },
        "admin": {
            "img": "http",
            "pass": 50,
            "url": "http",
        },
    }

    github = Github(token)
    repo = github.get_repo(repo_full_name)

    # PR 목록을 가져옵니다.
    pr_list = repo.get_pulls(state="all")

    pass_label_counts = {}

    for pr in pr_list:
        # PR의 작성자 (auth_id)와 할당된 사용자 (assignee)를 가져옵니다.
        auth_id = pr.user.login
        assignee = pr.assignee.login if pr.assignee else None

        # auth_id와 assignee가 동일하고, PR에 'pass' 라벨이 붙어있는지 확인합니다.
        if auth_id == assignee and any(label.name == "pass" for label in pr.labels):
            # 해당 사용자에 대한 pass 라벨 갯수를 카운트합니다.
            pass_label_counts[auth_id] = pass_label_counts.get(auth_id, 0) + 1

    # 전부 패스인 사람 = 명예전당
    # 풀고 있는 사람 = 라벨 갯수
    # 그 사람이 풀고있는 곳 클릭 할수 있게
    # 이름도 나오긴 해야겠네

    return pass_label_counts
