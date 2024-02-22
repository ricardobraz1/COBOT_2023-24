from PIL import Image
import os




# código para buscar os arquivos no diretório

# print("Diretório de trabalho atual:", os.getcwd())                   # Verifica o diretório de trabalho atual
# print("Arquivos na pasta:", os.listdir())                            # Lista os arquivos na pasta atual


# código de detecção de cores

img = Image.open("image_kratos.png")

max_colors = 900000      # parâmetro definido para setar um limite de cores

print(img.getcolors(max_colors))