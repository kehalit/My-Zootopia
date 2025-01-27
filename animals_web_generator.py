import json
import webbrowser

with open('animals_data.json', 'r') as file:
    animals_data = json.load(file)
with open("animals_template.html", "r") as file_2:
    html_data = file_2.read()


output= ""

# Iterate through the animals and print the requested details
for animal in animals_data:
    output += '<li class="cards__item">'
    output += f' <div class="card__title">{animal["name"]}</div>\n'
    output += f'<p class="card__text">'
    output += f"<strong>Diet: </strong> {animal['characteristics']['diet']}<br/>\n"
    output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
    if 'type' in animal.get('characteristics', {}):
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
    output += "\n"
html_output = html_data.replace("__REPLACE_ANIMALS_INFO__", output)
print(html_output)

with open("animals.html", "w") as file_3:
    file_3.write(html_output)
