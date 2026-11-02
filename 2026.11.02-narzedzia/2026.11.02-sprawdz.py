#!/usr/bin/env python3
"""Kontrola lokalnych odnośników, hashy, prywatności i historii GWK."""
from pathlib import Path
import hashlib, json, re, subprocess
r=Path(__file__).resolve().parents[1]
errors=[]
for name,digest in json.loads((r/'2026.11.02-zrodla/2026.11.02-manifest.json').read_text()).items():
 p=r/name
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest: errors.append('Hash: '+name)
ids=set()
for p in r.rglob('*'):
 if not p.is_file() or '.git' in p.parts: continue
 if p.suffix not in ('.md','.json','.yml','.py'):continue
 s=p.read_text()
 # Oryginały HTML pozostają niezmienione; nie wykonujemy ich.
 for forbidden in ['/Users/', '/home/', 'ghp_', 'gho_', 'github_pat_']:
  if forbidden in s and p.suffix!='.py':errors.append('Dane prywatne: '+str(p.relative_to(r)))
 if p.suffix!='.md':continue
 if any(c in s for c in '\u2014\u2013\u2018\u2019'):errors.append('Typografia: '+p.name)
 for ident in re.findall(r'^id: (.+)$',s,re.M):
  if ident in ids:errors.append('Powtórzone ID: '+ident)
  ids.add(ident)
 for link in re.findall(r'\]\(([^)]+)\)',s):
  if re.match(r'https?://',link):continue
  target,_,anchor=link.partition('#')
  q=p.parent/target if target else p
  if not q.is_file(): errors.append('Brak linku: '+link);continue
  if anchor and q.suffix=='.md':
   headings=re.findall(r'^#+ (.+)$',q.read_text(),re.M)
   slugs=[re.sub(r'[^\w\- ]','',x.lower()).replace(' ','-') for x in headings]
   if anchor not in slugs: errors.append('Brak kotwicy: '+link)
identity='Gęba w Kubeł <351696654+gebawkubel@users.noreply.github.com>'
result=subprocess.run(['git','log','--all','--format=%an <%ae>|%cn <%ce>'],cwd=r,capture_output=True,text=True)
if result.returncode==0:
 for line in result.stdout.splitlines():
  if line!=identity+'|'+identity: errors.append('Niedozwolona tożsamość w historii')
print('\n'.join(errors) if errors else 'OK: hashe, linki, ID, typografia, podstawowy skan prywatności i autorstwo.')
raise SystemExit(bool(errors))
