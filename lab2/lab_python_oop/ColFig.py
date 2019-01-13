class ColFig:
    def __init__(self, color):
        self._col = color

    def getcol(self):
        return self._col

    def setcol(self, value):
        self._col = value

    def delcol(self):
        del self._col

    col = property(getcol, setcol, delcol)
