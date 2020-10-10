# StepFunctionsWithDynamoSQSLambda
CC processing transaction designed with Step functions using Lambda, DynamoDB, SQS.

Below is the design view of the CC Processing example defined for Step functions


#Step 1 - Development of the Lambda
#Step 2 - create Dynamo DB - "TransactionHistory" and add "TransactionId" as partition Key
#Step 3 - Create SQS Queue - you need the QueueURL to be passed in the Steps Functions
#Step 4 - set up IAM role for Step Function with policies to "access SQS messages", "Execute Lambda" and "Accessing Dynamo DB"
#Step 5 - create Step Function
#Step 6 -  Test it out by executing the Step functions using the following Data

PURCHASE JSON
{
"TransactionType":"PURCHASE",
"CardType":"Visa",
"Amount":"$1234"
}

REFUND JSON
{
"TransactionType":"REFUND",
"CardType":"Visa",
"Amount":"$1234"
}


