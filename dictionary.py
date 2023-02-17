# profile = {}
# profile["user_name"] = "user123"
# profile["age"] = 20
# profile["email"] = "user123@gmail.com"


# print (profile)


profile ={}

def register():
    #ask for username
    #ask for email
    #ask for passward
    #store in dictionary
    name = input("Enter usernamae:")
    email = input("Enter email:")
    password = input("Enter password")

    profile["usename"]= name
    profile["email"]= email
    profile["password"]= password

    
def get_profile():
    print(profile)
    get_profile()


def change_username():
    new_username = input("user_name")
    profile["user_name"] = new_username

register()
get_profile()    