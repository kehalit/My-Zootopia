import json
import webbrowser

with open('animals_data.json', 'r') as file:
    animals_data = json.load(file)
with open("animals_template.html", "r") as file_2:
    html_data = file_2.read()


output= ""

# Iterate through the animals and print the requested details
for animal in animals_data:
    output += f"Name: {animal['name']}\n"
    output += f"Diet: {animal['characteristics']['diet']}\n"
    output += f"Location: {animal['locations'][0]}\n"
    if 'type' in animal.get('characteristics', {}):
        output += f"Type: {animal['characteristics']['type']}\n"
    output += "\n"
html_output = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
print(html_output)

with open("animals.html", "w") as file_3:
    file_3.write(html_output)
