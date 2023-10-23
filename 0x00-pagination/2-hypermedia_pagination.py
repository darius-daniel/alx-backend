#!/usr/bin/env python3
""" 1. Simple Pagination. """
import csv
import math
from typing import Tuple, List, Union, Dict


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
        """
        Initialize a new instance of the class
        """
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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        return [
            row for idx, row in enumerate(self.dataset())
            if start <= idx <= end
        ]

    def get_hyper(
            self,
            page: int = 1,
            page_size: int = 10
    ) -> Dict[str, Union[int, None, List[List]]]:
        """
        Doing whatever I want to do
        :param page:
        :param page_size:
        :return:
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)

        next_page = page + 1
        if page >= total_pages:
            next_page = None

        prev_page = page - 1
        if page <= 1:
            prev_page = None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
