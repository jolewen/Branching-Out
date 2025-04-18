import json


def read_json(json_path):
    with open(json_path, "r") as file:
        users = json.load(file)
    return users


def print_users(filtered_users):
    for user in filtered_users:
        print(user)


def filter_users_by_name(name):
    users = read_json("users.json")
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    print_users(filtered_users)


def filter_by_age(age: int):
    users = read_json("users.json")
    filtered_users = [user for user in users if user["age"] == age]
    print_users(filtered_users)


def main():
    filter_option = input("What would you like to filter by? "
                          "(Currently, only 'name' and 'age' are supported): ").strip().lower()
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_str = input("Enter an age: ").strip()
        age = int(age_str)
        filter_by_age(age)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
