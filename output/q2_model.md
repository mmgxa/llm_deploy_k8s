```
Name:             model-server-7f9b678b7-zfv62
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 03 Oct 2023 06:39:27 +0000
Labels:           app=model-server
                  pod-template-hash=7f9b678b7
Annotations:      <none>
Status:           Running
IP:               10.244.0.9
IPs:
  IP:           10.244.0.9
Controlled By:  ReplicaSet/model-server-7f9b678b7
Containers:
  model-server:
    Container ID:   docker://fab05dce869ba086164bf5cf7392a471d04ad3f8f68431517341b02fa089be75
    Image:          model-server:latest
    Image ID:       docker://sha256:89e976532dff7a7a3abab921f199c62b9c590b1f1dbe0a13cb50087cc58a7d94
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 03 Oct 2023 06:42:30 +0000
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     4
      memory:  2Gi
    Requests:
      cpu:     4
      memory:  2Gi
    Environment:
      REDIS_HOST:      <set to the key 'hostname' of config map 'redis-config'>         Optional: false
      REDIS_PORT:      <set to the key 'port' of config map 'redis-config'>             Optional: false
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret'>          Optional: false
      HF_MODEL:        <set to the key 'hf_model' of config map 'model-server-config'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-hr8wx (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-hr8wx:
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
  Normal   Scheduled          23m                 default-scheduler  Successfully assigned default/model-server-7f9b678b7-zfv62 to minikube
  Warning  Failed             21m (x12 over 23m)  kubelet            Error: ErrImageNeverPull
  Warning  ErrImageNeverPull  21m (x13 over 23m)  kubelet            Container image "model-server:latest" is not present with pull policy of Never
```
