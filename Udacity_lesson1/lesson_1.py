import os

def rename_files():
    file_list = []
    for f in os.listdir(r"/Users/vinicius.marinho/Udacity/prank"):
        if not f.startswith("."):
            file_list.append(f)


    path = os.getcwd()

    os.chdir("/Users/vinicius.marinho/Udacity/prank")

    tabela = str.maketrans(dict.fromkeys("0123456789"))

    for file in file_list:
        os.rename(file, file.translate(tabela))
    os.chdir("/Users/vinicius.marinho/Udacity/Udacity_lesson1")

rename_files()