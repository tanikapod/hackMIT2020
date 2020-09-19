from utils import text_to_speech
from Card import Card

class CardConcept(Card):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_back_definition(self, custom_text):
        self.back_text = custom_text
        self.back_audio = text_to_speech(self.back_text)
