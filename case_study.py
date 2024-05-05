from openai import OpenAI
import os
import json

f = open("key.json")
data = json.load(f)

x = os.listdir(data["file_locstion"])
y = [i for i in x if ".mp3" in i ]


for k in y:
  client = OpenAI(api_key = data["key"])
  audio_file= open(k, "rb")
  transcription = client.audio.transcriptions.create(model="whisper-1", response_format="text",file=audio_file)
  print(transcription.text)
  print("--------------")
  print(audio_file)






