from openai import OpenAI
import os
import json

x = os.listdir('/Users/mohammadmeraj/Desktop/case_study_koodoo/casestudy')
y = [i for i in x if ".mp3" in i ]
f = open("key.json")
data = json.load(f)

for k in y:
  client = OpenAI(api_key = data["key"])
  audio_file= open(k, "rb")
  transcription = client.audio.transcriptions.create(model="whisper-1", response_format="text",file=audio_file)
  print(transcription.text)
  print("--------------")
  print(audio_file)






