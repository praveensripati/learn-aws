
# Batch Writes

1. Create a table with Composite Primary Key
    <pre>
    aws dynamodb create-table \
        --table-name UserOrdersTable \
        --attribute-definitions '[
        {
            "AttributeName": "Username",
            "AttributeType": "S"
        },
        {
            "AttributeName": "OrderId",
            "AttributeType": "S"
        }
        ]' \
        --key-schema '[
        {
            "AttributeName": "Username",
            "KeyType": "HASH"
        },
        {
            "AttributeName": "OrderId",
            "KeyType": "RANGE"
        }
        ]' \
        --provisioned-throughput '{
        "ReadCapacityUnits": 1,
        "WriteCapacityUnits": 1
        }'</pre>

1. Insert multiple Items at once.
    <pre>
    aws dynamodb batch-write-item \
        --request-items '{
            "UserOrdersTable": [
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20160630-12928"},
                            "Amount": {"N": "142.23"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "daffyduck"},
                            "OrderId": {"S": "20170608-10171"},
                            "Amount": {"N": "18.95"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "daffyduck"},
                            "OrderId": {"S": "20170609-25875"},
                            "Amount": {"N": "116.86"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "daffyduck"},
                            "OrderId": {"S": "20160630-28176"},
                            "Amount": {"N": "88.30"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "yosemitesam"},
                            "OrderId": {"S": "20170609-18618"},
                            "Amount": {"N": "122.45"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170609-4177"},
                            "Amount": {"N": "27.89"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170608-24041"},
                            "Amount": {"N": "142.02"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "yosemitesam"},
                            "OrderId": {"S": "20170609-17146"},
                            "Amount": {"N": "114.00"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "yosemitesam"},
                            "OrderId": {"S": "20170609-9476"},
                            "Amount": {"N": "19.41"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20160630-13286"},
                            "Amount": {"N": "146.37"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170609-8718"},
                            "Amount": {"N": "76.19"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "daffyduck"},
                            "OrderId": {"S": "20171129-29970"},
                            "Amount": {"N": "6.98"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170609-10699"},
                            "Amount": {"N": "122.52"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20160630-25621"},
                            "Amount": {"N": "141.78"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170330-29929"},
                            "Amount": {"N": "80.36"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "yosemitesam"},
                            "OrderId": {"S": "20160630-4350"},
                            "Amount": {"N": "138.93"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170330-20659"},
                            "Amount": {"N": "47.79"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170115-20782"},
                            "Amount": {"N": "80.05"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "yosemitesam"},
                            "OrderId": {"S": "20170330-18781"},
                            "Amount": {"N": "98.40"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "yosemitesam"},
                            "OrderId": {"S": "20170330-1645"},
                            "Amount": {"N": "25.53"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170115-2268"},
                            "Amount": {"N": "37.30"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170609-8267"},
                            "Amount": {"N": "32.13"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20170330-3572"},
                            "Amount": {"N": "126.17"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "alexdebrie"},
                            "OrderId": {"S": "20171129-28042"},
                            "Amount": {"N": "83.12"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "Username": {"S": "yosemitesam"},
                            "OrderId": {"S": "20170609-481"},
                            "Amount": {"N": "136.68"}
                        }
                    }
                }
            ]
        }'</pre>