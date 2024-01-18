from ..abc import NamedModel, Message, MissingDependencyError

try:
    from transformers import AutoModelForCausalLM, AutoTokenizer
    import torch
except ImportError as err:
    raise MissingDependencyError("Please install transformers library") from err


class HFModel(NamedModel):
    def __init__(self, hf_name: str, device: str | None = None):
        self.name = "hf:" + hf_name
        if device is None:
            device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.__model = AutoModelForCausalLM.from_pretrained(hf_name).to(device).eval()
        self.__tokenizer = AutoTokenizer.from_pretrained(hf_name, use_fast=False)

        super().__init__("hf:" + hf_name, self.__predict)

    def __predict(self, messages: list[Message]) -> str:
        prompt = self.__tokenizer.apply_chat_template([x.to_json_obj() for x in messages])
        inputs = self.__tokenizer(prompt, return_tensors="pt").to(self.__model.device)
        prompt_tokens = inputs["input_ids"].shape[1]

        with torch.no_grad():
            outputs = self.__model.generate(**inputs)

        response = outputs[0][prompt_tokens:]
        return self.__tokenizer.decode(response, skip_special_tokens=True)
