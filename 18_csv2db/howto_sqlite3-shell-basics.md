`sqlite <filename>`:
- If a filename is provided:
    - If existing, executes program
    - If not existing, creates file
- If filename is not provided,
    - Creates temporary file

`SQLite Commands`:
- A semicolon is mandatory at the end of each line.
- `Ctrl + C` interrupts the SQL program. Stops but does not exits SQL.
- `Ctrl + D` terminates the SQL program. Exits SQL.

> A SQL program requires a database to read from. 
- Opening SQL from the application icon will not provide a database to read from.
    - You can still provide a database though! Using the command `.open <FILENAME>` immediately after SQL opens will make this `FILENAME` the reference database (recommended )

