import os

ruta_archivo = "C:/Users/Jesus/VSProjects/Python/CuentasPy/cuentas.txt"
flags = os.O_RDWR | os.O_CREAT
mode = 0o666


def write_data(data):
    try:
        with os.fdopen(os.open(ruta_archivo, flags, mode), "w") as file_object:
            file_object.write(data)
            print("-- Datos escritos correctamente. --")
    except NameError:
        print(NameError)


def read_data():
    file_descriptor = ""
    try:
        file_descriptor = os.open(ruta_archivo, flags, mode)
        file_size = os.path.getsize(file_descriptor)
        content = os.read(file_descriptor, file_size)
        string_content = content.decode()
        print("-- Datos leidos correctamente. --")
        return string_content
    except NameError:
        print("error"
        )
    finally:
        os.close(file_descriptor)
