# Kubernetes 
Tip of the day: Learning with a group of people is fun, if you can find a study buddy! 



## Tldr

A quick cheat sheet


## Theory
Lets spit out some theory

1. High-level overview of Kubernetes components:

```
    +-----------------+       +-----------------+        +-----------------+
    | Control Plane   |       | Node 1          |        | Node 2          |
    |                 |       |                 |        |                 |
    | +-------------+ |       | +-----------+   |        | +-----------+   |
    | | API Server  | |       | | Kubelet   |   |        | | Kubelet   |   |
    | +-------------+ |       | +-----------+   |        | +-----------+   |
    | +-------+-------+ |       | +-----------+   |        | +-----------+   |
    | | etcd  | |       | | Kube-proxy |   |        | | Kube-proxy |   |
    | +-------+ |       | +-----------+   |        | +-----------+   |
    | +-------------+ |       | +------+      |        | +------+      |
    | | Controller  | |       | | Pod  |      |        | | Pod  |      |
    | | Manager     | |       | +------+      |        | +------+      |
    | +-------------+ |       +-----------------+        +-----------------+
    | +-------------+ |
    | | Scheduler   | |
    | +-------------+ |
    +-----------------+
```


1. Cluster: A Kubernetes cluster consists of a control plane and multiple worker nodes. The control plane is responsible for managing the overall state of the cluster, while the worker nodes run containerized applications.

2. Control Plane: The control plane components include the kube-apiserver, etcd, kube-controller-manager, and kube-scheduler. These components work together to ensure the desired state of the cluster is maintained and to manage the communication between nodes.

3. Kube-apiserver: This component exposes the Kubernetes API, allowing users and other components to interact with the cluster. It validates and processes RESTful API requests and updates the corresponding objects in etcd.

4. Etcd: A distributed key-value store used by Kubernetes to store all the configuration data and state information of the cluster. It is critical for maintaining the consistency and reliability of the cluster data.

5. Kube-controller-manager: This component runs various controllers that handle different aspects of the cluster, such as managing nodes, replicating pods, and handling failures. Controllers watch for changes in the cluster state and work to maintain the desired state.

6. Kube-scheduler: The scheduler is responsible for deciding which nodes should run newly created pods. It takes into account factors like resource availability, node affinity, and anti-affinity rules, and other constraints.

7. Node: Each node in the cluster runs a kubelet, kube-proxy, and a container runtime like Docker or containerd. Nodes are responsible for running pods and providing the necessary resources for containers to function.

8. Kubelet: The kubelet is an agent that runs on each node, ensuring that containers are running in a pod and reporting their status to the control plane. It communicates with the kube-apiserver to ensure the desired state of the pod is maintained.

9. Kube-proxy: Kube-proxy runs on each node, maintaining network rules and enabling communication between pods and services within the cluster. It also handles load balancing for services.

10. Pod: A pod is a group of one or more containers that share the same network namespace and storage volumes. Pods are the smallest deployable units in Kubernetes and can be scaled horizontally to handle increased load.

11. Service: Services provide a stable IP address and DNS name that abstract away the backend pods, making it easy to discover and access pods in a load-balanced manner.

12. Deployment: Deployments are higher-level abstractions that manage the deployment, scaling, and rolling updates of containerized applications. They ensure the desired number of replicas for a pod are running and can automatically recover from failures.

13. ConfigMap & Secret: ConfigMaps and Secrets are used to separate configuration data and sensitive data from the container images. They can be mounted as files or environment variables in a pod.

14. Volume: Volumes provide a way to store data outside of the container's filesystem, ensuring data persists beyond the life of the pod. Kubernetes supports various types of volumes, including local storage and network-attached storage.

15. Ingress: Ingress objects define rules for external access to services within the cluster. Ingress controllers, like NGINX or HAProxy, implement these rules and provide load balancing, SSL termination, and name-based virtual hosting.


## Resources 
- https://learnk8s.io/ - Awesome PDF's and printable cheatsheets but very expensive. 