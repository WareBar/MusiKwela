from PIL import Image, ImageTk


def photoRender(path,height,width):
    variable_name = Image.open(path)
    variable_name = variable_name.resize((height, width), Image.LANCZOS)
    variable_name = ImageTk.PhotoImage(variable_name)
    return variable_name