# Sending emails

AWS SES is a service for sending emails without bothering about setting up a SMTP server. Also, we don't need to worry about high availability, scalability, licensing, upgrading and patching up the SMTP server.

1. `SendBulkEmail.java` is program which takes the list of emails and the email templates as the input and sends out emails in bulk. The same can be used for marketing, sales and promotion.

# Further Reading

1. Home Page
    - https://aws.amazon.com/ses/

1. Sending email using Boto3 (AWS Python SDK)
    - https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html

1. Configuration sets
    - https://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html

# TODO

1. The SendBulkEmail.java program works ASIS, but has to be cleaned and also more comments have to be included.