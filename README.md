Example:
```python __main__.py resources/input/16-4.txt resources/output/mbruncic-final.txt```

TODO:

- `cleanup src.model.Log.Log#get_date`
- `cleanup src.model.Log.Log#get_hour`
- `cleanup src.model.Log.Log#get_description_without_spaces`
- output folder must exist, create folder if needed?

How to add new parser:
* just Add new class in ``src/parsing/impl`` package and implement all methods