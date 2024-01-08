# app/utils.py
import random
import string

from app.models import ShortLink


def generate_unique_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for i in range(length))
    # Check if the generated code is unique in the database
    while ShortLink.query.filter_by(short_code=short_code).first():
        short_code = ''.join(random.choice(characters) for i in range(length))
    return short_code
