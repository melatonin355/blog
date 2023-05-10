Crossplane is an open-source infrastructure-as-code (IaC) platform that enables you to manage and provision infrastructure, services, and applications across a wide range of providers, including cloud providers like AWS, GCP, Azure, and others.



**Installation**

1. Install Crossplane CLI
```
curl -sL https://raw.githubusercontent.com/crossplane/crossplane/master/install.sh | sh
```

1. Install Crossplane into your Kubernetes cluster
```
kubectl crossplane install --version stable
```

**Provider Installation and Configuration**

1. Install a Provider (AWS example)
```
kubectl crossplane install provider crossplane/provider-aws:v0.19.0
```

2. Create a Provider Secret (AWS example)
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: aws-creds
  namespace: crossplane-system
type: Opaque
data:
  credentials: BASE64ENCODED_AWS_CREDS
```

3. Create a Provider Config (AWS example)
```yaml
apiVersion: aws.crossplane.io/v1beta1
kind: ProviderConfig
metadata:
  name: default
spec:
  credentials:
    source: Secret
    secretRef:
      namespace: crossplane-system
      name: aws-creds
      key: credentials
```

**Resource Management**

1. Define an Infrastructure Resource (AWS RDS example)
```yaml
apiVersion: database.aws.crossplane.io/v1beta1
kind: RDSInstance
metadata:
  name: sample-rds
spec:
  forProvider:
    dbInstanceIdentifier: sample-rds
    masterUsername: masteruser
    allocatedStorage: 20
    engine: mysql
    engineVersion: "5.6.35"
    skipFinalSnapshotBeforeDeletion: true
    deletionPolicy: Delete
  providerConfigRef:
    name: default
```

2. Define a Claim for the resource
```yaml
apiVersion: database.crossplane.io/v1alpha1
kind: MySQLInstance
metadata:
  name: sample-mysql-claim
spec:
  engineVersion: "5.6"
  storageGB: 20
  writeConnectionSecretToRef:
    name: mysql-secret
```

3. Bind the claim to the resource
```yaml
apiVersion: database.crossplane.io/v1alpha1
kind: MySQLInstance
metadata:
  name: sample-mysql-claim
spec:
  resourceRef:
    apiVersion: database.aws.crossplane.io/v1beta1
    kind: RDSInstance
    name: sample-rds
  writeConnectionSecretToRef:
    name: mysql-secret
```

**Uninstall Crossplane**
```
kubectl crossplane uninstall
```

