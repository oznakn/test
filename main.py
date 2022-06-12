import uuid
import time

print("Hello, world!")

for i in range(4):
    print("State:", i)
    time.sleep(1)

# open(f"{str(uuid.uuid4())}.txt", "w").close()
