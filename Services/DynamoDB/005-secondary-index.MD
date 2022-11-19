
# Secondary Indexes

There are two types of secondary indexes: local secondary indexes and global secondary indexes.

## Local secondary indexes

Local secondary indexes can be used on a table with a composite primary key to specify an index with the same HASH key but a different RANGE key for a table. This is useful for the scenario where we still want to partition our data by Username, but we want to retrieve Items by a different attribute (Amount).

Must be specified at table creation. You cannot add a local secondary index to an existing table. It must be provided at creation. You can only add local secondary indexes on tables with composite primary keys.

## Global secondary indexes

Global secondary indexes can be used to specify a completely different key structure for a table. If you had a table with a composite primary key, you could have a global secondary index with a simple key. Or, you could add a global secondary index with a completely different HASH key and RANGE key. If your table has a simple primary key, you could add a global secondary index with a composite key structure.

Unlike local secondary indexes, you can add global secondary indexes to tables with either simple primary keys or composite primary keys. Further, you're not limited to creating a composite key schema for your index -- you can create a simple key schema.

## Projected Attributes

When provisioning a secondary index, you specify which attributes you want to project into the index. This states which attributes will be available from the index directly without needing to make an additional call to the underlying table to retrieve attributes.

Your options for attribute projections are:

1. KEYS_ONLY: Your index will include only the keys for the index and the table's underlying partition and sort key values, but no other attributes.

1. ALL: The full Item is available in the secondary index with all attributes.

1. INCLUDE: You may choose to name certain attributes that are projected into the secondary index.

## Local secondary indexes

### delete the table

1. Delete the table.
    <pre>
    aws dynamodb delete-table \
        --table-name UserOrdersTable \
        $LOCAL
    </pre>

1. Create a table with the Local secondary indexes.
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
        },
        {
            "AttributeName": "Amount",
            "AttributeType": "N"
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
        --local-secondary-indexes '[
        {
            "IndexName": "UserAmountIndex",
            "KeySchema": [
                {
                    "AttributeName": "Username",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "Amount",
                    "KeyType": "RANGE"
                }
            ],
            "Projection": {
                "ProjectionType": "KEYS_ONLY"
            }
        }
        ]' \
        --provisioned-throughput '{
        "ReadCapacityUnits": 1,
        "WriteCapacityUnits": 1
        }'
    </pre>

1. Do a batch insert as mentioned earlier.

1. Querying a Local Secondary Index
    <pre>
    aws dynamodb query \
        --table-name UserOrdersTable \
        --index-name UserAmountIndex \
        --key-condition-expression "Username = :username AND Amount > :amount" \
        --expression-attribute-values '{
            ":username": { "S": "daffyduck" },
            ":amount": { "N": "100" }
        }'
    </pre>

## Global secondary indexes

1. Update the table to create a Global secondary index.

    <pre>
    aws dynamodb update-table \
        --table-name UserOrdersTable \
        --attribute-definitions '[
        {
            "AttributeName": "ReturnDate",
            "AttributeType": "S"
        },
        {
            "AttributeName": "OrderId",
            "AttributeType": "S"
        }
        ]' \
        --global-secondary-index-updates '[
            {
                "Create": {
                    "IndexName": "ReturnDateOrderIdIndex",
                    "KeySchema": [
                        {
                            "AttributeName": "ReturnDate",
                            "KeyType": "HASH"
                        },
                        {
                            "AttributeName": "OrderId",
                            "KeyType": "RANGE"
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1
                    }
                }
            }
        ]'</pre>

1. Scan the table using the above index.
    <pre>
        aws dynamodb scan \
        --table-name UserOrdersTable \
        --index-name ReturnDateOrderIdIndex</pre>