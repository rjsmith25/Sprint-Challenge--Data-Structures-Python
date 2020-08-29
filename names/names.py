import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# binary search tree implementation
class BSTNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    # Insert the given names into the tree lexicographical order, avoids duplicates
    def insert(self, name):
        # add name in right order if it comes before current name in tree
        if name < self.name:
            if not self.left:
                self.left = BSTNode(name)
                return
            self.left.insert(name)
        # add name in right order if comes after current name in tree
        elif name > self.name:
            if not self.right:
                self.right = BSTNode(name)
                return
            self.right.insert(name)
        else:
            return

    def contains(self, name):
        if self.name == name:
            return True

        if name < self.name:
            if not self.left:
                return False
            return self.left.contains(name)
        else:
            if not self.right:
                return False
            return self.right.contains(name)

    def getNames(self):
        names = []
        stack = []
        stack.append(self)

        while len(stack) > 0:
            current = stack.pop()

            names.append(current.name)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)
        return names


# insert names_1 into its own binary tree
bst1 = BSTNode(names_1[0])

for i in range(1, len(names_1)):
    bst1.insert(names_1[i])

# insert names_2 into its own binary tree
bst2 = BSTNode(names_2[0])

for i in range(1, len(names_2)):
    bst2.insert(names_2[i])

# compare name_1 to names_2 binary tree to find duplicates

bst1_names = bst1.getNames()
for name in bst1_names:
    if bst2.contains(name):
        duplicates.append(name)


# array implementation

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
