// Before executing the program
// make sure that the bucket is empty

// Load the AWS SDK for Node.js
var AWS = require('aws-sdk');
// Set the region
AWS.config.update({region: 'us-east-1'});

// Create S3 service object
s3 = new AWS.S3({apiVersion: '2006-03-01'});

// CHANGE
// Create params for S3.deleteBucket
var bucketParams = {
  Bucket : 'node-sdk-sample-c3808558-0b09-4415-b5a0-1a6c501abd61'
};

// Call S3 to delete the bucket
s3.deleteBucket(bucketParams, function(err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data);
  }
});
