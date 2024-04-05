#!/usr/bin/env python3
'''
function named index_range with two integer arguments page and page_size
'''
def index_range(page, page_size):
    '''
    function that takes two integer arguments page and page_size
    '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)