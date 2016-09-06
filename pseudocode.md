```
initialize connections
get status of each connection from db
for each connection
     get current status of each connection
     check if status changed
     if change:
          check if count threshold for state change has been met
          if met:
               change state
               reset all counts for interface
               send alert to all stakeholders
          else
               increase count by one
               reset other count
          save new connection state in db
          save new counts in file
     else:
          reset all counts
          save new counts in db
     if status change in any connection:
          get all active connections
          prepare template based on connection combo
          overwrite tcrules
          restart shorewall
```
