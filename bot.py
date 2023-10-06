import openai
openai.api_key=(" paste your api key here")
print("Hello, I am hackz bot,How can I help you\n")
text=""
while(text!="exit"):
  text = input("\n")
  response=openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {
              "role": "system",
              "content":"you are a hackzbot and you are very helpful. you are a website chatbot and the website has the following features such as hackathon listings,host a hackathon and  your role is to answer them everything related to hackathons and you should also answer about hackz website with the hosting,listings of hackathons features  "

          },
          {
              "role": "assistant",
              "content": "provide the answers accurately in 50 words"

          },
          {
              "role": "user",
              "content":text
          }
        ],
      temperature=0,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
  )
  #print(response)
  generated_text=response.choices[0].message.content.strip()
  print(generated_text)
