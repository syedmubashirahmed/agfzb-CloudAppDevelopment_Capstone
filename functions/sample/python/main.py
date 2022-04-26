#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#


#
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(dict):
    databaseName = "dealerships"

    try:
        client = Cloudant.iam(
            account_name=dict["COUCH_USERNAME"],
            api_key=dict["IAM_API_KEY"],
            connect=True,
        )
        print("Databases: {0}".format(client.all_dbs()))
    except CloudantException as ce:
        print("unable to connect")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}
    

dict={
  "IAM_API_KEY": "6COGnWPRUVwZ0QsBCYFGAvA53MjNAtgbkLd1XHicSglm",
  "host": "fbcd12ae-b980-4832-8e9b-57526f7a52ad-bluemix.cloudantnosqldb.appdomain.cloud",
  "iam_apikey_description": "Auto-generated for key crn:v1:bluemix:public:cloudantnosqldb:au-syd:a/2d8bc3f0f518465d92fc2c0cd0008ded:8d112daf-62bb-4a52-b963-e0c6cc19be72:resource-key:daa33066-74f5-4b7b-abbf-3b66d7c9a6de",
  "iam_apikey_name": "for-guestbook",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/2d8bc3f0f518465d92fc2c0cd0008ded::serviceid:ServiceId-6448d0a4-bbcb-4749-9ccb-93577e618c2f",
  "URL": "https://fbcd12ae-b980-4832-8e9b-57526f7a52ad-bluemix.cloudantnosqldb.appdomain.cloud",
  "COUCH_USERNAME": "fbcd12ae-b980-4832-8e9b-57526f7a52ad-bluemix"
}
print(main(dict))
