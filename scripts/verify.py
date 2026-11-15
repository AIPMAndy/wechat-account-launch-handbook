#!/usr/bin/env python3
"""Offline structural tests for source-driven Pages site and 36-ish page CJK PDF."""
from pathlib import Path
import csv, json, re, struct, sys, subprocess
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/'docs'; CH=ROOT/'content'/'chapters'
issues=[]
def check(condition,msg):
    if not condition:issues.append(msg)
chapters=list(sorted(CH.glob('*.md')))
check(len(chapters)==24, f'24 chapters expected, found {len(chapters)}')
for x in chapters:
    check((DOCS/'chapters'/(x.stem+'.html')).exists(),f'missing web page {x.stem}')
    s=x.read_text(encoding='utf-8');check(len(s)>600, f'chapter too short: {x.stem}')
    check(s.startswith('# '), f'no H1: {x.stem}')
with (ROOT/'templates/30-day-sop.csv').open(encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
check(len(rows)==30,'30 day SOP incomplete')
check(len({r['第几天'] for r in rows})==30,'duplicate SOP days')
check(len(list((ROOT/'templates').glob('*')))>8,'commercial template set incomplete')
check('xitang_ai/status/2121207382630117537' in (CH/'19-xitang-case-study.md').read_text(), 'xitang primary reference missing')
check('isnail/status/2060928267046060445' in (CH/'23-evidence-and-sources.md').read_text(), 'isnail primary reference missing')
check('www.samr.gov.cn' in (CH/'20-2026-rules.md').read_text(),'advert law source missing')
check('AIPMAndy' in (CH/'21-andy-case-playbook.md').read_text(),'contact information missing')
for file in [DOCS/'index.html', DOCS/'404.html',*sorted((DOCS/'chapters').glob('*.html'))]:
    soup=BeautifulSoup(file.read_text(encoding='utf-8'),'html.parser')
    check(len(soup.select('h1'))==1,f'H1 wrong: {file.name}')
    check(soup.select_one('link[rel="canonical"]') is not None, f'canonical missing {file}')
    for a in soup.select('a[href],link[rel="stylesheet"][href],script[src]'):
        url=a.get('href') or a.get('src')
        if not url or url.startswith(('#','mailto:','tel:','http:','https:','javascript:','data:')):continue
        clean=url.split('#')[0].split('?')[0]
        if not clean:continue
        dest=(file.parent/clean).resolve()
        check(dest.exists(), f'broken internal link: {file.name} -> {url}')
check((DOCS/'robots.txt').exists() and (DOCS/'sitemap.xml').exists() and (DOCS/'llms.txt').exists(), 'SEO root docs missing')
preview=DOCS/'assets'/'social-preview.png'
source_preview=ROOT/'assets'/'social-preview.png'
check(preview.exists() and source_preview.exists(), 'social preview missing from assets/ or docs/assets/')
if preview.exists():
    raw=preview.read_bytes()
    check(raw[:8]==b'\x89PNG\r\n\x1a\n' and len(raw)<1024*1024, 'social preview is not a PNG under 1MB')
    if raw[:8]==b'\x89PNG\r\n\x1a\n':
        width,height=struct.unpack('>II', raw[16:24])
        check(width==1280 and height==640, f'social preview size {width}x{height}')
    check(source_preview.read_bytes()==raw, 'docs social preview differs from assets/social-preview.png')
image_url='https://aipmandy.github.io/wechat-account-launch-handbook/assets/social-preview.png'
for file in [DOCS/'index.html', DOCS/'404.html', *sorted((DOCS/'chapters').glob('*.html'))]:
    text=file.read_text(encoding='utf-8')
    for needle in [
        f'property="og:image" content="{image_url}"',
        'property="og:image:width" content="1280"',
        'property="og:image:height" content="640"',
        'name="twitter:card" content="summary_large_image"',
        f'name="twitter:image" content="{image_url}"',
        '<link rel="canonical"',
        '<meta name="description"',
    ]:
        check(needle in text, f'meta missing in {file.name}: {needle[:70]}')
    if file.name!='404.html':
        check('application/ld+json' in text, f'JSON-LD missing in {file.name}')
        check('aggregateRating' not in text and 'reviewCount' not in text, f'rating markup in {file.name}')
home_ld=DOCS/'index.html'
if home_ld.exists():
    home_text=home_ld.read_text(encoding='utf-8')
    check('"@type": "TechArticle"' in home_text, 'homepage JSON-LD is not TechArticle')
    check('AI酋长Andy' in home_text and '流量 AI 联合创始人、星觉 AI 创始人' in home_text, 'homepage author metadata incomplete')
check((DOCS/'search-index.json').exists(),'missing search index')
index=json.loads((DOCS/'search-index.json').read_text(encoding='utf-8'))
check(len(index)==24, 'search index count mismatch')
js=DOCS/'assets/site.js'
check(js.exists(),'javascript missing')
try:
    result=subprocess.run(['node','--check',str(js)],capture_output=True,text=True,timeout=12)
    check(result.returncode==0, f'JS syntax error: {result.stderr[:350]}')
except FileNotFoundError:
    print('WARN: node unavailable; skipping JS syntax check')
pdf=DOCS/'wechat-account-launch-handbook.pdf';check(pdf.exists(),'PDF missing')
if pdf.exists():
    reader=PdfReader(str(pdf));check(len(reader.pages)>=25, f'PDF too short: {len(reader.pages)} pages')
    for i in [0,1,min(10,len(reader.pages)-1),len(reader.pages)-1]:
        t=reader.pages[i].extract_text() or ''
        check(len(t)>100, f'PDF text not extractable page={i+1}')
    alltext='\n'.join(page.extract_text() or '' for page in reader.pages)
    for term in ['微信公众', 'AIPMAndy', '西堂', '蜗牛', '商单', '2026']:
        check(term in alltext, f'PDF missing key {term}')
print('Chapters',len(chapters),'Website HTML',len(list(DOCS.rglob('*.html')))-1,'Templates',len(list((ROOT/'templates').glob('*'))),'PDF pages',len(PdfReader(str(pdf)).pages) if pdf.exists() else 'missing')
if issues:
    print('FAILED checks:',len(issues))
    for issue in issues[:50]:print('-',issue)
    sys.exit(1)
print('PASS: structural site, chapter content, link paths, JS syntax, SEO, PDF selectable Chinese text, required evidence')
