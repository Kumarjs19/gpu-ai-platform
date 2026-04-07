# 🚀 Deployment Guide (RunPod + AWS)

## 🔹 Option 1: RunPod (Recommended for GPU resale)

### Step 1: Create Pod
- Go to https://runpod.io
- Select GPU (24GB+ recommended)
- Choose Docker image: `runpod/pytorch:2.0.1-py3.10-cuda11.8`

### Step 2: Deploy Worker
```bash
git clone https://github.com/Kumarjs19/gpu-ai-platform.git
cd gpu-ai-platform

docker build -t gpu-worker ./worker

docker run --gpus all -e REDIS_HOST=<your-redis-ip> gpu-worker
```

### Step 3: Use Managed Redis
- Use Upstash / Redis Cloud

---

## 🔹 Option 2: AWS Deployment

### Services:
- EC2 (GPU instance)
- RDS (PostgreSQL)
- ElastiCache (Redis)
- S3 (storage)

### Steps:
1. Launch EC2 GPU (g5.xlarge)
2. Install Docker + NVIDIA runtime
3. Clone repo
4. Run:
```bash
docker-compose up --build
```

---

## 🔥 Production Tips
- Use NGINX as reverse proxy
- Add domain (Route53)
- Enable HTTPS (Let's Encrypt)
- Use autoscaling for workers

---

## 💰 Cost Optimization
- RunPod: cheapest for GPU resale
- AWS: better for enterprise scaling

---

## 🚀 Final Setup
UI → API (AWS) → Redis → GPU Workers (RunPod)

Hybrid = Best ROI 💰
