# commander-llama
A command line AI assistant for Linux utilities

Sometimes you need help putting together a Linux command line to accomplish something.  Of course you can just Google it, or you could type a question into an AI web page, but since you are already staring at a terminal trying to think of the command, wouldn't it be more convenient to just type out what you need a command to do and get the answer right there?
This utility will attempt to do that, but be advised that the answers come from an LLM, and therefore you are responsible for verifying the commands before executing them.  The answers are merely tokens predicted by an LLM and they may be what you need, or if you are not careful, running the command could do harm to your data or your system.  The cmdr_llama.py only prints the command and does not execute it.  It is up to you to decide whether to run the command that is printed and I am not responsible for the consequences of that decision.  
For example:
```bash
$ cmdr_llama I need a command to find all files in a given directory and delete them if they are more than 7 days old
find /path/to/directory -type f -mtime +7 -exec rm {} \;
```
