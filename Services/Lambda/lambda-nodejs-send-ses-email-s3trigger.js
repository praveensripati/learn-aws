var aws = require('aws-sdk');

var ses = new aws.SES({ region: 'us-east-1' });

exports.handler = function (event, context) {
	console.log("Incoming: ", event);
	// var output = querystring.parse(event);

	var eParams = {
		Destination: {
			ToAddresses: ["ugetaws@gmail.com"]//give the email ID which is verified by SES
		},
		Message: {
			Body: {
				Text: {
					Data: "lambda is working"
				}
			},
			Subject: { Data: "mail from ses" }
		},
		Source: "praveensripati@gmail.com" //give the email ID which is verified by SES
	};

	console.log('===SENDING EMAIL===');

	var email = ses.sendEmail(eParams, function (err, data) {
		if (err) console.log(err);
		else {
			console.log("===EMAIL SENT===");
			console.log(data);
			console.log("EMAIL CODE END");
			console.log('EMAIL: ', email);
			context.succeed(event);
		}
	});
};