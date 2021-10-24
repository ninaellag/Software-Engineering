import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

assistant_id = "e2bdf1fe-fbb7-4fe2-a047-5fe277167367"

authenticator = IAMAuthenticator('1vaPOr2csjCYbvkSC5YWhclDzplzowEi9EgPUZI0n6yx')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
)

assistant.set_service_url('https://api.eu-de.assistant.watson.cloud.ibm.com/instances/bd1a6c20-81b8-49c4-8d16-127239754cac')

response = assistant.create_session(
    assistant_id='{}'.format(assistant_id)
).get_result()

session_id = response['session_id']

message = input("You: ")

while message != "":


    response = assistant.message(
        assistant_id='{}'.format(assistant_id),
        session_id='{}'.format(session_id),
        input={
            'message_type': 'text',
            'text': 'Hello'
        }
    ).get_result()

    print("Bot: ", response['output']['generic'][0]['text'])
    #print(json.dumps(response, indent=2))
    print("\n")

    message = input("You: ")



response = assistant.delete_session(
    assistant_id='{}'.format(assistant_id),
    session_id='{}'.format(session_id)
).get_result()



exit()
