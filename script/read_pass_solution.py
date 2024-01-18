import sys


if __name__ == "__main__":
    path = sys.argv[1]

    with open(f"..{path}", encoding="utf-8") as fp:
        content = fp.read()
        print(content, end="")
