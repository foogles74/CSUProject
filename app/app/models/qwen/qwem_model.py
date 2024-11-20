from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class QwenModel:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(QwenModel, cls).__new__(cls)
            torch.set_default_device('cuda')
            model_name = "Qwen/Qwen2.5-3B-Instruct"
            cls._instance.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype="auto",
                device_map='cuda'
            )
            cls._instance.tokenizer = AutoTokenizer.from_pretrained(model_name)
        return cls._instance

    def generate_text(self,prompt):
        text = self.tokenizer.apply_chat_template(
            prompt,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=512
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return  response