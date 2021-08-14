# Bulk File Rename

## Help
```bash
python bulk_rename.py -h
```

## RegEx Documentation
https://docs.python.org/3/library/re.html#regular-expression-syntax

## Example:
If we need to rename `ABCD_EURO_WW_MAP_77.jpg` -> `ABCD_WW_MAP_77_US.png`
```bash
python bulk_rename.py -r "(.*)(_EURO_)(.*)(_\d{2})(.*)" -n "\1_\3\4_US.png" -a
```
