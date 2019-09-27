# Simple ptvsd loader
# Example usage <flask>:
# cd /app
# env PYTHONIOENCODING=UTF-8 PYTHONUNBUFFERED=1
# python loader.py --default --client --host localhost --port 3000 -m flask run --no-debugger --no-reload --port=5000 --host=0.0.0.0

import os
import os.path
import sys
import traceback

args = sys.argv[:]
try:
    lib_path = os.path.join(os.path.dirname(__file__), 'lib', 'python')
    sys.path.insert(0, lib_path)
    try:
        import ptvsd
        from ptvsd.__main__ import main
    except ImportError:
        raise
except:
    traceback.print_exc()
    sys.exit(1)
finally:
    sys.path.remove(lib_path)
#print(args)
main(args)
