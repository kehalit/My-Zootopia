import json

with open('animals_data.json', 'r') as file:
    animals_data = json.load(file)

# Iterate through the animals and print the requested details
for animal in animals_data:
    if 'name' in animal:
        print(f"Name: {animal['name']}")

    # Access the characteristics for diet and type
    characteristics = animal.get('characteristics', {})
    if 'diet' in characteristics:
        print(f"Diet: {characteristics['diet']}")
    if 'locations' in animal and animal['locations']:
        print(f"Location: {animal['locations'][0]}")
    if 'type' in characteristics:
        print(f"Type: {characteristics['type']}")

    # Add a blank line between animals for readability
    print()
