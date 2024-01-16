import pytest
import os
import re
from dotenv import load_dotenv


def get_test_file_path(file_path, user_id):
    script_path = os.path.abspath(file_path)

    # 부모 폴더 이름
    parent_path = os.path.dirname(script_path)
    parent_directory = os.path.split(parent_path)[-1]

    # 파일명에서 숫자 추출
    file_name = os.path.basename(file_path)
    numbers = re.findall(r"\d+", file_name)[-1]

    return f"src.{user_id}.{parent_directory}.solution_{numbers}"


def pytest_addoption(parser):
    # .env 파일을 현재 작업 디렉토리에서 읽어옴
    load_dotenv()

    # 환경 변수 읽기
    USER_ID = os.getenv("USER_ID")

    parser.addoption(
        "--id",
        action="store",
        default=USER_ID,
        help="여기를 수정하지 마세요!!! .tests/.env 파일에 테스트하고 싶은 아이디를 넣어주세요!!",
    )


@pytest.fixture(name="user_id")
def setup(request):
    user_id = request.config.getoption("--id")

    return user_id


@pytest.fixture(name="func")
def setup_lib():
    return get_test_file_path
