#!/usr/bin/python

import email
import json
import socket
import sys

#hardcode everything for now
incoming = email.message_from_file(sys.stdin)

if incoming.is_multipart():
    payload = incoming.get_payload(0).get_payload(decode=True)
else:
    payload = incoming.get_payload(decode=True)

subj = incoming.get("Subject")
if subj == "irker json":
    decoded = json.loads(payload)
    targets = decoded["to"]
    message = decoded["privmsg"]
elif subj.startswith("irker: "):
    stripped = subj.lstrip("irker: ")
    targets = json.loads(stripped)
    message = payload
else:
    sys.exit(1)

if not isinstance(targets, list):
    targets = [targets]
irkermsg = json.dumps({ "to" : targets, "privmsg" : message})

for target in targets:
    # This list is what you want to configure
    if target not in ["irc://chat.freenode.net/##projectchannel", "irc://chat.freenode.net/#commits"]:
        sys.exit(1)
socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(irkermsg + "\n", ("localhost", 6659))

