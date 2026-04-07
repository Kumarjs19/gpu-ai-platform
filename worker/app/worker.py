import redis
import json
import os

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

print("Worker started")

while True:
    _, job = r.blpop("job_queue")
    data = json.loads(job)
    print("Processing:", data)
