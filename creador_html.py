def creador_usuario(nombre, fecha, curso):

    usuario = {
        "nombre": nombre,
        "fecha": fecha,
        "curso": curso,
    }
    return usuario


def crear_html(usuario):
    template = open("template.html", "r")
    salida = open("".join([usuario.get("nombre"), ".html"]), "w")
    texto_template = template.read().format(get_user=usuario.get("nombre"),
                                            get_fecha=usuario.get("fecha"),
                                            get_curso=usuario.get("curso"))

    salida.write(texto_template)


user1 = creador_usuario("Mariano", "18/11/2017", "Python")
crear_html(user1)
