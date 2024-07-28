class ImageExistError(Exception):

    def __init__(self, message='ImageExistError: image did not saved in storeg folder'):
        self.message = message
        super().__init__(message)

    def image_exist(self):
        return print(self.message)