import requests

API_ENDPOINT = "https://6ade9a514e88f1bba4a535f6.mockapi.io/books"


def get_books():
    print("\n=== GET ALL BOOKS ===")

    try:
        response = requests.get(API_ENDPOINT)
        response.raise_for_status()

        print("Status Code:", response.status_code)
        print(response.json())

    except requests.exceptions.HTTPError as error:
        print("GET ERROR:", error)


def add_book(book):
    print("\n=== ADD BOOK ===")

    try:
        response = requests.post(API_ENDPOINT, json=book)
        response.raise_for_status()

        print("Status Code:", response.status_code)
        print(response.json())

        return response.json()["id"]

    except requests.exceptions.HTTPError as error:
        print("POST ERROR:", error)

    return None


def update_book(book_id, book):
    print("\n=== UPDATE BOOK ===")

    try:
        response = requests.put(
            f"{API_ENDPOINT}/{book_id}",
            json=book
        )

        response.raise_for_status()

        print("Status Code:", response.status_code)
        print(response.json())

    except requests.exceptions.HTTPError as error:
        print("PUT ERROR:", error)


def delete_book(book_id):
    print("\n=== DELETE BOOK ===")

    try:
        response = requests.delete(
            f"{API_ENDPOINT}/{book_id}"
        )

        response.raise_for_status()

        print("Status Code:", response.status_code)
        print(response.json())

    except requests.exceptions.HTTPError as error:
        print("DELETE ERROR:", error)


def confirm_delete(book_id):
    print("\n=== CONFIRM DELETE ===")

    try:
        response = requests.get(
            f"{API_ENDPOINT}/{book_id}"
        )

        response.raise_for_status()

        print(response.json())

    except requests.exceptions.HTTPError as error:
        print("Expected HTTP Error:", error)


# GET
get_books()

# POST
new_book = {
    "title": "Clean Code",
    "author": "Robert Martin",
    "rating": "10"
}

book_id = add_book(new_book)

# PUT
if book_id:
    updated_book = {
        "title": "Clean Code Second Edition",
        "author": "Robert Martin",
        "rating": "9"
    }

    update_book(book_id, updated_book)

    # DELETE
    delete_book(book_id)

    # Confirm deletion
    confirm_delete(book_id)

# Final GET
get_books()

print("\nBookstore API Activity Completed Successfully.")
