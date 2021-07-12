# -*- coding:utf-8 -*-
from typing import *

import os


def make_directory(dir_path: str):
    """
    해당 위치에 디렉토리가 없다면 디렉토리를 생성해주는 함수
    :param dir_path: 디렉토리 위치 | str
    :return: None
    """
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)


def get_file_name_list(file_path: str) -> List[str]:
    """
    해당 위치에 존재하는 모든 파일의 이름의 목록을 반환하는 함수
    :param file_path: 확인할 위치 | str
    :return: 파일 목록 | List[str]
    """
    file_list: Set = set()
    for name in os.listdir(file_path):
        file_list.add(os.path.splitext(name)[0])
    return list(file_list)


def get_root_path() -> str:
    """
    패키지의 Root Path를 반환하는 함수 (util/directory.py의 위치가 고정되어있다는 전재)
    :return: Root Path | str
    """
    # print("abs", os.path.dirname(os.path.abspath(__file__)))
    # print(os.getcwd())
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))