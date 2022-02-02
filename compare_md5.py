from pathlib import Path
import hashlib
import sys

if len(sys.argv[1:]) == 0:
    print('python3 compare_md5.py <folders path> <filter name>')
    print('ex. folder path: $PWD')
    print('    filter name: "02*.wav"')
    exit(0)

wav_path = sys.argv[1]
filter = sys.argv[2]

for path in Path(wav_path).rglob(filter):
    p = Path(path)
    m = hashlib.md5()
    filename = p.resolve()
    with open(filename, "rb") as f:
        buf = f.read()
        m.update(buf)

    h = m.hexdigest()
    print(filename, h)