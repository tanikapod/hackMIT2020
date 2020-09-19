import requests
import os
import sys
from api_keys import TRANSLATE_KEY, SPEECH_REC_KEY

TRANSLATE_URL = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/a4798b09-44a7-4ede-994a-aeb074163e52/v3/translate?version=2018-05-01"

SPEECH_REC_URL = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/2e753c43-d5d6-4c7b-b240-c82a18e3d547/v1/recognize"

DEFINE_URL = ""

this_path = os.path.dirname(os.path.realpath(sys.argv[0]))

def text_to_speech(text):
    raise NotImplementedError

def speech_to_text(audio_file, source_lang="en-US_BroadbandModel"):
    audio_path = "@{}/{}".format(this_path, audio_file)
    print("transcribing from: {}".format(audio_path))

    try:
        result = requests.post(url=SPEECH_REC_URL,
                               headers={"Content-Type":"audio/flac",
                                        "Transfer-Encoding":"chunked"},
                               params={"model":source_lang},
                               json={"data-binary":audio_path},
                               auth=("apikey", SPEECH_REC_KEY))
    except: print(result.json())

    print(result.json())

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
    raise NotImplementedError

if __name__ == "__main__":
    translate(text="Hello world!",
              source_lang="en",
              target_lang="es")

    # speech_to_text(audio_file="audio-file.flac",
    #                source_lang="en-US_BroadbandModel")
