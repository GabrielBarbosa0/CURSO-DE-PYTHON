import os
import shutil

# Caminho da pasta de downloads (altere conforme necessário)
downloads_folder = os.path.expanduser("~/Downloads")

# Categorias e extensões correspondentes
categories = {
    "Compressed": ["7z", "7zip", "rar", "zip", "tar", "gz", "bz2", "xz", "lzma", "z", "lz", "iso", "war", "apk"],
    "Imagens": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "tif", "webp", "heif", "heic", "svg", "ico", "avif", "jfif"],
    "Vídeos": ["mp4", "avi", "mkv", "mov", "wmv", "flv", "webm", "mpg", "mpeg", "3gp", "m4v", "ogv"],
    "Músicas": ["mp3", "wav", "flac", "aac", "ogg", "wma", "m4a", "alac", "opus", "amr"],
    "Documentos": ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "rtf", "odt", "ods", "odp", "csv"],
    "Scripts": ["py", "js", "html", "css", "java", "c", "cpp", "cs", "php", "rb", "go", "ts"],
    "Design e Modelagem 3D": ["psd", "ai", "eps", "cdr", "sketch", "fig", "fbx", "obj", "stl", "glb" "ply", "gltf", "blend", "max", "c4d", "ma", "mb"],
    "Arquivos SketchUp": ["skp", "rpz"],
    "Projetos Revit": ["rvt", "rte", "rfa"],
    "Programas": ["exe", "msi", "dmg", "sh", "deb", "rpm", "bat", "com", "jar"],
    "Arquivos AutoCAD": ["dwg", "dxf", "dwt", "ctb", "stb", "plt", "shx", "pat", "lin", "pc3", "arg", "bak", "sv$", "ac$"]
}

def organize_downloads(folder):
    # Iterar sobre os arquivos na pasta de downloads
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        
        # Ignorar pastas
        if os.path.isdir(filepath):
            continue

        # Obter a extensão do arquivo
        file_ext = filename.split(".")[-1].lower()

        # Procurar a categoria correspondente
        for category, extensions in categories.items():
            if file_ext in extensions:
                # Criar a pasta, se necessário
                category_folder = os.path.join(folder, category)
                os.makedirs(category_folder, exist_ok=True)
                
                # Mover o arquivo para a pasta correspondente
                shutil.move(filepath, os.path.join(category_folder, filename))
                print(f"Movido: {filename} -> {category}")
                break

# Executar a função
if __name__ == "__main__":
    organize_downloads(downloads_folder)
    print("Organização concluída!")

# Desenvolvido por GabrielBarbosa0 Github!