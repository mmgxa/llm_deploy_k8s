```
Name:                   model-server
Namespace:              default
CreationTimestamp:      Tue, 03 Oct 2023 06:39:27 +0000
Labels:                 <none>
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               app=model-server
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=model-server
  Containers:
   model-server:
    Image:      model-server:latest
    Port:       80/TCP
    Host Port:  0/TCP
    Limits:
      cpu:     4
      memory:  2Gi
    Environment:
      REDIS_HOST:      <set to the key 'hostname' of config map 'redis-config'>         Optional: false
      REDIS_PORT:      <set to the key 'port' of config map 'redis-config'>             Optional: false
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret'>          Optional: false
      HF_MODEL:        <set to the key 'hf_model' of config map 'model-server-config'>  Optional: false
    Mounts:            <none>
  Volumes:             <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   model-server-7f9b678b7 (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  23m   deployment-controller  Scaled up replica set model-server-7f9b678b7 to 1
```
