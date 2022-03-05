# python-get-absolute-resource-path
Get absolute resource path of exterior package

## Setup
```pip3 install git+https://github.com/yjg30737/python-get-absolute-resource-path.git --upgrade```

## Description
There is only one method. ```get_absolute_resource_path(res: str) -> str```.

This package find the module in the stack which includes relative resource path like 'ico/sample.png'. You can get the absolute path like C:/.../sample_exists_directory/ico/sample.png

### Example
```python
print(get_absolute_resource_path('ico/dark-notepad.svg')) # C:/.../ico_dark_notepad_exists_directory/ico/dark-notepad.svg
```
