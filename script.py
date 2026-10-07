import os

path_base =  "componentes_electronicos"
img_path = "images"
labels_path = "labels"



def generate_list(name_file, path_dir):
    content = ""
    for img_name in (os.listdir(path_dir)):
        content += img_name+"\n"

    with open(name_file, mode="w+", encoding="utf-8") as img_file:
        img_file.write(content)
        print(f"File written {name_file}")


def main():
    generate_list("images.txt", os.path.join(path_base, img_path))
    generate_list("labels.txt", os.path.join(path_base, labels_path))


main()