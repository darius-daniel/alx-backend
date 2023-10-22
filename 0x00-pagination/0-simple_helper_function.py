#!/usr/bin/env python3
""" 0. Simple Helper Function. """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start: int = (page - 1) * page_size
    end: int = start + page_size

    return start, end
