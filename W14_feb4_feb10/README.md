Problem of the week
===

Implement the Kruskal algorithm to find the minimum spanning tree in a graph.

You can fill the template `template.py`, and check your results against my implementation of Prim's algorithm by modifying `test.py` to import your version of the `kruskal` function.

You can either use my implementation of the Union-Find data stucture provided in `unionfind.py` or create your own one. I have also provided my implementation of the Kruskal algorithm, but I advise you not to open it until you have tried something (and asked for my help if you are physically present during the course).

---

Here is an example of execution of the `test.py` script with the provided test cases:

```
tests/in00.txt: OK (both 53)    - 16 edges      - Prim: 0.042 ms,       Kruskal: 0.049 ms
tests/in01.txt: OK (both 121)   - 20 edges      - Prim: 0.042 ms,       Kruskal: 0.055 ms
tests/in02.txt: OK (both 226)   - 50 edges      - Prim: 0.093 ms,       Kruskal: 0.124 ms
tests/in03.txt: OK (both 311)   - 100 edges     - Prim: 0.202 ms,       Kruskal: 0.338 ms
tests/in04.txt: OK (both 371)   - 200 edges     - Prim: 0.332 ms,       Kruskal: 0.446 ms
tests/in05.txt: OK (both 393)   - 500 edges     - Prim: 0.820 ms,       Kruskal: 1.120 ms
tests/in06.txt: OK (both 422)   - 1000 edges    - Prim: 1.747 ms,       Kruskal: 2.183 ms
tests/in07.txt: OK (both 448)   - 2000 edges    - Prim: 3.654 ms,       Kruskal: 4.370 ms
tests/in08.txt: OK (both 519)   - 5000 edges    - Prim: 8.964 ms,       Kruskal: 13.224 ms
tests/in09.txt: OK (both 608)   - 10000 edges   - Prim: 14.946 ms,      Kruskal: 25.905 ms
tests/in10.txt: OK (both 770)   - 20000 edges   - Prim: 29.152 ms,      Kruskal: 52.115 ms
tests/in11.txt: OK (both 1133)  - 50000 edges   - Prim: 74.568 ms,      Kruskal: 142.274 ms
tests/in12.txt: OK (both 1583)  - 100000 edges  - Prim: 156.290 ms,     Kruskal: 323.461 ms
tests/in13.txt: OK (both 2237)  - 200000 edges  - Prim: 323.391 ms,     Kruskal: 681.365 ms
tests/in14.txt: OK (both 3535)  - 500000 edges  - Prim: 837.310 ms,     Kruskal: 1855.102 ms
tests/in15.txt: OK (both 4999)  - 1000000 edges - Prim: 1897.291 ms,    Kruskal: 3992.873 ms
```

These values show that the complexity seems to be O(|E| log |E|) as expected, and the implementation of Prim's algorithm is more efficient than the implementation of Kruskal's on our test set.

*Note: you can tweak the generator of test cases, which is also provided, to run your custom tests.* 
