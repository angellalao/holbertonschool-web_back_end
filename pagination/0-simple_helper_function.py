#!/usr/bin/env python3
""" a python function called 'index_range' that takes 2 int arguments """


def index_range(page, page_size):
    """returns a tuple containing the start and end index of a page """
    start_index = int(page_size * (page - 1))
    end_index = int(page * page_size)
    return (start_index, end_index)
