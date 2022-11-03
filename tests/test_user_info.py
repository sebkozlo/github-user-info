from github_user.user_info import DataToPharse
from dataclasses import asdict


class TestDataToPharse:
    def test_empty_list(self):
        data = DataToPharse([])
        assert data.data == []

    def test_str_object(self):
        data = DataToPharse("test str")
        assert data.data == "test str"

    def test_one_item_in_list(self):
        data = DataToPharse([1])
        assert data.data == [1]

    def test_five_mix_different_in_list(self):
        data = DataToPharse(["one", 2, [3, 3], {5: 1}, (0, 0)])
        assert data.data == ["one", 2, [3, 3], {5: 1}, (0, 0)]

    def test_astict_dict(self):
        sample_dict = DataToPharse("example_key")
        assert asdict(sample_dict) == {"data": "example_key"}
