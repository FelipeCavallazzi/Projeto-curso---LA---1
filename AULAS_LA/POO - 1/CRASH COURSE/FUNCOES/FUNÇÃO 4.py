# Argument opcional

def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()

filho = get_formatted_name("felipe", "cavallazzi", "de moraes")
print(filho)

pai = get_formatted_name("marcelo", "cavallazzi")
print (pai)