from CardTranslate import CardTranslate

callbacks = {"highlight":highlight,
             "back_text":back_text,
             "back_notes":back_notes}

def highlight(highlighted_text):
    card = Card(front_text = highlighted_text)
    card.find_examples()
    return card

def back_text(card, entered_text):
    card.set_back_definition(entered_text)

def back_notes(card, entered_text):
    card.set_notes(entered_text)
