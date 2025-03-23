import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        heapq.heappush(self.heap, val)
    
    def pop(self):
        return heapq.heappop(self.heap) if self.heap else None
    
    def reheapify(self, index):
        if index < 0 or index >= len(self.heap):
            return
        
        # Extract the element and replace it temporarily with the last element
        temp = self.heap[index]
        self.heap[index] = self.heap[-1]
        self.heap.pop()
        
        # Restore heap property
        heapq.heappush(self.heap, temp)
    
    def __str__(self):
        return str(self.heap)

# Testing reheapification
heap = MinHeap()
values = [10, 20, 15, 30, 40]
for v in values:
    heap.push(v)

print("Initial heap:", heap)

# Modify an element directly (simulate change)
heap.heap[2] = 5  # Assume element at index 2 is changed to 5
heap.reheapify(2)

print("Heap after reheapification:", heap)

# Test with deletion
heap.pop()
print("Heap after popping the min element:", heap)