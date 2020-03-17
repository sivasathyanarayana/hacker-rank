def fun(s):
    # return True if s is a valid email, else return False
    try:
        username,url=s.split("@")
        website,extension=url.split(".")
    except:
        return False

    if not username.replace("_","").replace("-","").isalnum():
        return False
    if not website.isalnum():
        return False
    if (len(extension)>3):
        return False
    return True
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
