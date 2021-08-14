# Bulk File Rename

## Help
```bash
python bulk_rename.py -h

usage: bulk_rename [-h] [-p PATH] [-r REGEX] [-n NEW] [-a]

Bulk File Rename

optional arguments:
  -h, --help  show this help message and exit
  -p PATH     Path to the folder with files to be renamed
  -r REGEX    Regular Expression
  -n NEW      Replace string
  -a          Apply changes
```

## RegEx Documentation
https://docs.python.org/3/library/re.html#regular-expression-syntax

## Example:
If we need to rename `ABCD_EURO_WW_MAP_77.jpg` -> `ABCD_WW_MAP_77_US.png`
```bash
python bulk_rename.py -r "(.*)(_EURO_)(.*)(_\d{2})(.*)" -n "\1_\3\4_US.png" -a
```
