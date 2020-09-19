from utils import text_to_speech
from abc import ABC, abstractmethod

# TODO: make hashable?

class Card(ABC):
    def __init__(self, front_text):
        self.front_text = front_text
        self.front_audio = utils.text_to_speech(front_text)

        self.back_text = ""
        self.back_audio = None

        self.notes = ""
        self.examples = self.find_examples()

    @abstractmethod
    def set_back_definition(self, **kwargs):
        raise NotImplementedError

    def set_notes(self, text):
        self.notes = text

    @abstractmethod
    def find_examples(self):
        raise NotImplementedError
