name = "Ephraim Aondofa"
print(name.title())
print(name.upper())
print(name.lower())
first_name = "Lovelace"
last_name = "Ada" 
full_name = first_name + " " + last_name + "."
print(full_name)
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name +  " " + last_name
print("Hello, " + full_name.title() + "!") 
message = "Hello, " + full_name.title() + "!"
print(message)

#to addd tab
print("python")
print("\tpython")

#to add newline
print("languages:\nPython\nC\nJavascript")
print("languages:\n\tPython\n\tC\n\tJavaScript")

#to remove whitespace
favourite_language = 'Python '
print(favourite_language)
favourite_language.rstrip()
print(favourite_language.rstrip())

#to remove the whitespace permanently
favourite_language = 'Python '
favourite_language = favourite_language.rstrip()
print(favourite_language)

#to remove whitespace from both sides
favourite_language = ' python '
print(favourite_language.rstrip())
print(favourite_language.lstrip())
print(favourite_language.strip())