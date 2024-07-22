from typing import Any, Dict, List
from lyzr_automata.ai_models.model_base import AIModel
from openai import OpenAI
from lyzr_automata.data_models import FileResponse
from lyzr_automata.utils.resource_handler import ResourceBox


class GPTVISION(AIModel):
    def __init__(self, api_key, parameters: Dict[str, Any]):
        self.parameters = parameters
        self.client = OpenAI(api_key=api_key)
        self.api_key = api_key

    def generate_text(
        self,
        task_id: str=None,
        system_persona: str=None,
        prompt: str=None,
        image_url: str=None,
        messages: List[dict] = None,
    ):
        if messages is None:
            messages = [
                {"role": "user", "content": [
                    {"type": "text",
                     "text": prompt
                     },
                    {
                      "type": "image_url",
                      "image_url": {
                        "url": f"data:image/jpeg;base64,{image_url}",
                      },
                    },
                    ]
                 },
            ]

        response = self.client.chat.completions.create(
                **self.parameters,
                model="gpt-4o",
                messages=messages,
                )

        return response.choices[0].message.content

    def generate_image(
        self, task_id: str, prompt: str, resource_box: ResourceBox
    ) -> FileResponse:
        pass