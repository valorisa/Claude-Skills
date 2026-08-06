#!/usr/bin/env python3
"""fix_markdownlint.py - corrige MD026, MD032, MD034 (non auto-fixables par --fix).
Usage: python3 fix_markdownlint.py <fichier.md|dossier> [...]"""
import re, sys
from pathlib import Path

FENCE_RE = re.compile(r'^\s*(`{3,}|~{3,})')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)(\s+#+)?\s*$')
LIST_ITEM_RE = re.compile(r'^\s*(?:[-*+]|\d{1,9}[.)])\s+')
CONT_RE = re.compile(r'^ {1,3}\S')
BARE_URL_RE = re.compile(r'(?<![<(\["\'=])https?://[^\s<>`]+')
PUNCT = '.,;:!?'
EXCLUDE = {'.git', 'node_modules'}

def fence_mask(lines):
    """True pour chaque ligne situee dans un bloc de code fence."""
    mask, opener = [], None
    for ln in lines:
        m = FENCE_RE.match(ln)
        if opener is None:
            if m:
                opener = m.group(1)[0]
                mask.append(True)
            else:
                mask.append(False)
        else:
            mask.append(True)
            if m and m.group(1)[0] == opener:
                opener = None
    return mask

def fix_md026(line):
    """Ponctuation finale d'un titre : '# Titre.' -> '# Titre'"""
    m = HEADING_RE.match(line)
    if not m:
        return line
    text = m.group(2).rstrip()
    if text and text[-1] in PUNCT:
        cleaned = text.rstrip(PUNCT).rstrip()
        if cleaned:
            return m.group(1) + ' ' + cleaned
    return line

def wrap_url(m):
    url, trail = m.group(0), ''
    while url and url[-1] in PUNCT:
        trail = url[-1] + trail
        url = url[:-1]
    return '<' + url + '>' + trail

def fix_md034(line):
    """URL nue -> <URL>, sans toucher aux liens [x](url), <url>, ni au code inline."""
    parts = re.split(r'(`[^`]+`)', line)
    for i in range(0, len(parts), 2):
        parts[i] = BARE_URL_RE.sub(wrap_url, parts[i])
    return ''.join(parts)

def tighten_lists(lines, mask):
    """Supprime les lignes vides entre une puce et sa continuation indentée."""
    out = []
    n = len(lines)
    for i, ln in enumerate(lines):
        if (ln.strip() == '' and not mask[i]
                and 0 < i and i + 1 < n
                and not mask[i-1] and not mask[i+1]
                and (LIST_ITEM_RE.match(lines[i-1]) or CONT_RE.match(lines[i-1]))
                and CONT_RE.match(lines[i+1])):
            continue
        out.append(ln)
    return out

def fix_md032(lines, mask):
    """Insere les lignes vides manquantes autour de chaque bloc de liste,
    sans jamais couper une puce de sa continuation indentée."""
    out, i, n = [], 0, len(lines)
    while i < n:
        if mask[i] or not LIST_ITEM_RE.match(lines[i]):
            out.append(lines[i]); i += 1; continue
        j = i
        while j < n and not mask[j] and (LIST_ITEM_RE.match(lines[j]) or CONT_RE.match(lines[j])):
            j += 1
        if out and out[-1].strip():
            out.append('')
        out.extend(lines[i:j])
        if j < n and lines[j].strip():
            out.append('')
        i = j
    return out

def process(path):
    p = Path(path)
    orig = p.read_text(encoding='utf-8').split('\n')
    mask0 = fence_mask(orig)
    lines = tighten_lists(orig, mask0)
    mask = fence_mask(lines)
    lines = [ln if msk else fix_md034(fix_md026(ln)) for ln, msk in zip(lines, mask)]
    final = fix_md032(lines, mask)
    if final != orig:
        p.write_text('\n'.join(final), encoding='utf-8')
        return True
    return False

def main():
    targets = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_dir():
            targets += sorted(q for q in p.rglob('*.md')
                              if not any(x in EXCLUDE for x in q.parts))
        elif p.is_file():
            targets.append(p)
    fixed = 0
    for t in targets:
        status = 'corrigé' if process(t) else 'inchangé'
        if status == 'corrigé': fixed += 1
        print(f'[{status}] {t}')
    print(f'\n{fixed} fichier(s) modifié(s) sur {len(targets)} analysé(s).')

if __name__ == '__main__':
    main()
