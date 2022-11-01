import pytest
from github_user.user_info import some_func


def test_some_func():
    assert some_func() == "test-str"
