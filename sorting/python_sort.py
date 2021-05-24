# Timsort
# Time Complexity- O(nlogn)
# Space Complexity- O(n)

# list.sort(key=, reverse=)
# 1. built in functions for lists
# 2. modifies current list
a = [5,6,7,8,64,32,42,30]
a.sort()
print(a)


b = ['hell', 'oo', 'everg']
b.sort(key=len, reverse=True)

print(b)

c = ['hell', 'oo', 'everg']
# sorted(iterables, key=, reverse=)
print(sorted(c, key=len, reverse=False))
