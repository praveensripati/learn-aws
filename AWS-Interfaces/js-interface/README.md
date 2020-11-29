# Installing Node.js SDK and execute programs.

1. Execute the below commands on the EC2 instance.

    >sudo apt update\
    >sudo apt install nodejs npm -y

1. Create a folder in the EC2 instance.

    >mkdir js

1. From the same folder execute the below commands to install the `aws-sdk` and `uuid` modules. A `node_modules` subdirectory will be automatically created. If any warnings, ignore them.

    >cd js\
    >npm install aws-sdk\
    >npm install uuid

1. Copy the js files to the same folder. Execute the program using the below command.

    >node create-s3-bucket-object.js

1. Execute the different programs in this folder and also from the below `Examples` section.

# Further Reading

1. Modular packages in AWS SDK for JavaScript
    - https://aws.amazon.com/blogs/developer/modular-packages-in-aws-sdk-for-javascript/

1. How To Install Node.js on Ubuntu 18.04
    - https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04

1. Getting Started in Node.js
    - https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-nodejs.html

1. JavaScript API
    - https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/

1. Examples
    - https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sdk-code-samples.html
    - https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-javascript.html