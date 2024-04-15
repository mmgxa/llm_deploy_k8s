```
Name:             web-server-bc7c498f8-rz4x6
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 03 Oct 2023 06:39:28 +0000
Labels:           app=web-server
                  pod-template-hash=bc7c498f8
Annotations:      <none>
Status:           Running
IP:               10.244.0.10
IPs:
  IP:           10.244.0.10
Controlled By:  ReplicaSet/web-server-bc7c498f8
Containers:
  web-server:
    Container ID:   docker://1c652cc7c02e04148cbb2ddf45ceea5312be56487c9ca5c83030e6bfb0183b0c
    Image:          web-server:latest
    Image ID:       docker://sha256:24e04a1f0f883a6ad0cb97dfcf797318ec3b63105085c0965bb622999c9e0117
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 03 Oct 2023 06:42:08 +0000
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  200Mi
    Requests:
      cpu:     500m
      memory:  200Mi
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config'>                 Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config'>                     Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret'>                  Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-server-config'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6bt4v (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-6bt4v:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason             Age                 From               Message
  ----     ------             ----                ----               -------
  Normal   Scheduled          23m                 default-scheduler  Successfully assigned default/web-server-bc7c498f8-rz4x6 to minikube
  Warning  Failed             21m (x12 over 23m)  kubelet            Error: ErrImageNeverPull
  Warning  ErrImageNeverPull  21m (x13 over 23m)  kubelet            Container image "web-server:latest" is not present with pull policy of Never
```
