class ImagePathError(Exception):
    def __init__(self, message = 'ImagePathError:  image path does not exist maybe image dident saved '):
        self.message = message
        super().__init__(message)

    def image_path(self):
        return print(self.message)