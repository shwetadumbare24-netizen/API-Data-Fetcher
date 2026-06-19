import requests
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    if response.status_code == 200:

        users = response.json()
        print("\nAll Users:\n")

        for user in users:
            print(f"ID: {user['id']}")
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print("-" * 30)

        search = input("\nEnter user name to search: ").lower()

        print("\nSearch Results:\n")

        found = False

        for user in users:
            if search in user["name"].lower():
                print(f"ID: {user['id']}")
                print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print("-" * 30)
                found = True
        if not found:
            print("No user found.")

    else:
        print("Failed to fetch data.")

except Exception as e:
    print("Error:", e)