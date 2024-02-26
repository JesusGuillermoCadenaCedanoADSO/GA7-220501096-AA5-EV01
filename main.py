#Evidencia de desempeño: GA7-220501096-AA5-EV01 diseño y desarrollo de #servicios web - caso
#nombre: Jesus Guillermo Cadena Cedano
#grupo: 2547389
#programa: análisis y desarrollo de software

from flask import Flask, request, jsonify

#Inicializa la aplicacion
app = Flask(__name__)

# Datos de usuario y contraseña (simulación)
usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2",
    "usuario3": "contraseña3"
}

#Genera la ruta
@app.route('/autenticar', methods=['POST'])
def autenticar_usuario():
    # Obtener datos de usuario y contraseña del cuerpo de la solicitud
    datos = request.json
    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')

    # Verificar usuario y contraseña
    if usuario in usuarios and usuarios[usuario] == contraseña:
        # Autenticación exitosa
        respuesta = {"autenticacion": "autenticación satisfactoria"}
    else:
        # Autenticación fallida
        respuesta = {"autenticacion": "autenticación incorrecta"}

    return jsonify(respuesta)

#Inicializa el servidor
if __name__ == '__main__':
    app.run(debug=True)


