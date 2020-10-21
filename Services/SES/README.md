# Sending emails

AWS SES is a service for sending emails without bothering about setting up a SMTP server. Also, we don't need to worry about high availability, scalability, licensing, upgrading and patching up the SMTP server.

1. SendBulkEmail.java is program which takes the list of emails and the email templates as the input and sends out emails in bulk. The same can be used for marketing, sales and promotion.

# Further Reading

https://aws.amazon.com/ses/

Sending email using Python Boto
https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html

Configuration sets
https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html

# TODO

1. The SendBulkEmail.java program works as-is, but has to be cleaned and also more comments have to be included.