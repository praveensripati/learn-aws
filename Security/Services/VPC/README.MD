# Virtual Private Cloud

VPC is nothing more than a **logically isolated network**. Any resource like an EC2 in a VPC by default won't be able to talk to another VPC, unless we setup [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) across them. VPC can bes used to isolate Prod/Dev environments, Applications, Customers etc.

VPC spans within a region, Subnet spans within a Availability Zone. When you create a VPC, it spans all the Availability Zones in the region. After creating a VPC, you can add one or more subnets in each Availability Zone.

## Creating a VPC and EC2 in private/public subnets using the wizard

1. Create a VPC (Public) using Wizard.
	- Navigate to the VPC Management Console (https://console.aws.amazon.com/vpc/home?region=us-east-1)
	- Create an `Elastic IP`.
	- Click on `Launch VPC Wizard` in the `VPC Dashboard`.
	- Select `VPC with Public and Private Subnets`. Click on `Select`.
	- Give the VPC, Public and Private Subnet a name.
	- Select the `Elastic IP`.
	- Click on `Create VPC`.

## Creating a VPC and EC2 in private/public subnets manually

1. Create VPC (VPC 10.0.0.0/16 - Subnet 10.0.1.0/24 and 10.0.2.0/24)

1. Automatically a route table, Security Group, Network ACL are created

1. Create two subnet (private and public) in different Availability Zones in the same region
	- Enable auto assign public ip for the Public subnet

1. Create an Internet Gateway and attach it to a VPC (only one can be attached)

1. Create a Route Table (they are associated with the subnets)
	- Don't change the main route table as it is attached to all the subnets
	- Create a route out to the internet with destination as 0.0.0.0/0 and target as internet gateway
	- Associate the Route Table with the Public subnet

1. Deploy Ubuntu EC2 in the Public (webserver) and Private (database server) subnets.

1. Install WebServer on the instance in the Public subnet.

1. SSH into the EC2 in the Public Subnet and perform the below steps.
	- ping to the database server (ICMP has to be included in the Security Group) to check the connectivity
	- Copy the pem file (KeyPair) to the EC2 in the Public Subnet
	- `chmod 600` to the above file
	- SSH into the database server
		- Try connecting to the internet (ping). It would fail as the NAT Gateway has not been configured yet.
 
1. Create an Elastic IP and then create a NAT Gateway.
	- Specify the Public subnet.

1. Edit the main route table
	- Add a route -- destination is 0.0.0.0/0 and target is NAT Gateway.
	- Try installing MySQL (apt-get install mysql-server) on the EC2 in the Private subnet.

## Steps for Peering across VPCs

1. Create a VPC (Public) using Wizard.
	-  Select the PublicSubnet.
	-  Actions -> Modify auto-assign IP settings
	-  Select "Enable auto-assign public IPv4 address"

1. Create one EC2 instance in the Public Subnet in the default VPC and another EC2 instance in the VPC created in the previous step.
	-  Note that  a new Security Group has to be created for the new VPC, as the Security Groups are VPC specific.
	-  Login to both the instances via Putty.
	-  Make sure to add "All ICMP - IPv4" protocol in the Security Group to allow testing through Ping.

1. Go to the VPC Management Console and go to the "Peering Connections" Tab.
	-  Click on "Create Peering Connection"
	-  Enter the name
	-  Select the requester as the Default VPC.
	-  Select the accepter as the newly created VPC.
	-  Click on "Create Peering Connection"
	-  The status of the VPC Peering will be in a "Pending Acceptance" status.
	-  Select the VPC and select "Actions -> Accept Request". Now the status should change to Active.

1. Check if the ping is working from one EC2 to other using the Private IP address. It should not work as the routing tables have not been configured between the two VPC.

	- Note down the CIDR for both the VPC
    - The following should be performed for both the EC2 instances.
        - Select the EC2 instance.
        - Identify the Subnet for the above EC2 and select it.
        - Identify the Routing Table for above Subnet and select it.
        - Click on Route and edit it.
        - Add the missing VPC CIDR destination and target as the earlier created VPC peering.
	- Now the ping should work from both the EC2 using the private IP address as the peering has been properly established.

1. If the Ping works make sure to delete all the resources created earlier including the Elastic IP.

## Steps for deleting the VPC
1. Terminate the EC2
1. Delete the Peering connections
1. Delete the NAT Gateway
1. Wait for a few Minutes
1. Delete ElasticIP
1. Finally delete the VPC

# Further Reading

1. Enabling New SaaS Strategies with AWS PrivateLink
	- https://aws.amazon.com/blogs/apn/enabling-new-saas-strategies-with-aws-privatelink/

1. Control access to services with VPC endpoints
	- https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html

1. Interface endpoint properties and limitations
	- https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations

1. NAT Instance vs Gateway
    - https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html

1. Data Transfer Pricing
    - https://www.apptio.com/emerge/aws-data-transfer-costs/
    - https://aws.amazon.com/ec2/pricing/on-demand/

1. What is the least CIDR that we can use in AWS VPC?
    - https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#VPC_Sizing

1. VPC Resize
    - https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#vpc-resize

1. Default VPC and default subnets
	- https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html

1. Traffic Mirroring
	- https://aws.amazon.com/blogs/aws/new-vpc-traffic-mirroring/

1. Transit Gateway (a better alternate to VPC Peering)
	- https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html
	- https://aws.amazon.com/blogs/networking-and-content-delivery/migrate-from-transit-vpc-to-aws-transit-gateway/
	- https://aws.amazon.com/blogs/aws/new-use-an-aws-transit-gateway-to-simplify-your-network-architecture/
	- https://www.youtube.com/watch?v=yQGxPEGt_-w/

1. VPC Flow Logs
	- https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html
	- https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-fields

1. Different ways of connecting the on-premise network to the AWS network
     - https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html

1. How Netflix is able to enrich VPC Flow Logs at Hyper Scale to provide Network Insight
    - https://netflixtechblog.com/hyper-scale-vpc-flow-logs-enrichment-to-provide-network-insight-e5f1db02910d