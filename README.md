Script to monitor all WAN lines and connect/disconnect to firewall when any status change occurs. Implemented by rewriting tcrules file of shorewall on every run.

- Disconnect line if down for more than x seconds
- Connect line back if up for more than y seconds
- Send alert to alert group



