# geohub-services-qgis-plugin
A QGIS plugin to import Ontario Geohub LIO data layers into the QGIS project

# Using the plugin

- To test the plugin
1. Download this repo and unzip
2. Quit QGIS
3. File the unzipped folder into your QGIS plugins directory
4. Restart QGIS
5. In QGIS - Plugins "Manage and Install Plugins" - go to "Installed".
6. Check the "geohub_services" box


- TODO - add notes on how to use the plugin / its different functions and features
- For now - the plugin will recreate the load_lyrs_from_geohub_services pyqgis script, and nothing more. [https://github.com/eco-gis-helpers/geohub-services](https://github.com/eco-gis-helpers/geohub-services/blob/main/load_lyrs_from_geohub_services.py)


# Setting up the dev environment / recompiling resources.py
Used Plugin Builder 3 Within QGIS to make the plugin structure
The icon.png must be 24x24 pixels

On MacOS

1. In terminal, navigate to the directory where you made the plugin directory with Plugin Builder 3
2. Set up a python virtual environment
```
python3 -m venv geohub_env
```
3. Activate the environment
```
source py_env/bin/activate
```
4. Install pyrcc5
```
pip install PyQt5
```
6. Compile resource file (Convert the .qrc resource file to Python file using pyrcc5). resources.py must be recompiled if the icon.png or the metadata is changed.
```
pyrcc5 resources.qrc -o resources.py
```
The next steps are useful for dev, but not mandatory

7. Create a Symlink - Make a symbolic link in the QGIS plugin directory pointing to the plugin development directory
```
cd /Users/<username>/Library/Application \ Support/QGIS/QGIS3/profiles/default/python/plugins
ln -s <plugin development directory>
```
8. Verify the symlink with ls -l Users/<username>/Library/Application \ Support/QGIS/QGIS3/profiles/default/python/plugins
9. Restarting QGIS is needed anytime changes to the plugin code have been made
