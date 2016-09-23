from Authentication.auth import Auth
import json


class About:

    @staticmethod
    def aboutMe():
        service = Auth.login()
        response = service.about().get(
            fields="user").execute()

        data = json.dumps(response)
        user = json.loads(data)

        name = user['user']['displayName']
        email = user['user']['emailAddress']

        print name, email
