#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
and returns a tuple of size two containing a start index and an end index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function should return a tuple of size two containing
    a start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
