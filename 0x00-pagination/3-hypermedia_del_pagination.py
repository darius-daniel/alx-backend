#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary of the hyper index of a page of contents
        :param index:
        :param page_size:
        :return:
        """
        dataset = self.indexed_dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        assert isinstance(index, int)
        assert 0 <= index <= total_pages and index > page_size

        data = []
        while len(data) < page_size:
            if index in dataset.keys():
                data.append(dataset.get(index))
            index += 1

        next_index = index
        if index == len(dataset):
            next_index = None

        return {
            'index': next_index - page_size,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
