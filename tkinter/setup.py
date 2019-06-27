from disutils.core import setup
import py2exe,sys,os
sys.argv.append('py2exe')
setup=(
  options=['py2exe':{'bundle_files': 3,'compressed':True}],
  windows=[{'script':'app3.py'}],
  zipfile=None,
      )