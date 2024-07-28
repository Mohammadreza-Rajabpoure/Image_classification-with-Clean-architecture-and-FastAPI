class StoregFolderExistError(Exception):

    def __init__(self, message='StoregFolderExistError: storeg folder is not exist'):
        self.message = message
        super().__init__(message)

    def storeg_exist(self):
        return print(self.message)