import json
import requests
from flask import Blueprint, jsonify, request, Response

team_service = Blueprint(name="team_service", import_name=__name__)

## variables globales
league_id = 1488

## definir peticiones teams

@team_service.route('/informacion/liga', methods=['GET'])
def informacion_liga():
    try:

        ##procesamiento de los datos
        url = "https://api-football-v1.p.rapidapi.com/leagues/league/"+str(league_id)

        headers = {
            "X-RapidAPI-Key": "fb450516e1msh73eecc24fc1f4d4p1436fajsn95fc6843edad",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        data = json.loads(str(response.text))
        data_response = {
            "informacion": {}
        }
        data_response['informacion'] = data['api']['leagues'][str(league_id)]

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

@team_service.route('/informacion/equipos', methods=['GET'])
def informacion_equipos():
    try:

        ##procesamiento de los datos
        url = "https://api-football-v1.p.rapidapi.com/teams/league/"+str(league_id)
        headers = {
            "X-RapidAPI-Key": "fb450516e1msh73eecc24fc1f4d4p1436fajsn95fc6843edad",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        data = json.loads(str(response.text))
        data_response = {
            "informacion": {}
        }
        data_response['informacion'] = data['api']['teams']

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

@team_service.route('/informacion/equipos/v1/<equipo_id>', methods=['GET'])
def informacion_equipo(equipo_id):
    try:

        ##procesamiento de los datos
        url = "https://api-football-v1.p.rapidapi.com/teams/team/"+str(equipo_id)
        headers = {
            "X-RapidAPI-Key": "fb450516e1msh73eecc24fc1f4d4p1436fajsn95fc6843edad",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        data = json.loads(str(response.text))
        data_response = {
            "informacion": {}
        }
        data_response['informacion'] = data['api']['teams'][str(equipo_id)]

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

@team_service.route('/informacion/equipos/v2/<equipo_id>', methods=['GET'])
def informacion_equipov2(equipo_id):
    try:

        ##procesamiento de los datos
        url = "https://api-football-v1.p.rapidapi.com/v3/teams"
        url_season = "https://api-football-v1.p.rapidapi.com/v3/teams/seasons"
        querystring = {"id": str(equipo_id)}
        querystring_season = {"team": str(equipo_id)}

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

        response_season = requests.request("GET", url_season, headers=headers, params=querystring_season)
        data_season = json.loads(str(response_season.text))
        data_response['seasons'] = data_season['response']

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
    