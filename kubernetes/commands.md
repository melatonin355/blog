# Kubernetes Cheat Sheet

## CREATE

| Resource   | Command                                            |
|------------|----------------------------------------------------|
| Pod        | `kubectl run <name> --image=<container-image>`     |
| Deployment | `kubectl create deployment <name> --image=<image>` |
| Service    | `kubectl expose <resource> <name> --port=<port>`   |
| Ingress    | Create an Ingress YAML and apply with `kubectl apply -f <ingress.yaml>` |

## INSPECT

| Resource   | Command                                  | Command (get)                  | Command (describe)                  |
|------------|------------------------------------------|---------------------------------|-------------------------------------|
| Pod        |                                          | `kubectl get pods`             | `kubectl describe pod <pod-name>`   |
| Deployment |                                          | `kubectl get deployments`      | `kubectl describe deployment <name>`|
| Service    |                                          | `kubectl get services`         | `kubectl describe service <name>`   |
| Ingress    |                                          | `kubectl get ingress`          | `kubectl describe ingress <name>`   |
| Node       |                                          | `kubectl get nodes`            | `kubectl describe node <node-name>` |

## DEBUG

### Pod

| Action                               | Command                                          |
|--------------------------------------|--------------------------------------------------|
| Inspect the logs                     | `kubectl logs <pod-name>`                        |
| Inspect logs of a previous container | `kubectl logs <pod-name> --previous`            |
| Interactive shell access             | `kubectl exec -it <pod-name> -- bash`           |
| Port forward                         | `kubectl port-forward <podname> 8080:<cont-port>`|
| Delete a pod                         | `kubectl delete pod <pod-name>`                  |

### Deployment

| Action                                   | Command                                      |
|------------------------------------------|----------------------------------------------|
| Scale a deployment                       | `kubectl scale deployment <name> --replicas=<count>`|
| Update a deployment's image              | `kubectl set image deployment/<name> <container-name>=<new-image>` |
| Rollout history                          | `kubectl rollout history deployment/<name>`  |
| Rollback to a previous revision          | `kubectl rollout undo deployment/<name> --to-revision=<revision-number>` |
| Delete a deployment                      | `kubectl delete deployment <name>`           |

### Service

| Action                                       | Command                                             |
|----------------------------------------------|-----------------------------------------------------|
| Connect to a service                         | `kubectl port-forward service/<name> 8080:<service-port>` |
| Inspect endpoints                            | `kubectl describe service <name> \| grep Endpoint` |
| Delete a service                             | `kubectl delete service <name>`                     |

### Ingress

| Action                       | Command                                  |
|------------------------------|------------------------------------------|
| Inspect the ingress manifests| `kubectl get ingress`                    |
| Retrieve the YAML for ingress| `kubectl get ingress <name> -o yaml`     |
