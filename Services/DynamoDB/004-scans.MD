
# Scans

The Scan call is the bluntest instrument in the DynamoDB toolset. By way of analogy, the GetItem call is like a pair of tweezers, deftly selecting the exact Item you want. The Query call is like a shovel -- grabbing a larger amount of Items but still small enough to avoid grabbing everything.

The Scan operation is like a payloader, grabbing everything in its path. The Scan operation operates on your entire table. For tables of real size, this can quickly use up all of your Read Capacity. If you're using it in your application's critical path, it will be very slow in returning a response to your users.

The Scan operation generally makes sense only in the following situations:

1. you have a very small table;
1. you're exporting all of your table's data to another storage system; or
1. you use global secondary indexes in a special way to set up a work queue (very advanced).

<pre>
aws dynamodb scan \
    --table-name UserOrdersTable
</pre>

DynamoDB has a 1MB limit on the amount of data it will retrieve in a single request. Scans will often hit this 1MB limit if you're using your table for real use cases, which means you'll need to paginate through results.

If you hit the 1MB limit with a Scan, it will return a "NextToken" key in the response. You can use the value given with the --starting-token option to continue scanning from the location you previously ended.

<pre>
aws dynamodb scan \
    --table-name UserOrdersTable \
    --max-items 1
</pre>

## Parallel scan

For scanning to happen in parallel when getting a log of data.

<pre>
aws dynamodb scan \
    --table-name UserOrdersTable \
    --total-segments 3 \
    --segment 1
</pre>