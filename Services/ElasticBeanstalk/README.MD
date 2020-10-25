# ElasticBeanstalk (PAAS)

1. Download tomcat.zip from the below URL.
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/tutorials.html

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

1. Home Page
    - https://aws.amazon.com/elasticbeanstalk/

1. Getting started
    - https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html

1. Concepts
    - https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.html

1. Extensions to Elastic Beanstalk
    - https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html
    - https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-resources.html

1. Sample configuration files
    - https://github.com/awsdocs/elastic-beanstalk-samples/tree/master/configuration-files

1. Adding a Database to the Elastic Beanstalk Environment. Can be done manually or by using the extensions.
    - https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.db.html