import flask
from flask import request, jsonify, abort
import json
from decimal import Decimal
from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from .create_hash import create_hash


def create_tournament(title, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

    table = dynamodb.Table('Tournaments')
    tournament_id = create_hash()
    response = table.put_item(
       Item={
            'tournamentId': tournament_id,
            'title': title,
        }
    )
    return read_tournament(tournament_id)


def query_tournaments(tournament_id):
    dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

    table = dynamodb.Table('Tournaments')
    response = table.query(
       KeyConditionExpression=Key('tournamentId').eq(tournament_id)
    )
    return response['Items']


def read_tournament(tournament_id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

    table = dynamodb.Table('Tournaments')

    try:
        response = table.get_item(Key={'tournamentId': tournament_id})
    except ClientError as err:
        print(err.response['Error']['Message'])
    else:
        return response['Item']


def update_tournament(tournament_id, title, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

    table = dynamodb.Table('Tournaments')

    response = table.update_item(
        Key={
            'tournamentId': tournament_id,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            ':r': Decimal(rating),
            ':p': plot,
            ':a': actors
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


def delete_tournament(tournament_id, title, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

    table = dynamodb.Table('Tournamnent')

    try:
        response = table.delete_item(Key={'tournamentId': tournament_id, 'title': title})
    except ClientError as err:
        print(err.response['Error']['Message'])
    else:
        return print(flask.jsonify(response))