def get_pass_label_count(repo):
    open_prs = repo.get_pulls(state="all")

    users = {}
    SERVER_URL = "https://github.com"
    REPOSITORY = "tiaz0128/git-actions"

    for pr in open_prs:
        # 1. PR 작성자 == PR assignee (붙어있는 경우만 가져와서)

        if pr.user in pr.assignees:
            cnt = 0
            id = pr.user.login

            if not users.get(id):
                users[id] = {
                    "id": id,
                    "name": pr.user.name,
                    "img": pr.user.avatar_url,
                    "url": f"{SERVER_URL}/{REPOSITORY}/pulls?q=is%3Apr+author%3A{id}+assignee%3A{id}",
                    "cnt": 0,
                }

            if "Pass" in [label.name for label in pr.labels]:
                users[id][cnt] += 1

    return users
