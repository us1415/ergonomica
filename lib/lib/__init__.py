"""
[lib/lib/__init__.py]

This module loads all commands from lib/lib into the 'verbs' dictionary for running.
"""

# lowcase is the standard in other files
# pylint: disable=invalid-name

verbs = {}

commands = ["bash", "cd", "clear", "cp", "echo", "edit", "ergo_help", "find",
            "fish", "get", "ls", "mkdir", "mv", "pwd", "python", "quit", "read",
            "rm", "set", "version", "whoami", "yes", "zsh", "string_find", "multiply",
            "length", "size", "swap", "free", "sort", "addline", "removeline", "users",
            "mkdir", "rmtree", "alias", "macro", "export", "load_config", "title", "ping",
            "equal", "nequal", "shuffle","license","list_modules","write",
           ]

for item in commands:
    if (item != "__init__.py") and (item[-4:] != ".pyc"):
        verbs.update(__import__('lib.lib.'+item, globals(), locals(), ['object'], 0).verbs)
