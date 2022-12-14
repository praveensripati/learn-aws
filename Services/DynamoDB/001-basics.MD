
# Basic commands.

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
      }'</pre>

1. List the tables.
    <pre>
    aws dynamodb list-tables</pre>

1. Describe the tables.
    <pre>
    aws dynamodb describe-table \
      --table-name UsersTable</pre>

## Expressions

<b>Condition expressions</b> are used when manipulating individual items to only change an item when certain conditions are true.<br/>
<b>Projection expressions</b> are used to specify a subset of attributes you want to receive when reading Items. We used these in our GetItem calls in the previous lesson.<br/>
<b>Update expressions</b> are used to update a particular attribute in an existing Item.<br/>
<b>Key condition expressions</b> are used when querying a table with a composite primary key to limit the items selected.<br/>
<b>Filter expressions</b> allow you to filter the results of queries and scans to allow for more efficient responses.<br/>

  
## Condition expressions
<b>Condition expressions</b> are used when manipulating individual items to only change an item when certain conditions are true.<br/>
<pre>
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
    }'</pre>
	
## Projection expressions
<b>Projection expressions</b> are used to specify a subset of attributes you want to receive when reading Items. We used these in our GetItem calls in the previous lesson.<br/>
<pre>
aws dynamodb get-item \
    --table-name UsersTable \
    --projection-expression "Age, Username" \
    --key '{
      "Username": {"S": "yosemitesam"}
    }'</pre>

## Update expressions
<b>Update expressions</b> are used to update a particular attribute in an existing Item.<br/>
When using the update expression, you must include one of four update clauses. These clauses are:

1. SET: Used to add an attribute to an Item or modify an existing attribute;
1. REMOVE: Used to delete attributes from an Item.
1. ADD: Used to increment/decrement a Number or insert elements into a Set.
1. DELETE: Used to remove items from a Set.

<pre>
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
    }'</pre>