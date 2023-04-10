first_name = "ada"
last_name = "lovelace"

print(f"{first_name} {last_name}".title())

full_name = f"{first_name} {last_name}".title()

print(f"Hello, {full_name}!")

full_name = "{} {}".format(first_name, last_name).title()

print("New full_name " + full_name)