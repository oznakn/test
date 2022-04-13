import uuid

print("Hello, world!")

open(f"{str(uuid.uuid4())}.txt", "w").close()
