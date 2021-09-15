# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['Structure\\\\DataStructure.py', 'Structure\\\\SerialThread.py', 'Utils\\\\analyze.py', 'Utils\\\\hovertip.py', 'Utils\\\\Logger.py', 'Utils\\\\Utils.py', 'Views\\\\AnalyzeView.py', 'Views\\\\GUI.py', 'Views\\\\ScaleView.py', 'Views\\\\StartView.py', 'D:\\NTU\\python\\ECL-CKH-Pig-Scale-main'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
