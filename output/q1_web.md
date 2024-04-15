```
Name:                   web-server
Namespace:              default
CreationTimestamp:      Tue, 03 Oct 2023 06:39:28 +0000
Labels:                 app=web-server
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               app=web-server
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=web-server
  Containers:
   web-server:
    Image:      web-server:latest
    Port:       80/TCP
    Host Port:  0/TCP
    Limits:
      cpu:     500m
      memory:  200Mi
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config'>                 Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config'>                     Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret'>                  Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-server-config'>  Optional: false
    Mounts:              <none>
  Volumes:               <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   web-server-bc7c498f8 (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  23m   deployment-controller  Scaled up replica set web-server-bc7c498f8 to 1
```
