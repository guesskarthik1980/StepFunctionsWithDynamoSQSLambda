#this is a lambda function to confirm the purchase 
import json
import datetime

def lamdba_handler(event, context):
    #Sample Input for the event
    #{"TransactionType":"PURCHASE", "CardType":"Mastercard", "Amount":"$1200"}
    # step 1 - log in the input message
    print("The input message is below")
    print(event)

    #step 2 - produce response
    response = {}
    response['TransactionId'] = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    response['TransactionType'] = event['TransactionType']
    response['CardType'] = event['CardType']
    response['Amount'] = event['Amount']
    response['TransactionDate'] = datetime.datetime.now().strftime("%Y-%m-%d: %H:%M:%S")
    response['Message'] = "Successfully Processed"

    #Step 3 - return the response
    return {
        'statusCode':200,
        'body':response
    }