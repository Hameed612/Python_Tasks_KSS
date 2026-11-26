# 8. Decorator-based Access Control

# Scenario:
# Restrict access to certain functions.

# Task:
# ● Create a decorator to check user role
# ● Use condition inside decorator
# ● Apply decorator to multiple functions
# ● Store roles in a dictionary


# Decorator-based Access Control

# Store user roles
users = {
    "Rahul": "admin",
    "Anita": "user"
}

# Create decorator
def check_role(function):

    def wrapper(name):

        # Check user role
        if users.get(name) == "admin":
            print("Access Granted")
            function(name)

        else:
            print("Access Denied")

    return wrapper


# Apply decorator
@check_role
def delete_data(name):
    print(name, "can delete data")


@check_role
def update_data(name):
    print(name, "can update data")


# Call functions
delete_data("Rahul")

update_data("Anita")

delete_data("Anita")
