ECHO OFF

python -m setup bdist_egg
python -m setup bdist_wheel

rmdir ".\build" /s /q
rmdir ".\netbox_better_templates.egg-info" /s /q

PAUSE