from decimal import Decimal
import json
import boto3


def load_cards(cards, dynamodb=None):
    if not dynamodb:
        #dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

    table = dynamodb.Table('Cards')
    for card in cards:
        year = int(card['year'])
        title = card['title']
        print("Adding card:", year, title)
        table.put_item(Item=card)


if __name__ == '__main__':
    with open("loadCards.json") as json_file:
        card_list = json.load(json_file, parse_float=Decimal)
    load_cards(card_list)

