# Pulumi

- https://www.youtube.com/watch?v=RaoKcJGchKM Chef vs ansible vs puppet vs terraform vs crossplane vs pulumi 


Pulumi is an open-source infrastructure as code (IaC) tool that allows you to define and manage your cloud infrastructure using familiar programming languages like Python, JavaScript, and Go. Here are the basic steps to get started:

1. Install Pulumi - Pulumi provides installation packages for various operating systems. You can download and install Pulumi by following the instructions here: https://www.pulumi.com/docs/get-started/install/

2. Configure Pulumi - After installing Pulumi, you need to configure it to connect to your cloud provider account. Pulumi supports several cloud providers, including AWS, Azure, GCP, and Kubernetes. You can configure Pulumi using the CLI command `pulumi login`. This command will prompt you to log in to your cloud provider account and authenticate your Pulumi CLI.

3. Create a Pulumi project - Once Pulumi is configured, you can create a new project using the `pulumi new` command. This command will create a new directory with all the necessary files and configurations for your Pulumi project.

4. Write infrastructure code - In Pulumi, you write infrastructure code using your preferred programming language. For example, if you are using Python, you would write Python code to create and manage your cloud resources. You can find examples of Pulumi code in the Pulumi documentation.

5. Deploy your infrastructure - After writing your infrastructure code, you can deploy it to your cloud provider using the `pulumi up` command. This command will create or update your cloud resources based on your infrastructure code.

Pulumi Cheat Sheet:

- `pulumi new` - create a new Pulumi project
- `pulumi stack init` - initialize a new stack in the current project
- `pulumi config set KEY VALUE` - set a configuration value for the current stack
- `pulumi up` - deploy the current stack
- `pulumi destroy` - destroy all resources in the current stack
- `pulumi stack select STACK_NAME` - select a different stack
- `pulumi login` - log in to your cloud provider account
- `pulumi preview` - preview the changes that will be made by a `pulumi up` command without actually making any changes
- `pulumi refresh` - refresh the current stack's state from the cloud provider
- `pulumi stack ls` - list all available stacks in the current project


**Python** 
```python
import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
```


**Yaml**

```yaml
name: quickstart
runtime: yaml
description: A minimal AWS Pulumi YAML program

resources:
  # Create an AWS resource (S3 Bucket)
  my-bucket:
    type: aws:s3:Bucket

outputs:
  # Export the name of the bucket
  bucketName: ${my-bucket.id}
```

**Golang**

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an AWS resource (S3 Bucket)
        bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
        if err != nil {
            return err
        }

        // Export the name of the bucket
        ctx.Export("bucketName", bucket.ID())
        return nil
	  })
}
```