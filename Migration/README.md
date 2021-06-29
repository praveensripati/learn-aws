# Migration to the AWS

Many are moving towards and some are moving away from the Cloud. This page is all about exploring the resources around to get started with the migration.

## Four Phases

    - PROJECT - Run small/trial projects/PoC to get familiar and experience the benefits of the Cloud
	
	- FOUNDATION - Setting Cloud Center of excellence, Creating accounts, forming Security and Compliance guidelines etc
	
	- MIGRATION - Migrate applications or entire data center to the Cloud
	
	- REINVENTION - Take advantage of flexibility of the Cloud for increasing the innovation, TTM etc.

## Migration Process

	- Phase 1 : MIGRATION PREPARATION AND BUSINESS PLANNING
		○ Business case, Identify the objectives and benefits

	- Phase 2 : PORTFOLIO DISCOVERY AND PLANNING
		○ Identify the applications and prioritize them

	- Phase 3 : DESIGNING, MIGRATING AND VALIDATING APPLICATIONS
		○ Start with less critical and easy to move applications towards critical and difficult to move applications

	- Phase 4: OPERATE
		○ Turn off old applications
		○ Improve people, process and technology

## Six Common Application Migration Strategies (6R's)

	1. Rehost (Lift and shift) - Applications are migrated as is without any changes to the Cloud. Virtual machines from VMware vSphere and Windows Hyper-V. AWS SMS (Service Migration Service) can be used.
	
	2. Replatform (Lift, tinker and shift) - A few cloud optimizations are performed without changing the core architectures of the applications. May be use RDS, Elastic Bean Stalk.
	
	3. Repurchase - Move to a different product or upgrading to a newer version, involves change in the existing license model.
	
	4. Refactor/Rearchitect - For ex, moving to SOA or Containers. Mainly driven by a strong business need to add features, scale, or performance that would otherwise be difficult to achieve in the application’s existing environment.
	
	5. Retire
	
	6. Retain - keep the application as-is, because maybe of the criticality, budget etc.

## AWS Services to help with Server and Database Migration

	- AWS SMS (Server Migration Service) - Virtual machines from VMware vSphere and Windows Hyper-V.
	
	- AWS DMS (Database Migration Service)
	
	- VMWare Cloud on AWS - seamlessly migrate and extend their on-premises VMware vSphere-based environments to the AWS Cloud running on next-generation Amazon Elastic Compute Cloud (Amazon EC2) bare metal infrastructure.

    - Data Migration
        - S3 Transfer Acceleration
        - Snowball
        - SnowMobile
        - DirectConnect (Uses Direct Connect Locations)
        - Kinesis Firehose
        - edynamo

# Further Reading

1. General Migration
	- https://aws.amazon.com/cloud-migration/

1. AWS Services around Migration
	- https://aws.amazon.com/cloud-data-migration/
	- https://aws.amazon.com/dms/
	- https://aws.amazon.com/server-migration-service/

1. How does migration work from Mainframes to Cloud?
	- https://aws.amazon.com/blogs/apn/migrating-a-mainframe-to-aws-in-5-steps/
	- https://aws.amazon.com/blogs/enterprise-strategy/yes-you-should-modernize-your-mainframe-with-the-cloud/

1. Papers
	- https://www.infosys.com/modernization/insights/Pages/accelerate-mainframe-migration-aws.aspx

1. How to Migrate your Virtual Machines to AWS using the AWS Server Migration Service
	- https://www.youtube.com/watch?v=_SpRpC2Ez9c

# VS

1. Choosing a Rehost Migration Tool – CloudEndure or AWS SMS
	- https://aws.amazon.com/blogs/architecture/field-notes-choosing-a-rehost-migration-tool-cloudendure-or-aws-sms/