import os
import glob
import face_recognition
from PIL import Image

def sort_faces(dataset_direct, same_faces_direct, another_faces_direct, image_of_face):
    try:
        face = face_recognition.load_image_file(image_of_face)
        face_encodings = face_recognition.face_encodings(face)[0]
    except FileNotFoundError:
        print("[Error]: Выбранное фото не содержит лиц ;(")
        return None

    for path in glob.iglob(f'{dataset_direct}/*'):
        path = path.replace('\\', '/')

        try:
            face_2 = face_recognition.load_image_file(path)
            face_2_encodings = face_recognition.face_encodings(face_2)[0]
        except:
            print("[Error]: У этой картинки нет лица ;(")
            continue

        result = face_recognition.compare_faces([face_encodings], face_2_encodings)

        if result[0]:
            same_path = path.split('/')[-1]
            new_path = f"{same_faces_direct}"

            if os.path.exists(same_faces_direct):
                if os.path.isdir(same_faces_direct):
                    img = Image.open(path)
                    img.save(f"{new_path}/{same_path}")
            else:
                os.mkdir(new_path)
                img = Image.open(path)
                img.save(f"{new_path}/{same_path}")
        else:
            another_path = path.split("/")[-1]
            new_path = f"{another_faces_direct}"

            if os.path.exists(another_faces_direct):
                if os.path.isdir(another_faces_direct):
                    img = Image.open(path)
                    img.save(f"{new_path}/{another_path}")
            else:
                os.mkdir(another_faces_direct)
                img = Image.open(path)
                img.save(f"{new_path}/{another_path}")


def main():
    with open("pathes.txt", "r") as file:
        src = file.readlines()
    path_1 = src[0].replace('\\', '/').split('\n')[0]
    path_2 = src[1].replace('\\', '/').split('\n')[0]
    path_3 = src[2].replace('\\', '/').split('\n')[0]
    path_4 = src[3].replace('\\', '/').split('\n')[0]

    sort_faces(path_1, path_2, path_3, path_4)

if __name__ == '__main__':
    main()