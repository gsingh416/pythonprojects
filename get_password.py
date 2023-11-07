# get_pass.py

# import getpass module
import getpass

# request user to input a password
passwd = getpass.getpass('Password:')

# validate the password entered by the user against the given password
if passwd == "password":
  print("authentication successful")
else:
  print("authentication failed ")
