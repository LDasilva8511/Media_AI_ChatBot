from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ExtractGenreEntity(Action):
    def name(self) -> Text:
        return "action_extract_genre_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        genre_entity = next(tracker.get_latest_entity_values('genre'), None)

        if genre_entity:
            dispatcher.utter_message(text=f"You have selected {genre_entity} as your genre choice")
        else:
            dispatcher.utter_message(text="I am sorry, I could not detect that genre choice")

        return []


class PickGenreAction(Action):
    def name(self) -> Text:
        return "action_pick_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Which genre would you like to know about?")

        return []

class ConfirmGenreAction(Action):
    def name(self) -> Text:
        return "action_confirm_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        genre_entity = next(tracker.get_latest_entity_values('genre'), None)

        if genre_entity:
            dispatcher.utter_message(text=f"You have selected {genre_entity} as your genre choice")
        else:
            dispatcher.utter_message(text="I am sorry, I could not detect that genre choice")

        return []
