# IAM NOTES
```
+--------------------------------------------------+
|                  AWS Account                     |
|    +---------------------------------------+    |
|    |             IAM Service               |    |
|    |    +------+     +------+     +-----+ |    |
|    |    | User |     | Role |     |Group| |    |
|    |    +-+----+     +-+----+     +-+---+ |    |
|    |      |             |             |     |    |
|    |    +-v------------v-------------v-+   |    |
|    |    |        IAM Policies           |   |    |
|    |    +-------------------------------+   |    |
|    +---------------------------------------+    |
|                                                  |
|    +---------------------------------------+    |
|    |            AWS Resources             |    |
|    |   +-----+     +-----+     +-----+    |    |
|    |   | EC2 |     | S3  |     | RDS |    |    |
|    |   +-----+     +-----+     +-----+    |    |
|    +---------------------------------------+    |
+--------------------------------------------------+
```


```
+------------------------------------------+
|              AWS Account                 |
|  +-----------------------------------+   |
|  |              IAM                   |   |
|  |    +------+    +------+    +-----+ |   |
|  |    | User |    | Role |    |Group| |   |
|  |    +-+-+--+    +-+-+--+    +-+-+-+ |   |
|  |      | |         | |          | |   |   |
|  | +----+ +-----+   | |          | |   |   |
|  | | User Policy |  | |          | |   |   |
|  | +-------------+  | |          | |   |   |
|  |                  | |          | |   |   |
|  | +----------------+ +-------+  | |   |   |
|  | | Role Policy              |  | |   |   |
|  | +--------------------------+  | |   |   |
|  |                               | |   |   |
|  | +-----------------------------+ +--+ |   |
|  | | Group Policy                    | |   |
|  | +---------------------------------+ |   |
|  +-----------------------------------+   |
+------------------------------------------+
```

**1. IAM Users**
- IAM users are AWS's primary mechanism for granting access to resources.
- Each user has security credentials that can be used to access AWS resources, including a user name and password for AWS Management Console access and an access key ID and secret access key for API, CLI, SDK, and other development tool access.

**2. IAM Roles**
- IAM roles are temporary security tokens that you can use to authenticate services and users to access resources.
- IAM roles can be assumed by trusted entities, such as IAM users, applications, or AWS services like EC2.

**3. IAM Policies**
- Policies define permissions in AWS. They are JSON documents that, when attached to identities or resources, define their permissions.
- IAM policies can be used to grant and limit access to the resources in your environment.
- IAM supports different types of policies: Identity-based policies, Resource-based policies, Permissions boundaries, Organizations SCPs, Access control lists (ACLs), and Session policies.

**4. IAM Groups**
- IAM groups are collections of IAM users. 
- You can use groups to specify permissions for a collection of users, which can make those permissions easier to manage for those users.

**5. Multi-Factor Authentication (MFA)**
- For an additional layer of security, you can enable MFA for your IAM users to protect your resources.
- MFA requires users to present two separate forms of identification: their password and a code from an MFA device.

**6. IAM Best Practices**
- Grant least privilege: Only give necessary permissions to perform a task.
- Use groups to assign permissions to IAM users.
- Regularly rotate security credentials.
- Enable MFA for privileged users.
- Use IAM roles for applications running on EC2 instances to make calls to AWS services.
- Use policy conditions for extra security. For example, you can add a condition to deny access if MFA is not enabled.

**7. IAM for Networking**
- VPC Flow Logs can be delivered to an Amazon S3 bucket or to Amazon CloudWatch Logs, based on IAM roles.
- Amazon Route 53 Resolver rules can be shared with other accounts using IAM policies.
- IAM policies can control access to your Amazon VPCs and Amazon VPC resources.
- IAM roles can be used to delegate permissions to create and manage VPC resources.


### authorization, authentication, and identity management (IDP) 

```
+---------------------------------------------+
|             Identity Provider (IdP)         |
|     +---------+     +---------+             |
|     | User 1 |     | User 2 |             |
|     +----+----+     +----+----+            |
|          |               |                 |
|     +----v----+     +----v----+            |
|     |Credentials|   |Credentials|          |
|     +----+----+     +----+----+            |
|          |               |                 |
+---------------------------------------------+
             |               |
             v               v
+---------------------------------------------+
|              Authentication                  |
|     +---------+     +---------+             |
|     | Verify  |     | Verify  |             |
|     | User 1  |     | User 2  |             |
|     +----+----+     +----+----+            |
|          |               |                 |
+---------------------------------------------+
             |               |
             v               v
+---------------------------------------------+
|              Authorization                  |
|     +-----------+    +-----------+          |
|     |Permissions|    |Permissions|          |
|     |  for User1|    | for User2 |          |
|     +-----------+    +-----------+          |
+---------------------------------------------+

```

**1. Authentication**
   - Authentication is the process of verifying who a user is.
   - In AWS, IAM users authenticate by providing their credentials (username and password for AWS Management Console, access key ID and secret access key for AWS CLI, SDKs, or API operations).
   - Multi-Factor Authentication (MFA) can be used for additional security.

**2. Authorization**
   - Authorization is the process of verifying what a user is allowed to do.
   - In AWS, this is handled via IAM policies, which are attached to IAM users, groups, or roles.
   - Policies are JSON documents that define permissions, specifying who (Principal) is allowed to perform what action (Action) on which resource (Resource), and under what conditions (Condition).

**3. Identity Management (Identity Provider - IDP)**
   - An identity provider (IdP) is a service that stores and verifies user identity.
   - IAM can integrate with external identity providers (such as Microsoft Active Directory) via federation, allowing external user identities to be used in AWS.
   - AWS also offers AWS Directory Service and Amazon Cognito for identity management.

