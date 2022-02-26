from collections import deque
import Node as nd

class Tree:

    # constructure
    def __init__(self):
        self.root = nd.Node("*")
        self.wordset = list()
        self.root.setWord()


    # get and print methods

    def getWordset(self):
        return self.wordset

    def getPreord(self):
        nodeorder = []
        Stack = deque([])
        nodeorder.append(self.root)
        Stack.append(self.root)

        while(len(Stack) > 0):
            flag = True

            if Stack[len(Stack) - 1].isEmpty():
                Stack.pop()
            else:
                prnt = Stack[len(Stack) - 1]

            for i in range(0, prnt.getChildLen()):
                childnode = prnt.getChild()[i] 
                if childnode not in nodeorder:
                    flag = not flag
                    Stack.append(childnode)
                    nodeorder.append(childnode)
                    break

            if flag:
                Stack.pop()

        return [(i.getTitle(), i.getWord()) for i in nodeorder]

    def getTree(self):
        def TreeList(obj):
            return (
                obj.getTitle(),
                list(map(TreeList, obj.getChild()))
            )
        return TreeList(self.root)[1]


    # add word

    def addWord(self, word):
        
        if word  not in self.wordset:
            self.wordset.append(word)

            currentNode = self.root
            for letter in word:

                ind = currentNode.getChildIndex(letter)

                if ind == -1:
                    newnode = nd.Node(letter)
                    currentNode.addChild(newnode)
                    currentNode = newnode
                else:
                    currentNode = (currentNode.getChild())[ind]

            currentNode.setWord(True)


    # delete word

    def clearTree(self):
        self.root.clearChild()

    def deleteWord(self, word):
        # case 1: word is substring of tree -> change isword = False
        # case 2: word is goint towords leaf -> last disting obj -> clearchild
        if word not in self.wordset:
            return -1, f'{word} is not avalable in tree'

        indObj = self.root
        parentObj = self.root
        ind = 0
        
        while ind < len(word):

            # find word index from child if valable
            childObj, cind = parentObj.getChildObj(word[ind])
            
            # if child is not thair return -1
            if  childObj == None:
               return -1, f'"{word}" is not avalable in tree'


            # child is more than one, update indObj
            if parentObj.getChildLen() > 1 or parentObj.getWord():
                indObj = parentObj

            parentObj = childObj

            ind += 1

        if not childObj.getWord():
            return 0, f'"{word}" can not be deleted'

        if childObj.isEmpty():
            indObj.delitChild(cind)
            self.wordset.remove(word)
            return 1, f'"{word}" is deleted sucessfully*'
        else:
            childObj.setWord(False)
            self.wordset.remove(word)
            return 1, f'"{word}" is deleted sucessfully'
     

    # suggest word

    def suggestWord(self, pathstack, char, n = 3):
        ans = []
        # ans = [], char = t
        # pathstack = [(self.root, ""), ]

        def traversetree(tobj):
            nodeorder = []
            Stack = deque([])
            Stack.append(tobj)
            nodeorder.append(tobj[0])
            prnt = ""
            
            
            while(len(Stack) > 0 and len(ans) != n):
                flag = True

                if Stack[len(Stack) - 1][0].isEmpty():
                    Stack.pop()
                else:
                    prnt, prestring = Stack[len(Stack) - 1]
                    

                if prnt == "" or not Stack:
                    break

                for i in range(0, prnt.getChildLen()):
                    childnode = prnt.getChild()[i] 
                    if childnode not in nodeorder:
                        flag = not flag

                        newWord = prestring + childnode.getTitle()
                        Stack.append((childnode, newWord))
                        nodeorder.append(childnode)

                        if childnode.getWord() and newWord not in ans:
                            ans.append(newWord)

                        break


                if flag:
                    Stack.pop()
            

        obj, pstring = pathstack[len(pathstack) - 1]
        cobj, ind = obj.getChildObj(char)

        if(ind != -1):
            newWord = pstring + char
            if cobj.getWord() and newWord not in ans:
                ans.append(newWord)
            traversetree((cobj, newWord))
            pathstack.append((cobj, char) if obj.getTitle() == "*" else (cobj, newWord))

        return ans, pathstack

            
                    


        

        

    def suggestAndAdd(self):
        word = ""
        char = ""
        isaddword = False

        while char != "/":
            char = input()[0]

            if not isaddword:
                k = self.suggestWord([(t.root, "")] if word == "" else k[1], char)

                if k[0] :
                    for i in k[0]:
                        print("- ",i)
                else:
                    isaddword = True

            word += char

        self.addWord(word[:-1:1])
        return self.getWordset()
            

if __name__ == "__main__":
    t = Tree()
    t.addWord('too')
    t.addWord('tea')
    t.addWord('took')
    t.addWord('teach')
    t.addWord('tops')
    t.addWord('true')
    t.addWord('truck')
    t.addWord('trust')
    t.addWord('teo')
    print(t.getWordset())
    print(t.getPreord())
    print(t.getTree())
    print(t.getWordset())
    print(t.deleteWord('tea'))
    print(t.getWordset())
    print(t.getPreord())
    print(t.getTree())
    print("*")
    k = t.suggestWord([(t.root, "")], "t", 5)
    print(k[0])
    k = t.suggestWord(k[1], "r")
    print(k[0])
    k = t.suggestWord(k[1], "u")
    print(k[0])
    k = t.suggestWord(k[1], "c")
    print(k[0])
    k = t.suggestWord(k[1], "k")
    print(k[0])
    print(t.suggestAndAdd())
