# -*- mode: python -*-

import platform

is_mac = platform.system().lower() == "darwin"

block_cipher = None


added_files = []


a = Analysis(
    ["pyinstaller_entry.py"],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=["ptvsd"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
items = (
    []
    if is_mac
    else [
        a.binaries,
        a.zipfiles,
        a.datas,
    ]
)
exe = EXE(
    pyz,
    a.scripts,
    *items,
    [],
    exclude_binaries=is_mac,
    name="Requests Cache Pyinstaller Test",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    # icon="chameleon/resources/chameleon.icns" if is_mac else None,
    entitlements_file=None,
)
if is_mac:
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name="Requests Cache Pyinstaller",
    )
    app = BUNDLE(
        coll,
        name="Requests Cache Pyinstaller.app",
        bundle_identifier="com.kaart.requests_cache_pyinstaller",
        info_plist={
            "NSHighResolutionCapable": "True",
        },
    )
