"""
Mock API Exercise: Music Album

1. Create an "Album" resource on mockapi.io ("id", "name", "rate").
2. Paste its URL into API_ENDPOINT below.
3. Study the finished GET section.
4. Fill in the POST, PUT, DELETE TODOs.
"""

import requests

# Replace with your MockAPI endpoint
API_ENDPOINT = "https://6ade8d494e88f1bba4a531b9.mockapi.io/songs"

# ============================================================
# 1. GET METHOD
# ============================================================

print("\n=== GET ALL SONGS ===")

try:
    getAllSongs = requests.get(API_ENDPOINT)
    getAllSongs.raise_for_status()

    print("Status Code:", getAllSongs.status_code)
    print("Songs:", getAllSongs.json())

except requests.exceptions.HTTPError as httperror:
    print("HTTP GET ERROR:", httperror)

# ============================================================
# 2. POST METHOD
# ============================================================

print("\n=== CREATE NEW SONG ===")

newSong = {
    "name": "Believer",
    "rate": "8"
}

created_song_id = None

try:
    responseOfNewSong = requests.post(
        API_ENDPOINT,
        json=newSong
    )

    print("Status Code:", responseOfNewSong.status_code)
    responseOfNewSong.raise_for_status()

    created_song = responseOfNewSong.json()
    created_song_id = created_song["id"]

    print("Created Song:")
    print(created_song)

except requests.exceptions.HTTPError as httperror:
    print("HTTP POST ERROR:", httperror)

# ============================================================
# 3. PUT METHOD
# ============================================================

print("\n=== UPDATE SONG ===")

if created_song_id:

    updatedSong = {
        "name": "Believer Updated",
        "rate": "10"
    }

    try:
        responseOfReplacement = requests.put(
            f"{API_ENDPOINT}/{created_song_id}",
            json=updatedSong
        )

        print("Status Code:", responseOfReplacement.status_code)
        responseOfReplacement.raise_for_status()

        print("Updated Song:")
        print(responseOfReplacement.json())

    except requests.exceptions.HTTPError as httperror:
        print("HTTP PUT ERROR:", httperror)

# ============================================================
# 4. DELETE METHOD
# ============================================================

print("\n=== DELETE SONG ===")

if created_song_id:

    try:
        deleteSong = requests.delete(
            f"{API_ENDPOINT}/{created_song_id}"
        )

        print("Status Code:", deleteSong.status_code)
        deleteSong.raise_for_status()

        print("Deleted Song:")
        print(deleteSong.json())

    except requests.exceptions.HTTPError as httperror:
        print("HTTP DELETE ERROR:", httperror)

# ============================================================
# FINAL GET
# ============================================================

print("\n=== FINAL SONG LIST ===")

try:
    finalSongs = requests.get(API_ENDPOINT)
    finalSongs.raise_for_status()

    print("Status Code:", finalSongs.status_code)
    print(finalSongs.json())

except requests.exceptions.HTTPError as httperror:
    print("HTTP FINAL GET ERROR:", httperror)

print("\nActivity completed successfully.")
