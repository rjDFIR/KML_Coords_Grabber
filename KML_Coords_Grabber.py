import argparse
def main_func():
    parser = argparse.ArgumentParser(
        description="Scrapes all coordinate values from a KML file."
    )

    parser.add_argument(
        "-k", "--kml", metavar="{path_to_kml}",
        required=True, help="The path of the input KML file"
    )

    args = parser.parse_args()
    #print({args.kml})

    print("\n\nCoordinates from this file:")
    print("===============================")
    add_line_string(args.kml)


def add_line_string(input_file):
    #coords_list = []  <-- unused at the moment; functionality could be added to create
    #the full lineString within this script at a later time

    input_kml = input_file
    print("[File Path: " + "\"" + input_kml + "\"" + "]")

    with open(input_kml, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if line.__contains__('<coordinates>'):
                grab_coords(line)


def grab_coords(current_line):
    line = current_line
    line = line.split('<coordinates>')
    line[1] = line[1].replace('</coordinates></Point>', '')
    print(line[1])


main_func()
