def contains_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

print(contains_duplicates([1, 2, 3, 4, 5]))
print(contains_duplicates([1, 2, 3, 4, 1]))