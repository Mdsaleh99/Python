import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    # print(response)   
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"] # sirf user ka data holder karre hai and no extra message, statusCode, success only user data
        username = user_data["login"]["username"] # user_data k andar login property hai uske andar username property hai
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username, country = fectch_random_user_freeapi()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()



# print(__name__)  # Will print "__main__" if run directly, else module name
# print(globals())  # This will display a dictionary of all global variables, including __name__
# print(dir())  # Lists all variables and functions in the current scope
"""
print(f"__name__: {__name__}")
print(f"__file__: {__file__}")  # Only works in scripts, not in interactive mode
print(f"__doc__: {__doc__}")  # Shows module docstring if available
"""