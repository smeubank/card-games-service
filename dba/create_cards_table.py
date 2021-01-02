import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')


def create_cards_table(dynamodb=None):
    if not dynamodb:
        #dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
        dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

    table = dynamodb.create_table(
        TableName='Cards',
        KeySchema=[
            {
                'AttributeName': 'cardId',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'sort',
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'cardId',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'sort',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return table

if __name__ == '__main__':
    cards_table = create_cards_table()
    print("Cards table status:", cards_table.table_status)