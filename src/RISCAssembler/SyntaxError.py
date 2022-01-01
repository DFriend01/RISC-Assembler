class SyntaxError(Exception):

    def __init__(self, line="", errorcode=0, message="Syntax Error"):
        self.errorcode = errorcode
        self.line = line
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
