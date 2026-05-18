import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
raw = open(path, 'rb').read()
has_crlf = b'\r\n' in raw
content = raw.decode('utf-8').replace('\r\n', '\n')

PATCHES = [
    ('const TOTAL_LECCIONES_JERO = 20;',
     'const TOTAL_LECCIONES_JERO = 112;'),
]

applied = 0
for i, (old, new) in enumerate(PATCHES, 1):
    if old in content:
        content = content.replace(old, new, 1)
        applied += 1
        print(f'  \u2705 Patch {i}: TOTAL_LECCIONES_JERO 20 \u2192 112')
    else:
        print(f'  \u274c Patch {i}: no encontrado')

if has_crlf:
    content = content.replace('\n', '\r\n')
open(path, 'wb').write(content.encode('utf-8'))
total = len(PATCHES)
ok = applied == total
print(f'\n{applied}/{total} patches aplicados {"✅" if ok else "⚠️  revisa errores"}')
