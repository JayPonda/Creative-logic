class FileOperation():

    def __init__(self, filePath: str) -> None:
        self.fileName = filePath
        self.file = open(self.fileName, 'a')
        self.title = ""
        self.content = ""
        self.writable = True
        self.entry = 0
        self.filecontent = None

    def addRow(self, msg, title, content) -> None:
        self.filecontent = None
        if not self.writable:
            self.close()
            self.file = open(self.fileName, 'a')
            self.writable = True
        self.entry += 1
        print(self.entry)
        self.title = title
        self.content = content
        self.file.write(msg + "\n")

    def readLastRow(self):
        return "" if self.entry == 0 else "{'title': {self.title}, 'content': {self.content}}"

    def readAll(self, reopen: bool = False):
        if self.writable or reopen:
            self.close()
            self.file = open(self.fileName, 'r')
            self.writable = False
        ans = []
        for line in self.file:
            ans.append(line)
        return ans

    def prepareWallFile(self):
        if self.filecontent == None:
            self.filecontent = self.readAll(True)
            return {
                'query': 'getAll',
                'unique': 1,
                'data': self.filecontent
            }
        else:
            return {
                'query': 'getAll',
                'unique': 0,
                'data': self.filecontent
            }

    def close(self):
        self.file.close()

    def clearFile(self):
        self.close()
        open(self.fileName, "w").close()
        self.file = open(self.fileName, 'a')
        self.title = ""
        self.content = ""
        self.writable = True
        self.entry = 0
        self.filecontent = None
