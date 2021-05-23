import heapq

pq = [3,6,1,0,8,4]
heapq.heapify(pq)

print(f'Heapify- {pq}')

heapq.heappush(pq, 2)

print(f'Push- {pq}')

print(f'Pop- {heapq.heappop(pq)}')
print(f'After Pop- {pq}')

# Given element is pushed then least element is poped
print(f'PushPop- {heapq.heappushpop(pq, 0)}')

# Least elment is poped then given element is pushed
print(f'Replace- {heapq.heapreplace(pq, 0)}')

print(f'nlargest- {heapq.nlargest(2, pq)}')
print(f'After nlargest- {pq}')

print(f'nsmallest- {heapq.nsmallest(2, pq)}')
print(f'After nsmallest- {pq}')
