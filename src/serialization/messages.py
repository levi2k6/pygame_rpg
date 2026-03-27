
class FileCorruptedException(Exception): 
    def __init__(self, data: str, fileName: str):
        message = f"Failed to read {data}, file {fileName} might be corrupted"
        super().__init__(message)


