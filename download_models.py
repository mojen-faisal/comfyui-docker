import os
import subprocess
from urllib.parse import urlparse, parse_qs, urlencode
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

MODELS = [
    {
    "name": "florence2-large-PromptGen-v1_5.safetensors",
    "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/model.safetensors",
    "path": "models/florence2/large-PromptGen-v1.5"
    },
    {
      "name": "added_tokens.json",
      "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/added_tokens.json",
      "path": "models/florence2/large-PromptGen-v1.5"
    },
    {
      "name": "config.json",
      "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/config.json",
      "path": "models/florence2/large-PromptGen-v1.5"
    },
    {
      "name": "generation_config.json",
      "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/generation_config.json",
      "path": "models/florence2/large-PromptGen-v1.5"
    },
    {
      "name": "merges.txt",
      "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/merges.txt",
      "path": "models/florence2/large-PromptGen-v1.5"
    },
    {
      "name": "preprocessor_config.json",
      "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/preprocessor_config.json",
      "path": "models/florence2/large-PromptGen-v1.5"
    },
    {
      "name": "special_tokens_map.json",
      "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/special_tokens_map.json",
      "path": "models/florence2/large-PromptGen-v1.5"
    },
    {
      "name": "tokenizer.json",
      "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/tokenizer.json",
      "path": "models/florence2/large-PromptGen-v1.5"
    },
    {
      "name": "tokenizer_config.json",
      "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/tokenizer_config.json",
      "path": "models/florence2/large-PromptGen-v1.5"
    },
    {
      "name": "vocab.json",
      "url": "https://huggingface.co/MiaoshouAI/Florence-2-large-PromptGen-v1.5/resolve/main/vocab.json",
      "path": "models/florence2/large-PromptGen-v1.5"
    },
]

def download_file(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
   
    print(f"Downloading from URL: {url}")
    subprocess.run(["wget", "-O", path, url], check=True)

def download_models(models):
    tasks = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for model in models:
            path = Path(f"/root/comfy/ComfyUI/{model['path']}/{model['name']}")
            if not path.exists():
                tasks.append(executor.submit(download_file, model['url'], str(path)))

        for future in as_completed(tasks):
            try:
                future.result()
            except Exception as exc:
                print(f"Generated an exception: {exc}")

if __name__ == "__main__":
  download_models(MODELS)