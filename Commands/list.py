from Authentication.auth import Auth


class List():
    @staticmethod
    def listAll():
        service = Auth.login()
        page_token = None
        while True:
            response = service.files().list(
                fields="nextPageToken, files(id, name)", pageToken=page_token).execute()

            for file in response.get('files', []):
                print ('File Name : ' + file.get('name') + ' ' + 'File Id : ' + file.get('id'))

            page_token = response.get('nextPageToken', None)

            if page_token is None:
                break

    @staticmethod
    def searchFile(filename):
        service = Auth.login()
        page_token = None
        while True:
            response = service.files().list(
                fields="nextPageToken, files(id, name)", q="name contains " + "'" + filename + "'",
                pageToken=page_token).execute()

            for file in response.get('files', []):
                print ('File Name : ' + file.get('name') + ' ' + 'File Id : ' + file.get('id'))

            page_token = response.get('nextPageToken', None)

            if page_token is None:
                break


    @staticmethod
    def searchFileById(file_id):
        service = Auth.login()
