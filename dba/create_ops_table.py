import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')


def create_tournaments_table(dynamodb=None):
    if not dynamodb:
        #dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

    table = dynamodb.create_table(
        TableName='Tournaments',
        KeySchema=[
            {
                'AttributeName': 'tournamentId',
                'KeyType': 'HASH'  #Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'tournamentId',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return table

if __name__ == '__main__':
    tournaments_table = create_tournaments_table()
    print("Table status:", tournaments_table.table_status)