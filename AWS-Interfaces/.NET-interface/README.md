# Installing .NET SDK

1. Generate the Access Keys using the below link.
    - https://console.aws.amazon.com/iam/home?region=us-east-1#/security_credentials

1. Create `%USERPROFILE%\.aws\credentials` file in Windows with the below content. Make sure to replace the Access Keys.
    >[dotnet-tutorials]  
    >aws_access_key_id = AKIAIOSFODNN7EXAMPLE  
    >aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

1. Install Microsoft Visual Studio if not from the below link.
    - https://visualstudio.microsoft.com/vs/

1. Open Visual Studio and create a new project that uses the C# version of the Console Application template ("...for creating a command-line application that can run on .NET Core..."). Name the project S3CreateAndList.

1. With the newly created project loaded, choose Tools, NuGet Package Manager, Manage NuGet Packages for Solution. Browse for the AWSSDK.S3 NuGet package and install it into the project.

1. Replace the code in `Program.cs` with the code from `s3-buckets.cs`.

1. Build the project (Ctrl + B).

1. Open a command prompt now and navigate to the folder that will contain the build output. This is typically something like S3CreateAndList\S3CreateAndList\bin\Debug\netcoreapp3.1, but will depend on our environment.

1. In the command prompt, use the following.
    >set AWS_PROFILE=dotnet-tutorials  
    >set AWS_REGION=us-east-1  

1. Execute the program without any parameters to get the list of buckets.

1. Execute the program with the bucket name to create one. Verify the same from the management console.

# Further Reading

1. Developing Windows-based application using the AWS SDK for .NET
    - https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/quick-start-s3-1-winvs.html

1. AWS SDK for .NET API Reference
    - https://docs.aws.amazon.com/sdkfornet/v3/apidocs/Index.html

1. .NET code samples
    - https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/tutorials-examples.html
    - https://aws.amazon.com/developer/language/net/code-samples/net-code-samples/

1. PowerShell code samples
    - https://aws.amazon.com/developer/language/net/code-samples/powershell-code-samples/

1. Nuget packages
    - https://www.nuget.org/packages?q=Tags%3A%22aws-sdk-v3%22

1. AWS Toolkit for Visual Studio Code
    - https://aws.amazon.com/visualstudiocode/
    - https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html