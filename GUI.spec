# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['GUI.py','AppUI.py','GetBaseInfo1.py','GetBaseInfo2.py','GetCorrelationInfo.py','GetDerivativeInfo.py','GetVisualization.py','Xlwings.py','Excel.py'],
             pathex=['D:\\Data\\VsCode\\Files\\stock_demo\\'],
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
          name='大数据实验大作业GUI版',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon="D:\\Data\\VsCode\\Files\\stock_demo\\icon.ico")
