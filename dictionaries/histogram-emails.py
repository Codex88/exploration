# histogram counting names from file

filename = "../sample-files/mbox.txt"

filehandle = open(filename, encoding="utf-8")

email_addresses = dict()
email_usernames = dict()
email_domains = dict()
names = dict()

for line in filehandle:
    line = line.rstrip('\n')
    if line.startswith("From:"):
        linelist = line.split(" ")
        emailaddress = linelist[1]
        if emailaddress not in email_addresses:
            email_addresses[emailaddress] = 1
        else:
            email_addresses[emailaddress] += 1
        emaillist = emailaddress.split("@")
        user = emaillist[0]
        if user not in email_usernames:
            email_usernames[user] = 1
        else:
            email_usernames[user] += 1
        if "." in user:
            userlist = user.split(".")
            name1 = userlist[0]
            name2 = userlist[1]
            if name1 not in names:
                names[name1] = 1
            else:
                names[name1] += 1
            if name2 not in names:
                names[name2] = 1
            else:
                names[name2] += 1
        elif "." not in user:
            if user not in names:
                names[user] = 1
            else:
                names[user] += 1
        else:
            continue
        domain = emaillist[1]
        if domain not in email_domains:
            email_domains[domain] = 1
        else:
            email_domains[domain] += 1
    else:
        continue


print("\nEmail addresses:\n", email_addresses)
print("\nEmail usernames:\n", email_usernames)
print("\nEmail domains:\n", email_domains)
print("\nNames:\n", names)
