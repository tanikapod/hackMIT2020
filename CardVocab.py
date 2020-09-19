from utils import text_to_speech, define
from Card import Card

class CardVocab(Card):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_back_definition(self):
        self.back_text = define(self.front_text)
        self.back_audio = text_to_speech(self.back_text)
