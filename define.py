import timeit


# =========================
# Boyer-Moore
# =========================

def build_shift_table(pattern):
    table = {}

    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)

    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)

    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


# =========================
# Knuth-Morris-Pratt
# =========================

def compute_lps(pattern):
    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < len(text):

        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return i - j

        elif i < len(text) and pattern[j] != text[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


# =========================
# Rabin-Karp
# =========================

def rabin_karp_search(text, pattern):
    d = 256
    q = 101

    m = len(pattern)
    n = len(text)

    p = 0
    t = 0
    h = 1

    for _ in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):

        if p == t:

            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            t = (
                d * (t - ord(text[i]) * h)
                + ord(text[i + m])
            ) % q

            if t < 0:
                t += q

    return -1


# =========================
# Reading files
# =========================

with open("article1.txt", "r", encoding="utf-8") as file:
    text1 = file.read()

with open("article2.txt", "r", encoding="utf-8") as file:
    text2 = file.read()


# Existing substring
existing_pattern = "алгоритм"

# Fake substring
fake_pattern = "супермегагіперрядок"


# =========================
# Time measurements
# =========================

def test_algorithm(name, func, text, pattern):
    time = timeit.timeit(
        lambda: func(text, pattern),
        number=10
    )

    print(f"{name}: {time:.6f} seconds")


print("\n========== ARTICLE 1 ==========\n")

print("Existing substring:\n")

test_algorithm(
    "Boyer-Moore",
    boyer_moore_search,
    text1,
    existing_pattern
)

test_algorithm(
    "KMP",
    kmp_search,
    text1,
    existing_pattern
)

test_algorithm(
    "Rabin-Karp",
    rabin_karp_search,
    text1,
    existing_pattern
)

print("\nFake substring:\n")

test_algorithm(
    "Boyer-Moore",
    boyer_moore_search,
    text1,
    fake_pattern
)

test_algorithm(
    "KMP",
    kmp_search,
    text1,
    fake_pattern
)

test_algorithm(
    "Rabin-Karp",
    rabin_karp_search,
    text1,
    fake_pattern
)


print("\n========== ARTICLE 2 ==========\n")

print("Existing substring:\n")

test_algorithm(
    "Boyer-Moore",
    boyer_moore_search,
    text2,
    existing_pattern
)

test_algorithm(
    "KMP",
    kmp_search,
    text2,
    existing_pattern
)

test_algorithm(
    "Rabin-Karp",
    rabin_karp_search,
    text2,
    existing_pattern
)

print("\nFake substring:\n")

test_algorithm(
    "Boyer-Moore",
    boyer_moore_search,
    text2,
    fake_pattern
)

test_algorithm(
    "KMP",
    kmp_search,
    text2,
    fake_pattern
)

test_algorithm(
    "Rabin-Karp",
    rabin_karp_search,
    text2,
    fake_pattern
)
