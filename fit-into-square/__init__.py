
from typing import List, Final
from util import PossibilityMatrix
import copy


class SquareWord:

    LEFT_TO_RIGHT: Final = 0
    UP_TO_BOTTOM: Final = 1
    RIGHT_TO_LEFT: Final = 2
    BOTTOM_TO_UP: Final = 3
    DIAGONAL_DOWN: Final = 4
    DEFAULT_VALUE: Final = None

    def getNextDirection(self, direction: int) -> int | None:
        match direction:
            case self.LEFT_TO_RIGHT:
                return self.UP_TO_BOTTOM
            case self.UP_TO_BOTTOM:
                return self.DIAGONAL_DOWN
            case _:
                return None

    def getNextStep(self, direction: int, currentRow: int, currentColumn: int) -> List[int]:
        match direction:
            case self.LEFT_TO_RIGHT:
                return [currentRow, currentColumn + 1]
            case self.UP_TO_BOTTOM:
                return [currentRow + 1, currentColumn]
            case self.RIGHT_TO_LEFT:
                return [currentRow, currentColumn - 1]
            case self.BOTTOM_TO_UP:
                return [currentRow - 1, currentColumn]
            case _:
                return [currentRow + 1, currentColumn + 1]

    def __init__(self, words) -> None:
        self.words = self.refineWordList(words)
        self.maxLen = max([len(w) for w in words])
        self.wordsMatrix = None
        self.matrix = PossibilityMatrix(self.words)

    """
    UseCase:
        - to refine initial words by removing duplicate words and empty words.
        - make words trim and lower
        - sort list by length as max length to min length
    """

    def refineWordList(self, wordList: List[str]) -> List[str]:
        wordSet = set()
        for word in wordList:
            word = word.strip().lower()
            if not (word == "" or word in wordSet or word[::-1] in wordSet):
                wordSet.add(word)
        return sorted(list(wordSet), key=lambda x: len(x), reverse=True)

    """
        Approach:
            - first fit longest word in first row and check if other can fit like that
            - if other's can't fit in it retry with longest word in second, third ... rows
            - if non of this word start with diagonal
            - say fit not possible
    """

    def fit(self) -> list[list[list[str | None]]]:

        # start to fit word in every row

        AnswerMatrix = []
        for rowIndex in range(self.maxLen):

            # get longest words
            # TODO: if two words found

            self.matrix.refresh(self.words)
            longestWord = self.matrix.getWordByIndex(0)

            # create new empty matrix
            self.wordsMatrix = [
                [self.DEFAULT_VALUE for _ in range(self.maxLen)] for _ in range(self.maxLen)
            ]

            # spread our longest word into rowIndex
            self.wordsMatrix[rowIndex] = [char for char in longestWord]

            # remove that word from possibility matrix
            self.matrix.removeWord(longestWord)

            # start iteration
            self.fitCheck(longestWord, SquareWord.LEFT_TO_RIGHT,
                          rowIndex, 0, self.wordsMatrix, AnswerMatrix)
        return AnswerMatrix

    def isOverlapPossible(self, word: str, rowIndex: int, colIndex: int, direction: int, matrix: list[list[str]]) -> bool:
        for char in word:
            if matrix[rowIndex][colIndex] != self.DEFAULT_VALUE and matrix[rowIndex][colIndex] != char:
                return False
            [rowIndex, colIndex] = self.getNextStep(
                direction, rowIndex, colIndex)
        return True

    def writeWord(self, matrix: list[list[str | None]], word: str, rowIndex: int, colIndex: int, direction: int) -> None:
        self.matrix.holdWord(word)
        for char in word:
            matrix[rowIndex][colIndex] = char
            [rowIndex, colIndex] = self.getNextStep(
                direction, rowIndex, colIndex)
        return matrix

    def checkLeftToRight(self, word: str, charPosition: int, currentRowIndex: int, currentColumnIndex: int, matrix: list[list[str]]):
        startingColumnIndex = currentColumnIndex - charPosition

        if startingColumnIndex < 0 or startingColumnIndex + len(word) - 1 >= self.maxLen:
            return self.DEFAULT_VALUE
        leftToWriteWordPossible = self.isOverlapPossible(word, currentRowIndex,
                                                         startingColumnIndex, self.LEFT_TO_RIGHT, matrix)
        if leftToWriteWordPossible:
            return {
                "matrix": self.writeWord(
                    matrix, word, currentRowIndex, startingColumnIndex, self.LEFT_TO_RIGHT),
                "rowIndex": currentRowIndex,
                "colIndex": startingColumnIndex,
                "direction": self.LEFT_TO_RIGHT
            }
        return self.DEFAULT_VALUE

    def checkUpToBottom(self, word: str, charPosition: int, currentRowIndex: int, currentColumnIndex: int, matrix: list[list[str]]):
        startingRowIndex = currentRowIndex - charPosition

        if startingRowIndex < 0 or startingRowIndex + len(word) - 1 >= self.maxLen:
            return self.DEFAULT_VALUE

        upToBottomWriteWordPossible = self.isOverlapPossible(word, startingRowIndex,
                                                             currentColumnIndex, self.UP_TO_BOTTOM, matrix)
        if upToBottomWriteWordPossible:
            return {
                "matrix": self.writeWord(
                    matrix, word, startingRowIndex, currentColumnIndex, self.UP_TO_BOTTOM),
                "rowIndex": startingRowIndex,
                "colIndex": currentColumnIndex,
                "direction": self.UP_TO_BOTTOM
            }
        return self.DEFAULT_VALUE

    def checkRightToLeft(self, word: str, charPosition: int, currentRowIndex: int, currentColumnIndex: int, matrix: list[list[str]]):
        startingColumnIndex = currentColumnIndex + charPosition

        if startingColumnIndex - len(word) + 1 < 0 or startingColumnIndex >= self.maxLen:
            return self.DEFAULT_VALUE

        leftToWriteWordPossible = self.isOverlapPossible(word, currentRowIndex,
                                                         startingColumnIndex, self.RIGHT_TO_LEFT, matrix)
        if leftToWriteWordPossible:
            return {
                "matrix": self.writeWord(
                    matrix, word, currentRowIndex, startingColumnIndex, self.RIGHT_TO_LEFT),
                "rowIndex": currentRowIndex,
                "colIndex": startingColumnIndex,
                "direction": self.RIGHT_TO_LEFT
            }
        return self.DEFAULT_VALUE

    def checkBottomToUp(self, word: str, charPosition: int, currentRowIndex: int, currentColumnIndex: int, matrix: list[list[str]]):
        startingRowIndex = currentRowIndex + charPosition

        if startingRowIndex - len(word) + 1 < 0 or startingRowIndex >= self.maxLen:
            return self.DEFAULT_VALUE

        upToBottomWriteWordPossible = self.isOverlapPossible(word, startingRowIndex,
                                                             currentColumnIndex, self.BOTTOM_TO_UP, matrix)
        if upToBottomWriteWordPossible:
            return {
                "matrix": self.writeWord(
                    matrix, word, startingRowIndex, currentColumnIndex, self.BOTTOM_TO_UP),
                "rowIndex": startingRowIndex,
                "colIndex": currentColumnIndex,
                "direction": self.BOTTOM_TO_UP
            }
        return self.DEFAULT_VALUE

    def fitCheck(self, previousWord: str, wordDirection: int, rowIndex: int, columnIndex: int, matrix: list[list[str]], answers: list = [], level: int = 1) -> bool:

        previousAnswerLength = len(answers)
        # check current and next char
        for currentChar in previousWord:
            possibleWord = self.matrix.getPossibleWords(currentChar)
            # print(previousWord, currentChar, possibleWord,
            #       wordDirection, rowIndex, columnIndex, answers, level)

            # for the given char check all possible words with all possible positions

            for word in possibleWord:
                currentWord = word["word"]
                positions = word["positions"]

                for charIndexInWord in positions:

                    newMatrix = self.checkLeftToRight(
                        currentWord, charIndexInWord, rowIndex, columnIndex, copy.deepcopy(matrix))
                    if newMatrix != self.DEFAULT_VALUE:
                        if self.matrix.isEmpty():
                            answers.append(newMatrix["matrix"])
                        else:
                            self.fitCheck(currentWord, newMatrix["direction"],
                                          newMatrix["rowIndex"], newMatrix["colIndex"], newMatrix["matrix"], answers, level + 1)
                        self.matrix.unHold(currentWord)

                    newMatrix = self.checkUpToBottom(
                        currentWord, charIndexInWord, rowIndex, columnIndex, copy.deepcopy(matrix))
                    if newMatrix != self.DEFAULT_VALUE:
                        if self.matrix.isEmpty():
                            answers.append(newMatrix["matrix"])
                        else:
                            self.fitCheck(currentWord, newMatrix["direction"],
                                          newMatrix["rowIndex"], newMatrix["colIndex"], newMatrix["matrix"], answers, level + 1)
                        self.matrix.unHold(currentWord)

                    newMatrix = self.checkRightToLeft(
                        currentWord, charIndexInWord, rowIndex, columnIndex, copy.deepcopy(matrix))
                    if newMatrix != self.DEFAULT_VALUE:
                        if self.matrix.isEmpty():
                            answers.append(newMatrix["matrix"])
                        else:
                            self.fitCheck(currentWord, newMatrix["direction"],
                                          newMatrix["rowIndex"], newMatrix["colIndex"], newMatrix["matrix"], answers, level + 1)
                        self.matrix.unHold(currentWord)

                    newMatrix = self.checkBottomToUp(
                        currentWord, charIndexInWord, rowIndex, columnIndex, copy.deepcopy(matrix))
                    if newMatrix != self.DEFAULT_VALUE:
                        if self.matrix.isEmpty():
                            answers.append(newMatrix["matrix"])
                        else:
                            self.fitCheck(currentWord, newMatrix["direction"],
                                          newMatrix["rowIndex"], newMatrix["colIndex"], newMatrix["matrix"], answers, level + 1)
                        self.matrix.unHold(currentWord)

                # after checking all possibilities increase step
            [rowIndex, columnIndex] = self.getNextStep(
                wordDirection, rowIndex, columnIndex)

        # print(self.matrix.isEmpty())
        return previousAnswerLength != len(answers)


# wordList = ["truck", "true", "eat", "top", "tap",
#             "pob", "took", "cook", "look"]
wordList = ["toy", "boy", "too"]
obj = SquareWord(wordList)
counter = 1
for answer in obj.fit():
    print(f"> answer {counter} <".center(50, "="))
    counter += 1

    for row in answer:
        print("[", end="")
        print(",".join(list(map(lambda x: x if x else " ", row))), end="")
        print("] ")
