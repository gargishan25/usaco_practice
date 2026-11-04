# Problem: Longest substring with at most K distinct characters
# Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.
# Examples
# s = "ecbea", k = 2 → 3 (substring "ec", but any of them works)
# s = "aa", k = 1 → 2 (substring "aa")
# s = "abc", k = 2 → 2 (e.g. "ab" or "bc")
# Constraints
# 1 <= s.length <= 10^5 (so aim for O(n), not nested scans that blow up)
# 0 <= k <= s.length
# s is lowercase English letters
string_ = "abaccc"
store = []
lengths = []
k=2
for i in string_:
    if len(store) >=k:
        if i not in store:
            if len(set(store)) < k:
                store.append(i)

            else:
                store.remove(store[0])
                store.append(i)
        elif i in store:
            store.append(i)    
    if len(set(store)) < k:
        store.append(i)

    while len(set(store)) > k:
        store.remove(store[0])
    lengths.append(len(store))
    print(store)

a = 0
for i in lengths:
    if i>a:
        a = i
print(a)