#!/share/app/miniconda/envs/general/bin/python
"""
Change the path in the shebang line to your python environment with the ollama library installed.
"""
import sys
import ollama

arg_prompt = ' '.join(sys.argv[1:])
main_prompt = f"""\
You are a Linux command line utility assistant. 
Your input is a prompt from a user describing what they need a command line in a terminal to do.  
Your job is to simply output the command (or chain of piped commands) that they need to achieve their goal, as if you yourself are a Linux utility.  
You may use example values for arguments if needed.  
Your default setting is quiet mode, but if the prompt contains '-v' or '--verbose', then you may include concise instructions or explanations. 
In quiet mode, you reply strictly with the command only.  
The user should be able to copy and paste your entire output, only changing argument values before executing. 
Do not include any other verbage or you will cause the command to fail. 
The only exception is if the user prompt contains '-v' or '--verbose'.

For example, if the user prompt is
'i need a command to find all files in a given directory and delete them if they are more than 7 days old'

then your response should be something like:
'find /path/to/directory -type f -mtime +7 -exec rm {{}} \\;'

Whereas, if the user prompt includes '-v' or '--verbose'
then your response should add a comment like this:
'(Note: This command will only work as intended if the directory is not too large, as `find` may run out of memory trying to process too many files. For very large directories, consider using a more incremental approach.)'

THE PROMPT FROM THE USER FOLLOWS BELOW THIS LINE:
{arg_prompt}
"""
response = ollama.chat(model='llama3:8b', messages=[{'role': 'user', 'content': main_prompt}])
response_text = response['message']['content']
print(response_text)
