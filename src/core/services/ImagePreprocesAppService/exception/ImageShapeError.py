class ImageShapeError(Exception):
    def __init__(self, message = 'ImageShapeError: image must be grayscale'):
        self.message = message
        super().__init__(message)

    def file_Shape(self):
        return print(self.message)