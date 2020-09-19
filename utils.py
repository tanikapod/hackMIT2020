import requests
import os
import sys
from api_keys import TRANSLATE_KEY, TRANSCRIBE_KEY, SYNTHESIZE_KEY, DICTIONARY_KEY
from ibm_watson import TextToSpeechV1, SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.websocket import RecognizeCallback, AudioSource


TRANSLATE_URL = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/a4798b09-44a7-4ede-994a-aeb074163e52/v3/translate?version=2018-05-01"

TRANSCRIBE_URL = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/2e753c43-d5d6-4c7b-b240-c82a18e3d547/v1/recognize"
speech2txt = SpeechToTextV1(authenticator=IAMAuthenticator(TRANSCRIBE_KEY))
speech2txt.set_service_url(TRANSCRIBE_URL)

SYNTHESIZE_URL = "https://api.us-south.text-to-speech.watson.cloud.ibm.com"
txt2speech = TextToSpeechV1(authenticator=IAMAuthenticator(SYNTHESIZE_KEY))
txt2speech.set_service_url(SYNTHESIZE_URL)

DICTIONARY_URL = "https://owlbot.info/api/v4/dictionary/"

THIS_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))


class TranscriberCallbacks(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)
        self.transcript = ""

    def on_data(self, data):
        self.transcript += data["results"][0]["alternatives"][0]["transcript"] + " "

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))


def text_to_speech(text, audio_file, target_lang="en-US_AllisonV3Voice"):
    audio_path = "{}/{}".format(THIS_PATH, audio_file)
    print("transcribing to: {}".format(audio_path))

    with open("audio.wav", "wb") as audio:
        audio.write(txt2speech.synthesize(text=text,
                                          accept="audio/wav",
                                          voice=target_lang).get_result().content)
    #
    # requests.post(url=TXT_TO_SPEECH_URL,
    #               headers={"Content-Type":"application/json",
    #                 "Accept":"audio/wav"},
    #               params={"output":audio_path,
    #                       "voice":target_lang},
    #               json={"text":text},
    #               auth=("apikey", TXT_TO_SPEECH_KEY))

def speech_to_text(audio_file, source_lang="en-US_BroadbandModel"):
    audio_path = "{}/{}".format(THIS_PATH, audio_file)
    print("transcribing from: {}".format(audio_path))

    callbacks = TranscriberCallbacks()

    with open(audio_path, "rb") as f:
        audio_source = AudioSource(f)
        speech2txt.recognize_using_websocket(audio=audio_source,
                                             content_type="audio/flac",
                                             recognize_callback=callbacks,
                                             model=source_lang)

    print("transcript: {}\n".format(callbacks.transcript))

    return callbacks.transcript

def translate(text, source_lang="en", target_lang="es"):
    try:
        result = requests.post(url=TRANSLATE_URL,
                               headers={"Content-Type":"application/json"},
                               json={"text":[text],
                                     "model_id":source_lang + "-" + target_lang},
                               auth=("apikey", TRANSLATE_KEY))
    except: print(result.json())

    translation = result.json()["translations"][0]["translation"]

    print("{}: {}\n{}: {}\n".format(source_lang,
                                    text,
                                    target_lang,
                                    translation))

    return translation

def define(text):
    try:
        headers = {'Authorization': 'Token '+ DICTIONARY_KEY,}
        result = requests.get('https://owlbot.info/api/v4/dictionary/' + text, headers=headers)
    except: print(result.json())

    type = result.json()["definitions"][0]["type"]
    definitions = result.json()["definitions"][0]["definition"]

    print("{}\n{}: {}".format(text, type, definitions))
    return type, definitions

if __name__ == "__main__":
    # translation = translate(text="Hello world!",
    #                         source_lang="en",
    #                         target_lang="es")

    # speech_to_text(audio_file="testing_audio.m4a",
    #                source_lang="en-US_BroadbandModel")

    text_to_speech(text="hello world",
                   audio_file="audio.wav")

    # text_to_speech(text=translation,
    #                audio_file="audio.wav",
    #                target_lang="es-ES_EnriqueVoice")

    # definition = define(text = 'hello')