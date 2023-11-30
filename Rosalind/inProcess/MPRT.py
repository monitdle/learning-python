import requests

url = "https://rest.uniprot.org/uniprotkb/A2Z669.fasta"

response = requests.get(url)

if response.status_code == 200:
    with open("A2Z669.fasta", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")


# Open the downloaded FASTA file
file_path = "A2Z669.fasta"
with open(file_path, "r") as file:
    # Read the file line by line
    for line in file:
        # Check if the line contains the target string "AQP"
        if "AQP" in line:
            print("Found 'AQP' in line:", line.strip())
