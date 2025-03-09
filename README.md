# Netbox Better Templates Plugin
Adds some functionality to netbox templates and config render.
The plugin uses `Monkey-patching` and injects extensions into the netbox render method.

## Added Functions

- **datetime**: adds datetime to config templates.
```jinja3
{{ datetime.now() }}
```

- **now**: standard now function of datetime.
```jinja3
{{ now() }}
```

contributors are welcome. fork for any changes you want to make