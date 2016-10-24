from Authentication.auth import Auth
import io
from apiclient.http import MediaIoBaseDownload


class Download:
    @staticmethod
    def downloadById():
        service = Auth.login()
        file_id = '0B3kwBOfyQooNY0dtRXZJSHF6cnM'
        request = service.files().get_media(fileId=file_id)
        fh = io.FileIO('abcd.jpg', 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print "Download %d%%." % int(status.progress() * 100)

