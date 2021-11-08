import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def send_message(message, assistant, assistant_id, session_id):
    response = assistant.message(
        assistant_id='{}'.format(assistant_id),
        session_id='{}'.format(session_id),
        input={
            'message_type': 'text',
            'text': message
        }
    ).get_result()


    return json.dumps({"intent":response['output']['intents'][0]["intent"], "entities":response['output']['entities'], "text":response['output']['generic'][0]['text']})


