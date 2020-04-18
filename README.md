Example:
```python __main__.py resources/input/16-4.txt resources/output/mbruncic-final.txt```

TODO:

- Single known difference with bash script is that disconnected logs have some 
information after duration. Example from bash: ``4h:50m:34s 284.76 127.27``, 
example from python: ``4h:50m:34s``
- `cleanup src.model.Log.Log#get_date`
- `cleanup src.model.Log.Log#get_hour`
- `cleanup src.model.Log.Log#get_description_without_spaces`
- output folder must exist, create folder if needed?

How to add new parser:
* just Add new class in ``src/parsing/impl`` package and implement all methods