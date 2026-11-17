# 13. Secure Login System (Decorators)
# A web application wants to ensure that users are authenticated before accessing
# sensitive functions. Create a decorator that checks whether the user is logged in before
# allowing access to a function.

# Explanation:
# - A decorator adds extra functionality to a function.
# - @login_required applies the decorator.
# - The wrapper checks the login status before executing the function.

# Create decorator
def login_required(func):

    def wrapper(is_logged_in):

        # Check login status
        if is_logged_in:
            return func()
        else:
            print("Please Login First")

    return wrapper


# Apply decorator
@login_required
def dashboard():
    print("Welcome to Dashboard")


# Call function
dashboard(True)

# Call without login
dashboard(False)