import os


def extract_place(filename):
    return filename.split("_")[1]


def make_place_directories(filelist):
    for file in filelist:
        os.mkdir(file)


def move_directories(filelist):
    for file in filelist:
        os.rename(file, os.path.join(extract_place(file), file))


def organize_photos(directory):
    os.chdir("Photos")
    originals = os.listdir()
    places = []
    for file in originals:
        place = extract_place(file)
        if place not in places:
            places.append(place)

    make_place_directories(places)
    move_directories(originals)


organize_photos("Photos")
# Print out the list, just to be sure you're getting the results you expect:
