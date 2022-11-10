import json


class PrimeHandlers():

    def __init__(self, fileName: str, configName: str) -> None:
        self.fileName = fileName + '.txt'
        self.configName = configName + '.json'
        self.fileObj = None
        self.fileMode = 'None'
        self.min = 0
        self.max = 0
        self.lines = 0
        self.__initFileObj()

    def __initFileObj(self):

        try:
            self.fileObj = open(self.fileName, 'x')
            print(f"{self.fileName} is created...")
        except:
            print(f"{self.fileName} is found...")
            pass
        finally:
            if self.fileObj != None:
                self.fileObj.close()
            self.fileObj = open(self.fileName, 'r')
            self.fileMode = 'Read'
            lines = 0
            for _ in self.fileObj:
                lines += 1

            self.lines = lines

        isConfigCreated = False
        try:
            configObj = open(self.configName, 'x')
            configObj.close()
            isConfigCreated = True
            print(f"{self.configName} is created...")

        except:
            print(f"{self.configName} is found...")
            pass
        finally:

            if not isConfigCreated:
                cfg = self.getConfig()

                if cfg['lines'] != self.lines:

                    self.__changeConfig(self.min, self.max, 0)

                    self.fileObj.close()
                    self.fileObj = open(self.fileName, 'w')
                    self.fileObj.write('')
                    self.fileMode = 'Write'
                    self.lines = 0
                else:
                    self.min = cfg['min']
                    self.max = cfg['max']

            else:
                self.__changeConfig(self.min, self.max, 0)

    def __changeConfig(self, min: int, max: int, lines: int) -> None:
        f = open(self.configName, 'w')
        json.dump({
            'min': min,
            'max': max,
            'lines': lines
        }, f)
        f.close()

    def getConfig(self) -> dict:
        f = open(self.configName, 'r')
        d = json.load(f)
        f.close()
        return d

    def writeFile(self, content: list, min: int, max: int) -> None:
        content = list(map(str, content))
        if self.fileMode != 'Write':
            self.fileObj.close()
            self.fileObj = open(self.fileName, 'w')
            self.fileMode = 'Write'

        for i in content:
            self.fileObj.write(i + "\n")
        self.__changeConfig(min, max, len(content))

        self.min = min
        self.max = max
        self.lines = len(content)

    def appendFile(self, content: list, max: int) -> None:
        content = list(map(str, content))
        if self.fileMode != 'Append':
            self.fileObj.close()
            self.fileObj = open(self.fileName, 'a')
            self.fileMode = 'Append'

        for i in content:
            self.fileObj.write(i + "\n")
        self.__changeConfig(self.min, max, self.lines + len(content))

        self.max = max
        self.lines = self.lines + len(content)

    def readFile(self) -> list:
        self.fileObj.close()
        self.fileObj = open(self.fileName, 'r')
        self.fileMode = 'Read'
        content = []

        for i in self.fileObj:
            content.append(int(i))

        return content

    def getOrWriteOrAppend(self, min: int, max: int) -> bool:
        d = self.getConfig()
        # 0 -> get, 1 -> write, 2 -> append
        if min == d['min'] and max <= d['max']:
            return 0
        elif min == d['min'] and max > d['max']:
            return 2
        else:
            return 1

    def getLines(self):
        return self.lines

    def getMax(self):
        return self.getConfig()['max']


if __name__ == "__main__":
    def test(obj: PrimeHandlers, n, m):
        k = obj.getOrWriteOrAppend(n, m)
        if k == 1:
            obj.writeFile([i for i in range(n, m)], n, m)
        elif k == 2:
            obj.appendFile([i for i in range(n, m)], m)
        else:
            print(obj.readFile())

        print(obj.getConfig(), k, obj.readFile())

    obj = PrimeHandlers('PrimList', 'PrimConfig')

    print(obj.getConfig())
    test(obj, 2, 10)
    test(obj, 5, 25)
    test(obj, 2, 7)
    test(obj, 2, 25)
