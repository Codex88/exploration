# generate a histogram from file using dictionaries and .get()

# get input from end-user
filename = input("Enter a filepath: ")

# failsafe for bad end-user input
try:
    filehandle = open(filename, encoding="utf-8")
except:
    print("Bad filepath. Cannot open file.")

# declare final dinctionaries
email_addresses = dict()
email_usernames = dict()
email_domains = dict()
email_names = dict()

# declare "get" lists for dictonaries
emails = list()
usernames = list()
domains = list()
names = list()

# extract email addresses from file
for line in filehandle:
    line = line.rstrip("\n")
    if line.startswith("From:"):
        linelist = line.split(" ")
        emails.append(linelist[1])
    else:
        continue

# commit email addresses to dictionary
for email in emails:
    email_addresses[email] = email_addresses.get(email, 0) + 1

# generate username and domain lists
for email in emails:
    emaillist = email.split("@")
    usernames.append(emaillist[0])
    domains.append(emaillist[1])

# commit users to dictionary
for user in usernames:
    email_usernames[user] = email_usernames.get(user, 0) + 1

# commit domains to dictonary
for domain in domains:
    email_domains[domain] = email_domains.get(domain, 0) + 1

# generate names from usernames
for user in usernames:
    if "." in user:
        userlist = user.split(".")
        names.append(userlist[0])
        names.append(userlist[1])
    else:
        names.append(user)

# commit names to dictonary
for name in names:
    email_names[name] = email_names.get(name, 0) + 1

# print dictionaries
print("\nEmail Address Count:\n", email_addresses)
print("\nEmail Username Count:\n", email_usernames)
print("\nEmail Domain Count:\n", email_domains)
print("\nEmail Name Count:\n", email_names)
