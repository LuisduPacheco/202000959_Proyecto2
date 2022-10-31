##IMPORTS
from flask import Flask, jsonify, request ## IMPORTS ESPECIFICOS DE FLASK
from flask_cors import CORS ## IMPORT QUE PERMITE EL CORS ORIGINS FLASK
from flask_socketio import SocketIO ## MODULO SOCKET FLASK

#### pip install flak
#### pip install flask_cors
#### pip install flask_socketio

## IMPORTAR LOS ENDPOINTS
from src.equipo.team import team_service
from src.jugador.player import player_service

##DEFINICION DE LA APLICACION
app = Flask(__name__)
CORS(app) ## PERMITIMOS CORS
socket = SocketIO(app, cors_allowed_origins="*") ##DEFINIMOS CORS


### BLUEPRINT --- ROUTES DE ENDPOINTS
app.register_blueprint(team_service, url_prefix="/v1/equipo")
app.register_blueprint(player_service, url_prefix="/v1/jugador")



##ENDPOINT PRINCIPAL
@app.route('/', methods=['GET'])
def aplicacion():
    return jsonify({
        "Curso": "Introduccion a la programacion y computacion 1 - USAC"
    })


## INICIALIZAR EL SERVER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port='3000', debug=True)
 