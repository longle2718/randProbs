'''
Least-Frequent-Used Cache

Long Le <longle1@illinois.edu>
University of Illinois
'''

class BinNode:
    def __init__(self, count):
        self.cnt = count
        self.keys = []
        self.next = None
        self.prev = None

class LFUBin:
    def __init__(self):
        self.nodeMap = {}
        self.binHead = BinNode(0) # dummy node

    def push(self,key):
        if key not in self.nodeMap:
            node = self.binHead
        else:
            node = self.nodeMap[key]
            
        if node.next == None:
            # insert new BinNode  at the end
            node.next = BinNode(node.cnt+1)
            node.next.prev = node
            node.next.keys.append(key)
        elif node.next.cnt == node.cnt + 1:
            # append key to an existing node
            node.next.keys.append(key)
        else:
            # insert new BinNode in between
            tmp = BinNode(node.cnt+1)
            tmp.keys.append(key)
            tmp.prev = node
            tmp.next = node.next

            node.next.prev = tmp
            node.next = tmp

        if len(node.keys) > 0:
            node.keys.remove(key)
        if node!= self.binHead and len(node.keys) == 0:
            # remove node
            node.prev.next = node.next
            node.next.prev = node.prev

        self.nodeMap[key] = node.next

    def pop(self):
        if self.binHead.next == None:
            return None

        node1 = self.binHead.next
        if len(node1.keys) > 0:
            lfuKey = node1.keys.pop(0)
        if len(node1.keys) == 0:
            # remove node1
            node1.prev.next = node1.next
            node1.next.prev = node1.prev

        del self.nodeMap[lfuKey]
        return lfuKey

        return None

class LFUCache:
    def __init__(self,capacity):
        self.cap = capacity
        self.valueMap = {}
        self.mLFUBin = LFUBin()

    def get(self,key):
        if key in self.valueMap:
            self.mLFUBin.push(key)
            return self.valueMap[key]
        else:
            return -1

    def put(self,key,value):
        if len(self.valueMap) >= self.cap:
            lfuKey = self.mLFUBin.pop()
            del self.valueMap[lfuKey]

        self.valueMap[key] = value
        self.mLFUBin.push(key)
        return None
