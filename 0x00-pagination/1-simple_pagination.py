#!/usr/bin/env python3
""" 0. Simple Helper Function. """
import math
import csv
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start index and an end index
    :param page:
    :param page_size: number of items on the page
    :return: a tuple
    """
    start = (page - 1) * page_size

    return start, start + page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a list of items from a paginated csv file
        :param page:
        :param page_size:
        :return:
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0

        start, end = index_range(page, page_size)

        with open('Popular_Baby_Names.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)

            output = [
                row for idx, row in enumerate(reader) if start <= idx <= end
            ]

        return output
