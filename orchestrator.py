import queue
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from Chatbot.watson_message import send_message

# Initiate Watson session
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




print(send_message("Hello", assistant, assistant_id, session_id))





# Close Watson session when done
response = assistant.delete_session(
    assistant_id='{}'.format(assistant_id),
    session_id='{}'.format(session_id)
).get_result()