// Load the AWS SDK for Node.js
var AWS = require('aws-sdk');
// Set the region 
AWS.config.update({region: 'us-east-1'});

// Create EC2 service object
var ec2 = new AWS.EC2({apiVersion: '2016-11-15'});

// CHANGE
var params = {
   GroupId: 'sg-03b38c738017bafa5'
};

// Delete the security group
ec2.deleteSecurityGroup(params, function(err, data) {
   if (err) {
      console.log("Error", err);
   } else {
      console.log("Security Group Deleted");
   }
});