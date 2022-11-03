from dataclasses import dataclass
from dataclasses import asdict


@dataclass
class DataToPharse(object):

    data: str


@dataclass
class OutputData:

    my_list = list[DataToPharse]
