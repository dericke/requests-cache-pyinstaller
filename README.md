# Requests Cache Pyinstaller Test

This project exists to demonstrate problems when using requests-cache with PyInstaller

## Run as standard Python script

1. Install dependencies with poetry
2. Make `pyinstaller_entry.py` executable
3. `poetry run ./pyinstaller_entry.py`
4. If the window with a "Get" button appears, the app is working properly

## Run as packaged Pyinstaller app

1. Install dependencies with poetry
2. `poetry run pyinstaller ./requests-cache-pyinstaller.spec -y`
3. Run in terminal (poetry not required this time) `'./dist/Requests Cache Pyinstaller/Requests Cache Pyinstaller Test'`
4. You will get something like the following:
   ```
   Traceback (most recent call last):
   File "pyinstaller_entry.py", line 3, in <module>
   from requests_cache_pyinstaller import main
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache_pyinstaller/main.py", line 9, in <module>
   import requests_cache
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/**init**.py", line 7, in <module>
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/backends/**init**.py", line 7, in <module>
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/backends/base.py", line 18, in <module>
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/serializers/**init**.py", line 6, in <module>
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/serializers/preconf.py", line 122, in <module>
   File "requests_cache/serializers/pipeline.py", line 44, in **init**
   File "requests_cache/serializers/pipeline.py", line 44, in <listcomp>
   AttributeError: type object 'Placeholder' has no attribute 'loads'
   [13481] Failed to execute script 'pyinstaller_entry' due to unhandled exception: type object 'Placeholder' has no attribute 'loads'
   [13481] Traceback:
   Traceback (most recent call last):
   File "pyinstaller_entry.py", line 3, in <module>
   from requests_cache_pyinstaller import main
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache_pyinstaller/main.py", line 9, in <module>
   import requests_cache
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/**init**.py", line 7, in <module>
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/backends/**init**.py", line 7, in <module>
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/backends/base.py", line 18, in <module>
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/serializers/**init**.py", line 6, in <module>
   File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
   File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
   File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
   File "PyInstaller/loader/pyimod02_importers.py", line 499, in exec_module
   File "requests_cache/serializers/preconf.py", line 122, in <module>
   File "requests_cache/serializers/pipeline.py", line 44, in **init**
   File "requests_cache/serializers/pipeline.py", line 44, in <listcomp>
   AttributeError: type object 'Placeholder' has no attribute 'loads'
   ```
