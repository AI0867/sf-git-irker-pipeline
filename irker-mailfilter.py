#!/usr/bin/python

import email
import json
import socket
import sys

incoming = email.message_from_file(sys.stdin)
#hardcode everything for now
subj = incoming.get("Subject")
if not subj.startswith("irker: "):
	sys.exit(1)
stripped = subj.lstrip("irker: ")
targets = json.loads(stripped)
if incoming.is_multipart():
	payload = incoming.get_payload(0).get_payload(decode=True)
else:
	payload = incoming.get_payload(decode=True)
for target in targets:
	if target not in ["irc://chat.freenode.net/##projectchannel", "irc://chat.freenode.net/#commits"]:
		sys.exit(1)
irkermsg = json.dumps({ "to" : targets, "privmsg" : payload })
socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(irkermsg + "\n", ("localhost", 6659))

