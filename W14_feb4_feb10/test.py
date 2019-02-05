#!/usr/bin/env python3

import os
import re
import time

from prim import prim
from kruskal import kruskal

TESTS_PATH = "tests"


def get_test_files():
    test_files = []
    for subdirpath, dirnames, filenames in os.walk(TESTS_PATH):
        for filename in filenames:
            if re.match(r"in\d\d.txt", filename):
                    test_files.append(os.path.join(subdirpath, filename))
    return test_files


def main():
    for filename in get_test_files():
        print("%s:" % filename, end=" ")
        with open(filename, "r") as fhandler:
            lines = fhandler.readlines()
        nb_edges = int(lines[0])
        edges = [(lambda s: (int(s[0]), int(s[1]), int(s[2])))
                 (lines[i + 1].strip().split()) for i in range(nb_edges)]
        try:
            t1 = time.perf_counter()
            _, prim_c = prim(edges)
            t2 = time.perf_counter()
            _, kruskal_c = kruskal(edges)
            t3 = time.perf_counter()
        except Exception:
            print("runtime error")
        else:
            if prim_c != kruskal_c:
                print("KO (Prim: %d, Kruskal: %d)" % (prim_c, kruskal_c))
            else:
                print("OK (both %d)\t- %d edges\t"
                      "- Prim: %.3f ms, \tKruskal: %.3f ms"
                      % (prim_c, nb_edges, 1000 * (t2 - t1), 1000 * (t3 - t2)))


if __name__ == "__main__":
    main()
