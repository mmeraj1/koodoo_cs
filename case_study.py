from openai import OpenAI
import os

x = os.listdir('/Users/mohammadmeraj/Desktop/case_study_koodoo/casestudy')
y = [i for i in x if ".mp3" in i ]

for k in y:
  client = OpenAI(api_key = "sk-proj-eWpJcqP0sr7IWh9aUi0UT3BlbkFJeE6rpFjZUYj1qRD3dbcR")
  audio_file= open(k, "rb")
  transcription = client.audio.transcriptions.create(model="whisper-1", response_format="text",file=audio_file)
  print(transcription.text)
  print("--------------")
  print(audio_file)


