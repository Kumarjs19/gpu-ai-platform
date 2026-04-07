from fastapi import APIRouter, Header
import uuid, json, redis, os

router = APIRouter()

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

@router.post("/generate")
def generate(data: dict, authorization: str = Header(None)):
    job_id = str(uuid.uuid4())

    job = {
        "id": job_id,
        "type": data["type"],
        "prompt": data["prompt"],
        "status": "queued"
    }

    r.lpush("job_queue", json.dumps(job))

    return {"job_id": job_id, "status": "queued"}
