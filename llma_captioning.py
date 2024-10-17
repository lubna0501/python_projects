from huggingface_hub import hf_hub_download
from llama_cpp import Llama

class LLMaCaptioning:
    def __init__(self):
        self.model_name_or_path = "TheBloke/Llama-2-13B-chat-GGML"
        self.model_basename = "llama-2-13b-chat.ggmlv3.q5_1.bin"
        self.model_path = hf_hub_download(repo_id=self.model_name_or_path, filename=self.model_basename)
        print("Loading model...")
        self.lcpp_llm = Llama(
            model_path=self.model_path,
            n_threads=2,  # CPU cores
            n_batch=512,  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
            n_gpu_layers=32  # Change this value based on your model and your GPU VRAM pool.
        )
        print("Model loaded!")

    def generate_caption(self, prompt):
        prompt_template = f'''SYSTEM: You are a super caption creator using description of image provided by user. You write 5 creative and trending captions.

USER: {prompt}

ASSISTANT:
'''     
        print("Getting response")
        response = self.lcpp_llm(prompt=prompt_template, max_tokens=256, temperature=0.5, top_p=0.95,
                                 repeat_penalty=1.2, top_k=150,
                                 echo=True)
        return response["choices"][0]["text"]

# Example usage
llma_captioner = LLMaCaptioning()
prompt = "An awesome girl with long hair and blue eyes."
print("Generating Caption...")
caption = llma_captioner.generate_caption(prompt)
print("LLMa Caption:", caption)
