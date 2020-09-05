import queue
# A node of BFS traversal
class node:
    def __init__(self, val, level):
        self.val = val
        self.level = level
def minOperations(x, y):
    # To keep track of visited numbers
    # in BFS.
    visit = set()
    # Create a queue and enqueue x into it.
    q = queue.Queue()
    n = node(x, 0)
    q.put(n)

    # Do BFS starting from x
    while (not q.empty()):
        # Remove an item from queue
        t = q.get()
        # If the removed item is target
        # number y, return its level
        if (t.val == y):
            return t.level
            # Mark dequeued number as visited
        visit.add(t.val)
        # If we can reach y in one more step
        if (t.val * 2 == y or t.val - 1 == y):
            return t.level + 1
        # Insert children of t if not visited
        # already
        if (t.val * 2 not in visit):
            n.val = t.val * 2
            n.level = t.level + 1
            q.put(n)
        if (t.val - 1 >= 0 and t.val - 1 not in visit):
            n.val = t.val - 1
            n.level = t.level + 1
            q.put(n)
x = 4
y = 25
print(minOperations(x, y))
