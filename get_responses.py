import os

class ResponseGenerator:
    def __init__(self, model_name):
        raise NotImplementedError
    
    def get_response(self, input_texts):
        raise NotImplementedError

######## Anthropic ########

class AnthropicResponseGenerator(ResponseGenerator):

    def __init__(self, model_name):
        import anthropic
        self.anthropic_client = anthropic.Anthropic(
            api_key=os.environ["ANTHROPIC_API_KEY"],
        )
        self.model_name = model_name
    
    def get_response(self, input_texts):
        return [
            self.anthropic_client.messages.create(
                model=self.model_name,
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
            ).message.content[0].text for input_text in input_texts
        ]

######## OpenAI ########

class OpenaiResponseGenerator(ResponseGenerator):
    def __init__(self, model_name):
        from openai import OpenAI

        self.openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.model_name = model_name
    
    def get_response(self, input_texts):
        return [
            self.openai_client.chat.completions.create(
                model=self.model_name,
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
                # top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                response_format={"type": "text"}
            ).choices[0].message.content for input_text in input_texts
        ]

######## VertexAI ########

class VertexResponseGenerator(ResponseGenerator):
    def __init__(self, model_name):
        self.model_name = model_name
    
    def get_response(self, input_texts):
        import vertexai
        from vertexai.generative_models import GenerativeModel

        generation_config = {
            "max_output_tokens": 2048,
            "temperature": 0,
        }

        safety_settings = [
        ]

        vertexai.init(project="dev-llab", location="asia-south1")
        model = GenerativeModel(
            self.model_name,
        )

        def get_vertex_response(input_text):
            chat = model.start_chat(response_validation=False)

            return chat.send_message(
                [input_text],
                generation_config=generation_config,
                safety_settings=safety_settings
            ).candidates[0].content.parts[0].text

        return [get_vertex_response(input_text) for input_text in input_texts]
        


######## vLLM ########

class VllmResponseGenerator(ResponseGenerator):
    def __init__(self, model_name):
        from vllm import LLM, SamplingParams
        self.model_name = model_name
        self.llm = LLM(model=self.model_name)
        self.sampling_params = SamplingParams(temperature=0.0, max_tokens=2048)

    def get_response(self, input_texts):
        input_conversations = [[{
            "role": "user",
            "content": input_text
        }] for input_text in input_texts]
        
        outputs = self.llm.chat(input_conversations,
                   sampling_params=self.sampling_params,
                   use_tqdm=True)
        return [output.outputs[0].text for output in outputs]