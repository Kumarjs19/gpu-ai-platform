FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y python3-pip git

WORKDIR /app

COPY . .

RUN pip3 install torch torchvision torchaudio transformers diffusers accelerate safetensors pillow redis

CMD ["python3", "app/worker.py"]
