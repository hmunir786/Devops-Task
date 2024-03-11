import requests
import hashlib
import os

def parse_data():
    # Get data from the endpoint
    response = requests.get("http://web:5000/data")
    data = response.json()["samples"]

    # Create files directory if it doesn't exist
    if not os.path.exists("files"):
        os.makedirs("files")

    # Parse data and create files
    for sample in data:
        name = sample["name"]
        id_ = sample["id"]
        file_path = f"files/{id_}.txt"
        
        # Write name to file
        with open(file_path, "w") as file:
            file.write(name)

        # Calculate and verify SHA256 sum
        with open(file_path, "rb") as file:
            file_contents = file.read()
            file_hash = hashlib.sha256(file_contents).hexdigest()

        if file_hash == id_:
            print(f"File {file_path} created successfully.")
        else:
            print(f"File {file_path} creation failed. Hash mismatch.")

if __name__ == "__main__":
    parse_data()
