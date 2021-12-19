import math
from collections import defaultdict
from typing import DefaultDict
import numpy as np
from lib.lib_check import LibCheck
from lib.lib_file import LibFile

input_files_and_results = [
    ("d12/simple_example.txt", 36),
    ("d12/example.txt", 103),
    ("d12/hard_example.txt", 3509),
    ("d12/input.txt", 122880),
]


class Link:
    def __init__(self, begin, end) -> None:
        self.begin = begin
        self.end = end


def get_graph(file_lines: list[str]) -> defaultdict[list]:
    graph = defaultdict(list)
    for file_line in file_lines:
        [begin, end] = file_line.split("-")
        graph[begin].append(end)
        graph[end].append(begin)

    return graph


def dfs(node, graph, seen=None, can_visit=True):
    if seen is None:
        seen = []
    
    if node == "end":
        return 1

    count = 0
    for dest_node in graph[node]:
        if dest_node == "start":
            continue
        if dest_node.isupper():
            count += dfs(dest_node, graph, seen, can_visit)
        elif dest_node not in seen or can_visit:
            seen_copy = seen.copy()
            seen_copy.append(dest_node)
            count += dfs(dest_node, graph, seen_copy, can_visit if dest_node not in seen else False)
    return count 



@LibCheck.check(input_files_and_results=input_files_and_results, input_parse_func=LibFile.read_lines)
def day_12(file_lines: list[str]):
    graph: defaultdict[list] = get_graph(file_lines)
    seen = []
    seen.append("start")
    visited = dfs("start", graph, seen)
    return visited
