# Mendeley API Integration
This project provides a Python-based integration with the Mendeley API, allowing you to interact with Mendeley collections, documents, and files. It includes functionality to list collections, list documents, check for attached files, and download files to a local directory.

## Features
- OAuth2 Authentication: Authenticate with the Mendeley API using OAuth2.
- List Collections: Retrieve all collections (folders) in your Mendeley account.
- List Documents: Retrieve all documents in your Mendeley library or a specific collection.
- Check Files: Check if documents have files attached.
- Download Files: Download attached files to a local directory.
- Export Data: Export collections and document data to JSON files.

## Prerequisites
1. Python: Ensure you have Python 3.7 or later installed.
2. Mendeley Developer Account: Register an application on the [Mendeley Developer Portal](https://dev.mendeley.com/) to obtain your `CLIENT_ID` and `CLIENT_SECRET`.
3. Dependencies: Install the required Python libraries.

### Setup
1. Clone the Repository

```sh
git clone https://github.com/PatrickCmd/Mendeley-API-integration.git
cd Mendeley-API-integration
```

2. Install Dependencies
Install the required Python libraries:

```sh
pip install -r requirements.txt
```

3. Create a `.env` File
Create a `.env` file in the root directory and add the following:

```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://localhost:8000/callback
```

Replace `your_client_id`, `your_client_secret`, and `http://localhost:8000/callback` with your actual values.


4 Run the Script
Run the script to start interacting with the Mendeley API:

```sh
python mendeley_manager.py
```

### Usage
1. Authenticate with Mendeley
When you run the script, it will generate an authorization URL. Open the URL in your browser, log in to Mendeley, and authorize the application. Copy the access token provided and paste it into the terminal when prompted.

2. List Documents and Collections
The script will list all documents and collections in your Mendeley account. It will also export this data to `documents.json` and `collections.json`.

3. Select a Collection
The script will display all available collections. Select a collection by entering its corresponding number.

4. List Documents and Files in a Collection
The script will list all documents and their attached files in the selected collection. It will also export this data to a JSON file named after the collection (e.g., `research-papers-2025_data.json`).

5. Download Files
The script will download all attached files to a local directory named [mendeley_data](./mendeley_data).


## Example Workflow
1. Run the Script:

```sh
python mendeley_manager.py
```

2. Authenticate with Mendeley:

Authorization URL: The script will generate an authorization URL:

```
Authorization URL: https://api.mendeley.com/oauth/authorize?client_id=20311&redirect_uri=http://localhost:8000/callback&response_type=code&scope=all
```

Paste the `Authorization URL` into the browser to complete the authorization and obtain the access token.

```json
{
  "access_token": "MSwxNzQ2NDI0Mzk3MTgwLDc5Mzk5MDg4MSwyMDMxMSxhbGwsLCxlZTkxOGYxNTQ1MzMyNzQxYjU5ODk3NzdmNzI4ZDZmMDdjMmNneHJxYSxiMGY5ODg4Yy03ZjgyLTMzZTQtYTJmMC02NTYwYTMxNjVkZjMsOGxmWTFfazlWdHp6djN5RlY1XXY9vQXMtN0pK"
}
```

3. Access Token: After authorizing the app, copy the access token and paste it into the terminal:

```
Enter the authorization access token: <your_access_token>
```

4. List Collections:

List Collections: The script will list all collections:

```
Available collections:
1. Research Papers (ID: 12345)
2. Thesis References (ID: 67890)
```

5. Select a Collection:

Select a Collection: Enter the number of the collection to list its documents and files:

```
Enter the number of the collection to list documents and files: 1
```

5. Export Data: The script will export the collection data to a JSON file:

```
Collection data exported to research-papers-2025_data.json
```

6. List Documents and Files:

List Documents and Files: The script will list all documents and their attached files:

7. Download Files: The script will download all attached files to the mendeley_data folder:

```
Downloading file: example_paper_1.pdf
Downloading file: example_paper_2.pdf
Downloaded files: ['mendeley_data/example_paper_1.pdf', 'mendeley_data/example_paper_2.pdf']
```

### Using in an Application
You can integrate the [MendeleyManager](./mendeley_manager.py) class into your own application. Here's an example:

```python
from mendeley_manager import MendeleyManager

# Initialize the manager
manager = MendeleyManager(client_id="your_client_id", client_secret="your_client_secret", redirect_uri="http://localhost:8000/callback")

# Get the authorization URL
auth_url = manager.get_auth_url()
print("Authorization URL:", auth_url)

# Exchange the authorization access token
access_token = input("Enter the authorization access token: ")

# List collections
collections = manager.list_collections(access_token)
print("Collections:", collections)

# List documents in a collection
collection_id = "your_collection_id"
documents = manager.list_documents_and_files_in_collection(access_token, collection_id)
print("Documents in collection:", documents)
```

### Notes
- Ensure your `REDIRECT_URI` matches the one registered in your Mendeley app settings.
- Handle exceptions and errors (e.g., invalid tokens, rate limits) in production code.
- Use the slugify library to create URL- and file-system-friendly names for collections.

