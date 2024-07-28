

class FileNotFoundError(Exception):

    def __init__(self, message='FileNotFoundError: file doese not exist'):
        self.message = message
        super().__init__(self.message)

    def file_not_found(self):
        return print(self.message)

    