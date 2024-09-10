class PossibilityMatrix:

    def __init__(self, wordList: list[str]) -> None:
        self.refresh(wordList)

    def refresh(self, wordList: list[str]):
        self.wordList = wordList.copy()
        self.generatePossibilityMatrix()
        self.holdWordsSet = set()

    def isEmpty(self, ignoreHold: bool = False) -> bool:
        if ignoreHold:
            return len(self.wordList) == 0
        return len(list(filter(lambda word: word not in self.holdWordsSet, self.wordList))) == 0

    def getWordByIndex(self, index: int) -> str:
        return self.wordList[index]

    def holdWord(self, word: str) -> None:
        self.holdWordsSet.add(word)

    def unHold(self, word: str) -> None:
        self.holdWordsSet.discard(word)

    def getPossibleWords(self, char: str, ignoreHold: bool = False) -> list[str]:
        colIndex = self.columnMapping[char]
        possibleWords = []

        for wordIndex in range(len(self.wordList)):
            if self.matrix[wordIndex][colIndex] != None:
                possibleWords.append(
                    {
                        "word": self.wordList[wordIndex],
                        "positions": self.matrix[wordIndex][colIndex]
                    }
                )
        if ignoreHold:
            return possibleWords

        return list(filter(lambda x: x["word"] not in self.holdWordsSet, possibleWords))

        # filter based on holdList

    def getCharCount(self) -> dict[str, dict[str, any]]:

        countDict = dict()
        keyExists: callable[[str], bool] = lambda x: x in countDict.keys()

        for word in self.wordList:
            for c in word:
                if keyExists(c):
                    countDict[c]["count"] += 1
                    countDict[c]["possibleWords"].append(
                        {
                            "word": word,
                            "positions": [i for i, char in enumerate(word) if char == c]
                        }
                    )
                else:
                    countDict[c] = {
                        "count": 1,
                        "possibleWords": [{
                            "word": word,
                            "positions": [i for i, char in enumerate(word) if char == c]
                        }],
                    }
        return countDict

    """
    UseCase:
        - to count of each char
        - to get matrix with possibility state
    """

    def generatePossibilityMatrix(self):
        charStatistics = self.getCharCount()
        col = sorted(list(charStatistics.keys()))
        matrix = [
            [None for _ in range(len(col))] for _ in range(len(self.wordList))
        ]

        countMapping = dict()
        columnMapping = dict()
        for colIndex, char in enumerate(col):
            columnMapping[char] = colIndex
            countMapping[char] = charStatistics[char]['count']
            for wordDict in charStatistics[char]['possibleWords']:
                rowIndex = self.wordList.index(wordDict["word"])
                matrix[rowIndex][colIndex] = wordDict["positions"]

        rowMapping = dict()
        for index, word in enumerate(self.wordList):
            rowMapping[word] = index

        self.rowMapping: dict[str, int] = rowMapping
        self.columnMapping: dict[str, int] = columnMapping
        self.countMapping: dict[str, int] = countMapping
        self.matrix = matrix

    def removeWord(self, word) -> None:

        if word not in self.wordList:
            raise Exception("Word does not exists")

        # get matrix index
        matrixRowIndex = self.rowMapping[word]

        # decrees count
        for char in word:
            self.countMapping[char] -= 1

        # remove word from rowMappings
        for rowWord in self.rowMapping:
            if rowWord == word:
                continue
            if self.rowMapping[rowWord] > matrixRowIndex:
                self.rowMapping[rowWord] -= 1
        del self.rowMapping[word]

        # mark possibility as False
        self.matrix.pop(matrixRowIndex)

        # remove word from wordList
        self.wordList.pop(self.wordList.index(word))
