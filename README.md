# goit-algo-hw-05

## Task

Comparison of substring search algorithms:
- Boyer-Moore
- Knuth-Morris-Pratt
- Rabin-Karp

The algorithms were tested on two text articles using:
- existing substring
- non-existing substring

Execution time was measured using the timeit module.

---

## Results

Boyer-Moore showed the best performance in most tests because it skips parts of the text efficiently.

Knuth-Morris-Pratt also demonstrated stable performance due to preprocessing of the pattern.

Rabin-Karp worked reasonably well but was generally slower because of hash calculations.

Overall, Boyer-Moore turned out to be the fastest algorithm for both articles.
