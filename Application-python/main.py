import os
import shutil

def search_and_organize_folder(folder_path):
    # Créer les dossiers cibles
    audio_folder = os.path.join(folder_path, "audio")  # Dossier pour les fichiers audio
    cv_folder = os.path.join(folder_path, "cv")  # Dossier pour les fichiers CV
    pdf_folder = os.path.join(folder_path, "pdf")  # Dossier pour les fichiers PDF
    image_folder = os.path.join(folder_path, "images")  # Dossier pour les images
    zip_folder = os.path.join(folder_path, "zip")  # Dossier pour les fichiers ZIP

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Vérifier le type de fichier et le déplacer vers le dossier approprié
            if file.endswith((".mp3", ".wav", ".flac")):
                move_file(file_path, audio_folder)
            elif file.endswith(".pdf"):
                move_file(file_path, pdf_folder)
            elif file.endswith((".jpg", ".jpeg", ".png", ".gif")):
                move_file(file_path, image_folder)
            elif file.endswith(".zip"):
                move_file(file_path, zip_folder)
            elif "CV" in file.upper() or "RESUME" in file.upper():
                move_file(file_path, cv_folder)

def move_file(source, destination):
    try:
        os.makedirs(destination, exist_ok=True)
        shutil.move(source, destination)
        print(f"Le fichier {source} a été déplacé vers {destination}.")
    except FileNotFoundError:
        print("Le fichier source n'existe pas.")
    except FileExistsError:
        print("Le fichier de destination existe déjà.")

def main():
    desktop_path = os.path.expanduser("/Users/omar/Desktop")  # Chemin du bureau
    search_and_organize_folder(desktop_path)

if __name__ == "__main__":
    main()
