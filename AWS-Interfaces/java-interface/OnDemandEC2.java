package com.amazonaws.samples;

import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.ec2.AmazonEC2;
import com.amazonaws.services.ec2.AmazonEC2ClientBuilder;
import com.amazonaws.services.ec2.model.InstanceType;
import com.amazonaws.services.ec2.model.RunInstancesRequest;
import com.amazonaws.services.ec2.model.RunInstancesResult;

public class OnDemandEC2 {

    public static void main(String[] args) {

        try {

            // Read the default profile
            AWSCredentials credentials = new ProfileCredentialsProvider("default").getCredentials();

            // Create the EC2 client to call different EC2 APIs
            AmazonEC2 amazonEC2Client = AmazonEC2ClientBuilder.standard()
                .withCredentials(new AWSStaticCredentialsProvider(credentials)).withRegion("us-east-1").build();

            // Create a Request for Ubuntu instance with appropriate KeyPair andSecurityGroup
            RunInstancesRequest runInstancesRequest = new RunInstancesRequest();
            runInstancesRequest.withImageId("ami-0a313d6098716f372").withInstanceType(InstanceType.T1Micro)
                .withMinCount(1).withMaxCount(1).withKeyName("ProdKeyPair").withSecurityGroups("ssh_http_access");

            // Launch the EC2 instance
            RunInstancesResult result = amazonEC2Client.runInstances(runInstancesRequest);

            // Get the result back
            System.out.println(result.toString());

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}