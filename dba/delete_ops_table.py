import boto3

def delete_tournaments_table(dynamodb=None):
    if not dynamodb:
        #dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

    table = dynamodb.Table('Tournaments')
    table.delete()


if __name__ == '__main__':
    delete_tournaments_table()
    print("Tournaments table deleted.")