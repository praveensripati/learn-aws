console.log("Loading function");

var AWS = require("aws-sdk");

exports.handler = function (event, context) {
	var eventText = JSON.stringify(event, null, 2);

	console.log("Received event:", eventText);

	event.Records.forEach(record => {
		const { body } = record;
		console.log("body:", body);
	});

	var sns = new AWS.SNS();

	var params = {
		Message: "An object is added in SQS",

		Subject: "Message from SNS",

		TopicArn: "arn:aws:sns:us-east-1:304000509264:MyDemoTopic" //Give the ARN of your SNS
	};

	sns.publish(params, context.done);

	console.log("Published messages to SNS Topic");

};