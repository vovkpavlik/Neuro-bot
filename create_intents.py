import os
import json

from dotenv import load_dotenv
from google.cloud import dialogflow


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []

    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)

        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )


def main():
    load_dotenv()

    with open("intents.json", "r") as f:
        intents_contents = json.load(f)

    project_id = os.getenv("GOOGLE_PROJECT_ID")

    for title, content in intents_contents.items():
        create_intent(project_id, title, content["questions"], [content["answer"]])


if __name__ == "__main":
    main()
    