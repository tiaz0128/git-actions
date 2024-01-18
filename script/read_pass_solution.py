import sys


if __name__ == "__main__":
    path = sys.argv[1]

    # ..\\src\\tiaz0128\\ch_05\\solution_001.py
    with open(f"..\\{path}", encoding="utf-8") as fp:
        print(fp.readline())
