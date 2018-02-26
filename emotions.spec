# -*- mode: python -*-

block_cipher = None

a = Analysis(['emotions.py'],
             pathex=['C:\\Users\\tijuk\\Projects\\v3_EmotionCam'],
             binaries=[],
             datas=[
                ('checkpoints\\epoch_75.hdf5','.\\checkpoints'),
                ('haarcascade_frontalface_default.xml','.'),
                ('gifs\\sad\\*', '.\\gifs\\sad'),
                ('gifs\\happy\\*', '.\\gifs\\happy'),
                ('gifs\\neutral\\*', '.\\gifs\\neutral'),
                ('gifs\\scared\\*', '.\\gifs\\scared'),
                ('gifs\\sunglass\\*', '.\\gifs\\sunglass'),
                ('gifs\\surprised\\*', '.\\gifs\\surprised')
                ],
             hiddenimports=['scipy._lib.messagestream'],
             hookspath=None,
             runtime_hooks=None,
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          exclude_binaries=True,
          name='emotions',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='emotions')


