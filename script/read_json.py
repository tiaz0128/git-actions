import json
import sys


if __name__ == "__main__":
    file_name = sys.argv[1]
    key = sys.argv[2]

    with open(f".\\json\\{file_name}", encoding="utf-8") as fp:
        solutions = json.load(
            fp,
        )
        result = solutions.get(key)

    print(result)
