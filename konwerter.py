import argparse
import json
import yaml
import os
import xmltodict


def convert_files(input_file, output_file, output_format):
    if not os.path.isfile(input_file):
        print(f"Plik wejściowy '{input_file}' nie istnieje.")
        return

    input_file_extension = input_file.split('.')[-1].lower()

    # Wczytywanie danych
    with open(input_file, 'r') as file:
        if input_file_extension == 'json':
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                print('Niepoprawny format pliku JSON.', str(e))
                return

        elif input_file_extension == 'yaml':
            try:
                data = yaml.safe_load(file)
            except yaml.YAMLError as e:
                print('Niepoprawny format pliku YAML.', str(e))
                return

        elif input_file_extension == 'xml':
            try:
                data = xmltodict.parse(file.read())
            except xmltodict.expat.ExpatError as e:
                print('Niepoprawny format pliku XML.', str(e))
                return
        else:
            print('Niepoprawny format pliku wejściowego. Dostępne formaty: xml, json, yaml.')
            return

    # Funkcje zapisywania danych do nowego formatu
    def json_to_yaml():
        with open(output_file, 'w') as file:
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

    def yaml_to_json():
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def json_to_xml():
        with open(output_file, 'w') as file:
            xml_data = xmltodict.unparse({"root": data}, pretty=True)
            file.write(xml_data)

    def yaml_to_xml():
        with open(output_file, 'w') as file:
            xml_data = xmltodict.unparse({"root": data}, pretty=True)
            file.write(xml_data)

    def xml_to_json():
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        with open(output_file, "w") as json_file:
            json_file.write(json_data)

    def xml_to_yaml():
        yaml_data = yaml.dump(data, default_flow_style=False, allow_unicode=True)
        with open(output_file, "w") as yaml_file:
            yaml_file.write(yaml_data)

    # Wywoływanie funkcji
    if input_file_extension == output_format:
        print("Format pliku wejściowego i wyjściowego jest taki sam! Plik nie został utworzony.")
        return

    elif input_file_extension == 'json':
        if output_format == 'yaml':
            print("Konwertowanie pliku JSON na YAML...")
            json_to_yaml()

        elif output_format == 'xml':
            print("Konwertowanie pliku JSON na XML...")
            json_to_xml()

    elif input_file_extension == 'yaml':
        if output_format == 'json':
            print("Konwertowanie pliku YAML na JSON...")
            yaml_to_json()

        elif output_format == 'xml':
            print("Konwertowanie pliku YAML na XML...")
            yaml_to_xml()

    elif input_file_extension == 'xml':
        if output_format == 'json':
            print("Konwertowanie pliku XML na JSON...")
            xml_to_json()

        elif output_format == 'yaml':
            print("Konwertowanie pliku XML na YAML...")
            xml_to_yaml()


