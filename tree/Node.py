class Node:   

    def __init__(self, parent, word=False):
        self._letter = parent # can't modify after initialise 
        self._isWord = word
        self._child = []

    # parent
    def getTitle(self):
        return self._letter 

    # word
    def getWord(self):
        return self._isWord

    def setWord(self, val = None):
        self._isWord = val if val != None else not self._isWord

    # child property

    def getChild(self):
        return self._child

    def isEmpty(self):
        return len(self._child) == 0

    def addChild(self, newNode):
        self._child.append(newNode)

    def clearChild(self):
        self._child.clear()

    def getChildIndex(self, subchild):
        ind = 0

        while(ind < len(self._child)):
            if self._child[ind].getTitle() == subchild:
                return ind 
            ind += 1
        
        return -1

    def getChildObj(self, subchild):
        ind = 0

        while(ind < len(self._child)):
            if self._child[ind].getTitle() == subchild:
                return self._child[ind], ind 
            ind += 1
        
        return (None, -1)


    def getChildLen(self):
        return len(self._child)

    # delete child based on index
    def delitChild(self, ind):
        if ind < 0 or ind >= self.getChildLen():
            raise Exception('index is out of range')
        self._child.pop(ind)


