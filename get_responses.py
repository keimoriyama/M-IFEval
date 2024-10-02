from openai import OpenAI
import os
import anthropic
import vertexai
from vertexai.generative_models import GenerativeModel
import cohere

######## Anthropic ########

anthropic_client = anthropic.Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"],
)

def get_anthropic_response(input_text, model_name):

    message = anthropic_client.messages.create(
        model=model_name,
        max_tokens=2048,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": input_text
                    }
                ]
            }
        ]
    )
    return message.content[0].text

######## OpenAI ########

openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_openai_response(input_text, model_name):

    response = openai_client.chat.completions.create(
      model=model_name,
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": input_text
            }
          ]
        }
      ],
      temperature=0,
      max_tokens=2048,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      response_format={
        "type": "text"
      }
    )

    return response.choices[0].message.content

######## VertexAI ########

def get_vertex_response(input_text, model_name):
    generation_config = {
        "max_output_tokens": 2048,
        "temperature": 0,
        "top_p": 0.95,
    }

    safety_settings = [
    ]

    vertexai.init(project="dev-llab", location="asia-south1")
    model = GenerativeModel(
        model_name,
    )
    chat = model.start_chat(response_validation=False)

    return chat.send_message(
        [input_text],
        generation_config=generation_config,
        safety_settings=safety_settings
    ).candidates[0].content.parts[0].text