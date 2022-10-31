import json
import requests
from flask import Blueprint, jsonify, request, Response

player_service = Blueprint(name="player_service", import_name=__name__)

@player_service.route('/informacion/jugadores/v2/<equipo_id>', methods=['GET'])
def informacion_equipov2(equipo_id):
    try:

        ##procesamiento de los datos
        url = "https://api-football-v1.p.rapidapi.com/v3/players/squads"

        querystring = {"team": str(equipo_id)}

        headers = {
            "X-RapidAPI-Key": "fb450516e1msh73eecc24fc1f4d4p1436fajsn95fc6843edad",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(str(response.text))
        data_response = {
            "informacion": {},
            "seasons": {}
        }
        data_response['informacion'] = data['response']

        return jsonify({
            "estado": 1,
            "mensaje": "ejecucion correcta",
            "respuesta": data_response
        }),200
    except Exception as e:
        return jsonify({
            "estado": 1,
            "respuesta": [],
            "mensaje": "El servidor no puede procesar la solicitud en este momento. " + str(e)
        }),500