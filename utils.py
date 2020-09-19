import requests

from api_keys import IBM_API_KEY

TRANSLATE_URL = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/a4798b09-44a7-4ede-994a-aeb074163e52/v3/translate?version=2018-05-01"

def text_to_speech(text):
    raise NotImplementedError

def translate(text, source_lang, target_lang):
    data = {"text":[text],
            "model_id":source_lang + "-" + target_lang}
    result = requests.post(url=TRANSLATE_URL,
                           json=data,
                           auth=("apikey", IBM_API_KEY))
    translation = result.json()["translations"][0]["translation"]

    print("{}: {}\n{}: {}".format(source_lang,
                                  text,
                                  target_lang,
                                  translation))

    return translation

def define(text):
    raise NotImplementedError

# IBM Watson API's translation from English to Spanish
translate("Hello world!", "en", "es")
