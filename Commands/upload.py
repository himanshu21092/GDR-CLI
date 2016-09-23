from Authentication.auth import Auth

class Upload():
    @staticmethod
    def uploadSmallFile(files):
        service = Auth.login()
        for file in files:
            if '/' in file['filename']:
                filename = file['filename'].split('/')
                filename = filename[-1]
            else:
                filename = file['filename']

            metadata = {'name': filename}

            if file['mimetype']:
                metadata['mimeType'] = file['mimetype']
            print metadata


            res =service.files().create(body=metadata, media_body=file['filename']).execute()

            if res:
                print res
