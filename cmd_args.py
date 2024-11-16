def hello(name, lang):
    greetins = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"
    }

    print(f"{greetins[lang]} {name}")

if __name__ == "__main__":
    import argparse
    # Creamos el objeto encargado de procesar los argumentos
    parser = argparse.ArgumentParser(description="Provides a personal greting.")

    # Creamos un argumento flag
    parser.add_argument(
        "-n", 
        "--name", 
        metavar="name",     # Esto aparece al hacer help
        required=True,      # Es requisito indicar un name para hacer funcionar el script
        help="the name of the person to greet"      # Descripción
    )

    parser.add_argument(
        "-l", 
        "--lang", 
        metavar="lang",         # Esto aparece al hacer help
        required=True,          # Es requisito indicar un name para hacer funcionar el script
        choices=["English", "Spanish", "German"],
        help="the language you talk"      # Descripción
    )

    # Recibimos los argumentos
    args = parser.parse_args()

    hello(args.name, args.lang)