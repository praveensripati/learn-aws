# ElasticBeanstalk (PAAS)

1. Download tomcat.zip from the below URL.
https://aws.amazon.com/elasticbeanstalk/

1. Go to the Elastic BeanStalk Management Console.

1. Click on `Create Application`.

1. In this screen.
    - Enter the Application name.
    - Select the platform as Tomcat.
    - In the `Source code origin`, choose "Choose file" and upload tomcat.zip file uploaded earlier.
    - Click on "Create application".

1. It takes a while for the application to be created. Click on the Application created in the left pane and grab the URL.

1. Open the URL in the browser to see the Tomcat application which has been deployed.

1. Make sure to delete the Application.

# Further Reading

https://aws.amazon.com/elasticbeanstalk/

Getting started
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html

Concepts
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.html

Extensions to Elastic Beanstalk
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-resources.html

Sample configuration files
https://github.com/awsdocs/elastic-beanstalk-samples/tree/master/configuration-files

Adding a DB to the Elastic Beanstalk Environment. Can be done manually or by using the extensions.
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.db.html