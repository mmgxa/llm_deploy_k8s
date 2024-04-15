```
Name:             web-server-ingress
Labels:           <none>
Namespace:        default
Address:          192.168.49.2
Ingress Class:    nginx
Default backend:  <default>
Rules:
  Host                                 Path  Backends
  ----                                 ----  --------
  secure-evident-hyena.ngrok-free.app  
                                       /   web-server-service:8000 (10.244.0.10:80)
Annotations:                           <none>
Events:
  Type    Reason  Age                From                      Message
  ----    ------  ----               ----                      -------
  Normal  Sync    16m (x3 over 23m)  nginx-ingress-controller  Scheduled for sync
```
