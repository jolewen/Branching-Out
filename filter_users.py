import json
from functools import wraps


def read_json(json_path: str) -> list[dict]:
    """Reads user data from a .json file."""
    with open(json_path, "r") as file:
        users = json.load(file)
    return users


def print_users(filtered_users: list):
    """Prints out the filtered users."""
    for user in filtered_users:
        print(user)


def load_and_print(func):
    """Decorator that loads user data from a .json file,
    applies a filtering function, and prints the filtered results.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        users = read_json("users.json")
        filtered_users = func(users, *args, **kwargs)
        print_users(filtered_users)

    return wrapper


@load_and_print
def filter_users_by_name(users: list, name: str) -> list:
    """Filters to keep only users with matching names."""
    return [user for user in users if user["name"].lower() == name.lower()]


@load_and_print
def filter_by_age(users: list, age: int) -> list:
    """Filters to keep only users who are exactly 'age' years old."""
    return [user for user in users if user["age"] == age]


@load_and_print
def filter_by_email(users: list, email_to_search: str):
    """Filters to keep only users with 'email_to_search' email information.
    Allows for part searches.
    """
    return [user for user in users if email_to_search.lower() in user["email"]]


def main():
    filter_option = input("What would you like to filter by? "
                          "(Currently, 'name', 'age' & 'email' are supported): ").strip().lower()
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_str = input("Enter an age: ").strip()
        try:
            age = int(age_str)
        except ValueError:
            print(f"Invalid age '{age_str}'.")
            raise ValueError
        filter_by_age(age)
    elif filter_option == "email":
        email_to_search = input("Enter a (part of) an email to filter users: ").strip()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
