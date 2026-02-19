from database import get_hash

def has_changed(old_text, new_text):
    if old_text is None:
        return True
    return get_hash(old_text) != get_hash(new_text)
