Sourceforge git-irker pipeline
==============================

A set of tools that get commit notifications from a sourceforge-hosted git repository to an external irker instance.
The regular irkerhook.py cannot be used in its current form because sourceforge doesn't give hooks network access and provides python 2.4 instead of something modern.

All configuration is hardcoded.

update
------
A feature-poor reimplementation of irkerhook.py that is compatible with python 2.4 and sends its notifications through email instead of TCP or UDP. Can simply be dumped into the hooks dir of a git repository.
Future work should probably be merging it back into irkerhook.py.

procmailrc.sample
-----------------
Sample .procmailrc for the server that receives the emails. Filters the relevant emails and passes them to irker-mailfilter.py.

irker-mailfilter.py
-------------------
Checks the target channels against a whitelist, then passes on the payload to the local irker instance.
