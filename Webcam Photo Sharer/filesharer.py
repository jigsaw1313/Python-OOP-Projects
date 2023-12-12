from filestack import Client


class FileSharer:
    """
    creates a link to generated report. use https://www.filestack.com/ to get API
    """

    def __init__(self, filepath, api_key=<YOUR-API-KEY>):
        self.file_path = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.file_path)
        return new_filelink.url
