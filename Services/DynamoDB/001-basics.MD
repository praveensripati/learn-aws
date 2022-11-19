

Basic commands.

1. Create a table with Simple Primary Key.
<pre>
aws dynamodb create-table \
  --table-name UsersTable \
  --attribute-definitions '[
    {
        "AttributeName": "Username",
        "AttributeType": "S"
    }
  ]' \
  --key-schema '[
    {
        "AttributeName": "Username",
        "KeyType": "HASH"
    }
  ]' \
  --provisioned-throughput '{
    "ReadCapacityUnits": 1,
    "WriteCapacityUnits": 1
  }'
</pre>

aws dynamodb list-tables


aws dynamodb describe-table \
  --table-name UsersTable
  
  
Condition expressions are used when manipulating individual items to only change an item when certain conditions are true.
Projection expressions are used to specify a subset of attributes you want to receive when reading Items. We used these in our GetItem calls in the previous lesson.
Update expressions are used to update a particular attribute in an existing Item.
Key condition expressions are used when querying a table with a composite primary key to limit the items selected.
Filter expressions allow you to filter the results of queries and scans to allow for more efficient responses.

  
#Condition expressions
aws dynamodb put-item \
    --table-name UsersTable \
    --item '{
      "Username": {"S": "yosemitesam"},
      "Name": {"S": "Yosemite Sam"},
      "Age": {"N": "73"}
    }' \
    --condition-expression "attribute_not_exists(#u)" \
    --expression-attribute-names '{
      "#u": "Username"
    }'
	
aws dynamodb get-item \
    --table-name UsersTable \
    --key '{
      "Username": {"S": "yosemitesam"}
    }'

	
#Projection expressions
aws dynamodb get-item \
    --table-name UsersTable \
    --projection-expression "Age, Username" \
    --key '{
      "Username": {"S": "yosemitesam"}
    }'
	

When using the update expression, you must include one of four update clauses. These clauses are:

SET: Used to add an attribute to an Item or modify an existing attribute;
REMOVE: Used to delete attributes from an Item.
ADD: Used to increment/decrement a Number or insert elements into a Set.
DELETE: Used to remove items from a Set.


aws dynamodb update-item \
    --table-name UsersTable \
    --key '{
      "Username": {"S": "yosemitesam"}
    }' \
    --update-expression 'SET #dob = :dob' \
    --expression-attribute-names '{
      "#dob": "DateOfBirth"
    }' \
    --expression-attribute-values '{
      ":dob": {"S": "1937-04-17"}
    }'
	
	
aws dynamodb delete-item \
    --table-name UsersTable \
    --key '{
      "Username": {"S": "daffyduck"}
    }'
	
