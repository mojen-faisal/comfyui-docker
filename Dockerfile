FROM python:3.11-slim

ENV COMFYUI_PATH=/root/comfy/ComfyUI \
  COMFYUI_MODEL_PATH=/root/comfy/ComfyUI/models

RUN apt-get update && apt-get install -y \
  git \
  wget \
  python3-opencv \
  curl && \
  rm -rf /var/lib/apt/lists/*

RUN pip install comfy-cli opencv-python

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN comfy --skip-prompt install --nvidia

COPY install_custom_nodes.py /root/install_custom_nodes.py
COPY download_models.py /root/download_models.py
COPY setup_ollama.py /root/setup_ollama.py

ARG OLLAMA_MODELS="phi3:latest,llava:34b,llama3.1:latest"

RUN python3 /root/install_custom_nodes.py
RUN python3 /root/download_models.py
RUN python3 /root/setup_ollama.py --models $OLLAMA_MODELS

ENTRYPOINT ["comfy", "launch", "--", "--listen", "0.0.0.0"]
