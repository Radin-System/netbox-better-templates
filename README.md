# Netbox Better Templates Plugin
Adds some functionality to netbox templates and config render.

## Added Functions

- **datetime**: adds datetime to config templates.
```jinja3
{{ datetime.now() }}
```

- **authenticated_user**: The user who is rendering the templates.
```jinja3
{{ authenticated_user }}
```