#!/usr/bin/env python3
""" 0. Simple Helper Function. """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start index and an end index
    :param page:
    :param page_size: number of items on the page
    :return: a tuple
    """
    start = (page - 1) * page_size

    return start, start + page_size
