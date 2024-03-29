import streamlit as st 
import google.generativeai as genai
import requests
from apikey import *




genai.configure(api_key=google_gemini_api_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.set_page_config("MovieGPT")
st.title("MovieGPT")
st.subheader("Merhaba. Ben MovieGPT. Bugün ne izlemek istersiniz ?")
user_input=st.text_input("Ne izlemek istersiniz?")
submit_button=st.button("Recommend Movie")

prompt_parts = [
  f"Senin adın MovieGPT .Sen arkadaş canlısı bir film tavsiyesi görevinde özelleşmiş chatbotsun.Senin işin kullanıcıdan alınan film adı,film türü,yönetmen,oyuncu,imdb puanı  parametrelerine göre kullanıcıya film tavsiyesi yapmak. Kullanıcı {user_input} şeklinde bir prompt verdiğinde prompta var olan parametrelere göre benzer 10 filmin ismini,türünü,yönetmeni,oyuncusu ve film özetini ekrana yazdırmalısın. Film bilgilerini sırasıyla film adı,film türü,film yönetmeni,filmin oyuncuları,filmin Imdb puanı ve film özeti olmak üzere alt alta 6 satır şeklinde yazmalısın. ",
  " "
]


if submit_button and user_input:
  response = model.generate_content(prompt_parts)
  bot_response=response.text
  st.write(bot_response)




  





    






    
    