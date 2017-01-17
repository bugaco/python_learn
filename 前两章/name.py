name = "ada lovelace"
print(name)
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)
print("\t" + message)
print("\n" + message)

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = '   python  '
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)