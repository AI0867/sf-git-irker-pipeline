Sourceforge git-irker pipeline
==============================

A set of tools that get commit notifications from a sourceforge-hosted git repository to an external [irker](http://www.catb.org/~esr/irker/) instance.
The regular TCP/UDP transmission cannot be used because sourceforge doesn't give hooks network access.

All configuration is hardcoded.

## Files

### update
A feature-poor reimplementation of irkerhook.py that is compatible with python 2.4 and sends its notifications through email instead of TCP or UDP. Can simply be dumped into the hooks dir of a git repository.

Since 1.21, irkerhook.py also has this functionality using the 'email' variable, so you should use that instead of this script.

### procmailrc.sample
Sample .procmailrc for the server that receives the emails. Filters the relevant emails and passes them to irker-mailfilter.py.

### irker-mailfilter.py
Checks the target channels against a whitelist, then passes on the payload to the local irker instance.

## Protocol
The receiving end supports two protocols. irkerhook.py uses the standard one, while 'update' uses the legacy kind.

### legacy
The subject is 'irker: ' followed by a pseudo-JSON list of targets.
The body is the message irker should send.

The reason for this format was that building a message of this type does not require a JSON library.

Example:

    From: someone@users.sourceforge.net
    Subject: irker: ["irc://chat.freenode.net/#commits", "irc://chat.freenode.net/##irkertest"]

    test message

### standard
The subject is 'irker json'.
The body is a regular irker JSON blob.

Example:

    From: someone@users.sourceforge.net
    Subject: irker json

    {"to":["irc://chat.freenode.net/#commits", "irc://chat.freenode.net/##irkertest"], "privmsg":"test message"}
