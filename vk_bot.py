import os
import random
from dotenv import load_dotenv
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

from detect_intents import detect_intents


def process_message(project_id, event, vk_api):
    response = detect_intents(project_id, event.user_id, event.text, language_code="ru-ru")
    if not response.intent.is_fallback:
        message = response.fulfillment_text
        vk_api.messages.send(
            user_id=event.user_id,
            message=message,
            random_id=random.randint(1,1000)
        )


def main():
    load_dotenv()
    
    project_id = os.getenv("GOOGLE_PROJECT_ID")

    vk_token = os.getenv("VK_TOKEN")
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:    
            process_message(project_id, event, vk_api)
     

if __name__ == "__main__":
    main()
