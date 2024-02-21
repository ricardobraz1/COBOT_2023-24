from PIL import Image

img = Image.open("image_kratos.png")

max_colors = 1000      # parâmetro definido para setar um limite de cores

print(img.getcolors(max_colors))