str1 = "alcantara@gmail.com"
str2 = "gmail.com"
str3 = "pepsicola.com"

def replace_domain(email, old_domain, new_domain):
	if "@" + old_domain in email:
		index = email.index("@" + old_domain)
		new_email = email[:index] + "@" + new_domain
		return new_email

	return email

print(replace_domain(str1,str2,str3))