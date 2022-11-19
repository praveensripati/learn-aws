
# Querying

We looked at working with individual Items at a time. That can be useful in some scenarios, such as working with Users. We're usually manipulating a single User at a time, whether retrieving a User's profile or changing a User's name.

It's less helpful in other situations, such as working with Orders. Occasionally we want to grab a specific Order, but we also may want to display all the Orders for a particular User. It would be inefficient to store the different partition keys for each User's Orders and query those Items separately.

Querying is a very powerful operation in DynamoDB. It allows you to select multiple Items that have the same partition ("HASH") key but different sort ("RANGE") keys.
<pre>
aws dynamodb query \
    --table-name UserOrdersTable \
    --key-condition-expression "Username = :username" \
    --expression-attribute-values '{
        ":username": { "S": "daffyduck" }
    }'</pre>

## When querying to return Items, you might want to further limit the Items returned rather than returning all Items with a particular HASH key.
<pre>
aws dynamodb query \
    --table-name UserOrdersTable \
    --key-condition-expression "Username = :username AND OrderId BETWEEN :startdate AND :enddate" \
    --expression-attribute-values '{
        ":username": { "S": "daffyduck" },
        ":startdate": { "S": "20170101" },
        ":enddate": { "S": "20180101" }
    }'</pre>

## A second way to handle this is with filtering based on non-key attributes. This is less efficient than Key Expressions but can still be helpful in the right situations.

Filter expressions are used to apply server-side filters on Item attributes before they are returned to the client making the call.
<pre>
aws dynamodb query \
    --table-name UserOrdersTable \
    --key-condition-expression "Username = :username" \
    --filter-expression "Amount > :amount" \
    --expression-attribute-values '{
        ":username": { "S": "daffyduck" },
        ":amount": { "N": "100" }
    }'</pre>