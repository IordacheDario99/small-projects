#get user email adress
email = input("Enter email adress: ").strip()
#slice out user name
email_name = email[:email.index("@")]
#slice out domain name
email_domain= email[email.index("@")+1:]
#format message
output = "User name: {}\nDomain name: {}".format(email_name,email_domain)
#display output message
print(output)