from utils import text_to_speech, translate
from Card import Card

class CardTranslate(Card):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_back_definition(self):
        self.back_text = translate(self.front_text)
        self.back_audio = text_to_speech(self.back_text)
