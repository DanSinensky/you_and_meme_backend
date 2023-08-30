from you_and_meme_backend_app.models import Meme
import json

file = open('master.json')
data = json.load(file)

Meme.insert_many(data).execute()