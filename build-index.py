#!/usr/bin/env python3
"""Assemble index.html from per-day editions in data/*.json.

Produces a self-contained single-page app (entra.news-style):
  - vertical sidebar: Cyber / AI / Tech sections, each expanding to its categories
  - month calendar to pick past editions (days with editions are active)
  - light / dark theme toggle
All edition data is embedded inline, so the page works from file:// or when hosted.

Run:  python3 build-index.py
"""
import json, glob, os, re, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, 'data')

def load_editions():
    eds = {}
    for path in sorted(glob.glob(os.path.join(DATA_DIR, '20*.json'))):
        base = os.path.splitext(os.path.basename(path))[0]
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', base):
            try:
                eds[base] = json.load(open(path, encoding='utf-8'))
            except Exception as e:
                print('skip', base, e)
    return eds

def build_manifest(eds):
    manifest = {}
    for date, ed in eds.items():
        counts = {}
        for slug, sec in ed.get('sections', {}).items():
            counts[slug] = sum(len(c.get('items', [])) for c in sec.get('categories', []))
        counts['total'] = sum(counts.values())
        manifest[date] = counts
    return manifest

def main():
    eds = load_editions()
    if not eds:
        raise SystemExit('No editions found in data/')
    manifest = build_manifest(eds)
    latest = sorted(eds.keys())[-1]
    payload = {'editions': eds, 'manifest': manifest, 'latest': latest,
               'generated': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
    data_js = json.dumps(payload, ensure_ascii=False)
    html = TEMPLATE.replace('/*__DATA__*/', data_js)
    with open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print('index.html written — %d editions, latest %s' % (len(eds), latest))

TEMPLATE = r'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Daily Briefing — Cyber · AI · Tech</title>
<style>
  :root{
    --accent:#D85604; --accent2:#AD1B02;
    --crit:#AD1B02; --high:#D85604; --med:#C77A0A; --low:#B0447E;
    --grad:linear-gradient(90deg,#AD1B02 0%,#D85604 28%,#E88D14 52%,#F3BE26 76%,#E669A2 100%);
    --serif:Georgia,"ITC Charter","Times New Roman",serif;
    --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  }
  html[data-theme="light"]{
    --bg:#f4f2ee; --panel:#ffffff; --panel2:#faf8f5; --ink:#1a1a1a; --ink2:#43413d;
    --muted:#7a756d; --rule:#e5e1da; --rule2:#d7d2c9; --shadow:0 1px 3px rgba(0,0,0,.06),0 6px 20px rgba(0,0,0,.04);
    --navhover:#f4f0ea; --navactive:#fdece2; --chip:#f0ece5;
  }
  html[data-theme="dark"]{
    --bg:#14140f; --panel:#1e1d18; --panel2:#242219; --ink:#f2efe8; --ink2:#cfc9bd;
    --muted:#928c80; --rule:#33322a; --rule2:#3f3d33; --shadow:0 1px 3px rgba(0,0,0,.4),0 8px 26px rgba(0,0,0,.35);
    --navhover:#26251d; --navactive:#3a2417; --chip:#2a2820;
  }
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);font:15.5px/1.6 var(--sans);
    -webkit-font-smoothing:antialiased;transition:background .2s,color .2s}
  a{color:inherit;text-decoration:none}

  /* momentum bar */
  .momentum{height:5px;background:var(--grad)}

  /* top bar */
  .topbar{display:flex;align-items:center;gap:16px;max-width:1240px;margin:0 auto;
    padding:14px 26px;border-bottom:1px solid var(--rule)}
  .brand{display:flex;align-items:center;gap:12px}
  .brand .logo{width:38px;height:38px;border-radius:9px;background:var(--grad);
    display:flex;align-items:center;justify-content:center;font-weight:800;color:#fff;font-size:19px;
    font-family:var(--serif);box-shadow:var(--shadow)}
  .brand .tt{line-height:1.15}
  .brand .tt b{font-family:var(--serif);font-size:20px;font-weight:700;letter-spacing:-.3px}
  .brand .tt span{display:block;font-size:10.5px;letter-spacing:2.5px;text-transform:uppercase;color:var(--accent);font-weight:700}
  .topbar .spacer{flex:1}
  .topnav{display:flex;gap:4px}
  .topnav a{font-size:12px;letter-spacing:1px;text-transform:uppercase;font-weight:600;color:var(--muted);
    padding:7px 12px;border-radius:7px}
  .topnav a:hover{background:var(--navhover);color:var(--ink)}
  .theme-btn{appearance:none;border:1px solid var(--rule2);background:var(--panel);color:var(--ink);
    cursor:pointer;border-radius:8px;padding:7px 11px;font-size:14px;line-height:1;display:flex;align-items:center;gap:6px}
  .theme-btn:hover{background:var(--navhover)}

  /* layout */
  .shell{display:grid;grid-template-columns:288px minmax(0,1fr);gap:34px;
    max-width:1240px;margin:0 auto;padding:26px 26px 90px}
  .side{position:sticky;top:18px;align-self:start;height:calc(100vh - 40px);overflow-y:auto;
    padding-right:6px;scrollbar-width:thin}
  .side::-webkit-scrollbar{width:7px}
  .side::-webkit-scrollbar-thumb{background:var(--rule2);border-radius:4px}

  /* daypicker */
  .daypick{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
  .daypick button{appearance:none;border:1px solid var(--rule2);background:var(--panel);color:var(--ink);
    cursor:pointer;border-radius:8px;width:34px;height:34px;font-size:15px;display:flex;align-items:center;justify-content:center}
  .daypick button:hover:not(:disabled){background:var(--navhover);border-color:var(--accent);color:var(--accent)}
  .daypick button:disabled{opacity:.35;cursor:default}
  .daypick .today{font-size:12.5px;font-weight:700;text-align:center;line-height:1.25}
  .daypick .today small{display:block;font-weight:500;color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:1px}

  /* nav */
  .navsec{margin-bottom:6px;border:1px solid var(--rule);border-radius:12px;overflow:hidden;background:var(--panel)}
  .navsec > .head{display:flex;align-items:center;gap:10px;width:100%;cursor:pointer;
    padding:12px 14px;font-weight:700;font-size:13px;letter-spacing:1.5px;text-transform:uppercase;
    background:var(--panel);border:none;color:var(--ink);text-align:left}
  .navsec > .head:hover{background:var(--navhover)}
  .navsec.active > .head{background:var(--navactive);color:var(--accent)}
  .navsec > .head .dot{width:9px;height:9px;border-radius:50%;flex:0 0 auto}
  .navsec > .head .n{margin-left:auto;font-size:11px;font-weight:700;color:var(--muted);
    background:var(--chip);border-radius:20px;padding:2px 9px;letter-spacing:.5px}
  .navsec .cats{display:none;padding:4px 8px 10px}
  .navsec.open .cats{display:block}
  .navsec .cats a{display:flex;align-items:center;gap:8px;padding:7px 10px;border-radius:8px;
    font-size:13px;color:var(--ink2);font-weight:500}
  .navsec .cats a:hover{background:var(--navhover);color:var(--ink)}
  .navsec .cats a .cn{margin-left:auto;font-size:11px;color:var(--muted)}

  .sidefoot{margin-top:16px;padding-top:14px;border-top:1px solid var(--rule);
    font-size:11.5px;color:var(--muted);line-height:1.6}
  .sidefoot a{color:var(--accent);font-weight:600}

  /* main */
  .main{min-width:0}
  .masthead{text-align:center;padding-bottom:18px;margin-bottom:8px;border-bottom:2px solid var(--ink)}
  .masthead .kick{font-size:11px;letter-spacing:4px;text-transform:uppercase;color:var(--accent);font-weight:700}
  .masthead h1{margin:6px 0 2px;font-family:var(--serif);font-size:46px;font-weight:700;letter-spacing:-1px;line-height:1}
  .masthead .dl{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:var(--muted);margin-top:8px}

  .lead{border:1px solid var(--rule);border-left:4px solid var(--accent);border-radius:12px;
    padding:18px 22px;margin:22px 0 10px;background:var(--panel);box-shadow:var(--shadow)}
  .lead h2{margin:0 0 12px;font-size:12px;letter-spacing:3px;text-transform:uppercase;color:var(--accent);
    display:flex;align-items:center;gap:9px}
  .lead h2 .db{flex:1;height:1px;background:var(--rule)}
  .lead ul{margin:0;padding:0;list-style:none}
  .lead li{margin:0;padding:9px 0 9px 26px;position:relative;font-size:14.5px;line-height:1.5;border-top:1px solid var(--rule)}
  .lead li:first-child{border-top:none}
  .lead li:before{content:"";position:absolute;left:6px;top:16px;width:7px;height:7px;border-radius:50%;background:var(--accent)}
  .lead li a:hover{color:var(--accent)}
  .rosternote{margin:12px 0 0;font-size:12.5px;font-style:italic;color:var(--muted);text-align:center}

  .cat{display:flex;align-items:center;gap:12px;margin:40px 0 20px;scroll-margin-top:16px}
  .cat h2{font-size:14px;letter-spacing:3px;text-transform:uppercase;font-weight:800;margin:0;white-space:nowrap}
  .cat .ln{flex:1;height:2px;background:var(--ink);opacity:.85}

  .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
  @media(max-width:1080px){.grid{grid-template-columns:1fr}}

  .item{border:1px solid var(--rule);border-radius:12px;background:var(--panel);padding:16px 18px;
    box-shadow:var(--shadow);transition:transform .12s,border-color .12s,box-shadow .12s}
  .item:hover{transform:translateY(-2px);border-color:var(--rule2)}
  .item .top{display:flex;align-items:center;gap:10px;margin-bottom:6px}
  .badge{font-size:10px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;
    padding:3px 9px;border-radius:20px;color:#fff}
  .b-crit{background:var(--crit)} .b-high{background:var(--high)} .b-med{background:var(--med)} .b-low{background:var(--low)}
  .item .date{font-size:12px;color:var(--muted);font-style:italic;margin-left:auto;white-space:nowrap}
  .item .date.stale{color:var(--high)}
  .item h3{margin:2px 0 0;font-family:var(--serif);font-size:19px;font-weight:700;line-height:1.28;letter-spacing:-.2px}
  .item h3 a:hover{color:var(--accent)}
  .item p{margin:9px 0 0;color:var(--ink2);font-size:14px;line-height:1.55}
  .why{margin-top:10px;font-size:13px;color:var(--ink2);background:var(--panel2);border-radius:8px;padding:9px 11px;line-height:1.5}
  .why b{font-variant:small-caps;letter-spacing:.5px;color:var(--accent);margin-right:4px}
  .src{margin-top:11px;font-size:10.5px;letter-spacing:1.2px;text-transform:uppercase}
  .src a{color:var(--muted);border-bottom:1px solid var(--rule2);padding-bottom:1px}
  .src a:hover{color:var(--accent);border-color:var(--accent)}

  .empty{border:1px dashed var(--rule2);border-radius:12px;padding:40px;text-align:center;color:var(--muted);background:var(--panel)}

  /* calendar */
  .calwrap{border:1px solid var(--rule);border-radius:12px;background:var(--panel);padding:14px;margin-top:4px}
  .calhead{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
  .calhead b{font-size:13px;letter-spacing:.5px}
  .calhead button{appearance:none;border:none;background:none;cursor:pointer;color:var(--muted);
    font-size:16px;padding:2px 8px;border-radius:6px}
  .calhead button:hover:not(:disabled){background:var(--navhover);color:var(--accent)}
  .calhead button:disabled{opacity:.3;cursor:default}
  .calgrid{display:grid;grid-template-columns:repeat(7,1fr);gap:3px}
  .calgrid .dow{font-size:9.5px;text-transform:uppercase;letter-spacing:.5px;color:var(--muted);text-align:center;padding:2px 0;font-weight:700}
  .calgrid .cell{aspect-ratio:1;display:flex;align-items:center;justify-content:center;position:relative;
    font-size:12px;border-radius:7px;color:var(--ink2)}
  .calgrid .cell.blank{visibility:hidden}
  .calgrid .cell.has{cursor:pointer;font-weight:700;color:var(--ink)}
  .calgrid .cell.has:hover{background:var(--navhover)}
  .calgrid .cell.has:after{content:"";position:absolute;bottom:4px;left:50%;transform:translateX(-50%);
    width:4px;height:4px;border-radius:50%;background:var(--accent)}
  .calgrid .cell.sel{background:var(--accent);color:#fff!important}
  .calgrid .cell.sel:after{background:#fff}
  .calgrid .cell.none{color:var(--muted);opacity:.5}

  @media(max-width:860px){
    .shell{grid-template-columns:1fr;padding:18px 16px 70px}
    .side{position:static;height:auto;overflow:visible}
    .masthead h1{font-size:34px}
    .topnav{display:none}
  }
</style>
</head>
<body>
<div class="momentum"></div>
<div class="topbar">
  <div class="brand">
    <div class="logo">DB</div>
    <div class="tt"><b>The Daily Briefing</b><span>Cyber · AI · Tech</span></div>
  </div>
  <div class="spacer"></div>
  <nav class="topnav">
    <a href="sources.html" id="srcCyber">Cyber Sources</a>
    <a href="sources-ai.html">AI Sources</a>
    <a href="sources-tech.html">Tech Sources</a>
  </nav>
  <button class="theme-btn" id="themeBtn" title="Toggle theme"><span id="themeIco">&#9789;</span></button>
</div>

<div class="shell">
  <aside class="side">
    <div class="daypick">
      <button id="prevDay" title="Previous edition">&#8249;</button>
      <div class="today"><span id="dpDate">—</span><small id="dpRel"></small></div>
      <button id="nextDay" title="Next edition">&#8250;</button>
    </div>
    <nav id="nav"></nav>
    <div class="calwrap">
      <div class="calhead">
        <button id="calPrev">&#8249;</button>
        <b id="calTitle">—</b>
        <button id="calNext">&#8250;</button>
      </div>
      <div class="calgrid" id="calGrid"></div>
    </div>
    <div class="sidefoot" id="sidefoot"></div>
  </aside>

  <main class="main">
    <div class="masthead">
      <div class="kick">Cyber · AI · Tech · Compiled Daily</div>
      <h1>The Daily Briefing</h1>
      <div class="dl" id="mastDate">—</div>
    </div>
    <div id="content"></div>
  </main>
</div>

<script>
const PAYLOAD = /*__DATA__*/;
const SECTIONS = [
  {slug:'cyber', label:'Cyber', color:'#AD1B02'},
  {slug:'ai',    label:'AI',    color:'#D85604'},
  {slug:'tech',  label:'Tech',  color:'#C77A0A'},
];
const SRCMAP = {cyber:'sources.html', ai:'sources-ai.html', tech:'sources-tech.html'};
const MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December'];
const DOW = ['M','T','W','T','F','S','S'];

let state = { date:null, section:'cyber', calYear:0, calMonth:0 };

function editionDates(){ return Object.keys(PAYLOAD.editions).sort(); }
function fmtLong(d){ const dt=new Date(d+'T00:00:00'); return dt.toLocaleDateString('en-US',{weekday:'long',month:'long',day:'numeric',year:'numeric'}); }
function stripIco(name){ return name.replace(/^[^A-Za-z0-9]+/,'').trim(); }
function icoOf(name){ const m=name.match(/^([^A-Za-z0-9]+)/); return m?m[1].trim():''; }
function slugify(s){ return s.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/(^-|-$)/g,''); }
function esc(s){ return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

function relLabel(d){
  const dates = editionDates(); const latest = dates[dates.length-1];
  if(d===latest) return 'Latest edition';
  const dt=new Date(d+'T00:00:00'), now=new Date(latest+'T00:00:00');
  const days=Math.round((now-dt)/86400000);
  return days+' day'+(days===1?'':'s')+' earlier';
}

function render(){
  const ed = PAYLOAD.editions[state.date];
  document.getElementById('mastDate').textContent = fmtLong(state.date);
  document.getElementById('dpDate').textContent = new Date(state.date+'T00:00:00').toLocaleDateString('en-US',{month:'short',day:'numeric'});
  document.getElementById('dpRel').textContent = relLabel(state.date);
  document.getElementById('srcCyber').setAttribute('href', SRCMAP[state.section]);
  renderNav(ed);
  renderContent(ed);
  renderCalendar();
  const dates=editionDates();
  document.getElementById('prevDay').disabled = dates.indexOf(state.date)<=0;
  document.getElementById('nextDay').disabled = dates.indexOf(state.date)>=dates.length-1;
}

function renderNav(ed){
  const nav=document.getElementById('nav'); nav.innerHTML='';
  SECTIONS.forEach(sec=>{
    const s=ed.sections[sec.slug]||{categories:[]};
    const total=(s.categories||[]).reduce((a,c)=>a+(c.items?c.items.length:0),0);
    const box=document.createElement('div');
    box.className='navsec'+(state.section===sec.slug?' active open':'');
    let cats=(s.categories||[]).map(c=>{
      const label=stripIco(c.name), ico=icoOf(c.name), n=c.items?c.items.length:0;
      return `<a href="#cat-${slugify(label)}" data-cat="${slugify(label)}"><span>${ico}</span><span>${esc(label)}</span><span class="cn">${n}</span></a>`;
    }).join('');
    box.innerHTML=`<button class="head" data-sec="${sec.slug}">
        <span class="dot" style="background:${sec.color}"></span>${sec.label}
        <span class="n">${total}</span></button>
      <div class="cats">${cats}</div>`;
    box.querySelector('.head').onclick=()=>{ state.section=sec.slug; render(); window.scrollTo({top:0,behavior:'smooth'}); };
    box.querySelectorAll('.cats a').forEach(a=>{
      a.onclick=(e)=>{ e.preventDefault();
        const el=document.getElementById('cat-'+a.dataset.cat);
        if(el) el.scrollIntoView({behavior:'smooth',block:'start'});
      };
    });
    nav.appendChild(box);
  });
}

function renderContent(ed){
  const s=ed.sections[state.section];
  const c=document.getElementById('content'); c.innerHTML='';
  if(!s){ c.innerHTML='<div class="empty">No content for this section.</div>'; return; }
  // lead
  if(s.lead && s.lead.length){
    let lis=s.lead.map(l=> l.url?`<li><a href="${l.url}" target="_blank" rel="noopener">${esc(l.text)}</a></li>`:`<li>${esc(l.text)}</li>`).join('');
    const label=SECTIONS.find(x=>x.slug===state.section).label;
    c.innerHTML+=`<div class="lead"><h2>Top of the Morning — ${label}<span class="db"></span></h2><ul>${lis}</ul>${s.rosternote?`<p class="rosternote">${esc(s.rosternote)}</p>`:''}</div>`;
  }
  (s.categories||[]).forEach(cat=>{
    const label=stripIco(cat.name), ico=icoOf(cat.name);
    let items=(cat.items||[]).map(it=>{
      const bcls={crit:'b-crit',high:'b-high',med:'b-med',low:'b-low'}[it.severity]||'b-med';
      return `<div class="item">
        <div class="top"><span class="badge ${bcls}">${esc(it.badge)}</span>
          <span class="date${it.stale?' stale':''}">${esc(it.date)}</span></div>
        <h3><a href="${it.url}" target="_blank" rel="noopener">${esc(it.headline)}</a></h3>
        <p>${esc(it.summary)}</p>
        ${it.why?`<div class="why"><b>Why it matters</b>${esc(it.why)}</div>`:''}
        <div class="src"><a href="${it.url}" target="_blank" rel="noopener">${esc(it.srcName||'Source')} &#8599;</a></div>
      </div>`;
    }).join('');
    c.innerHTML+=`<section><div class="cat" id="cat-${slugify(label)}"><span>${ico}</span><h2>${esc(label)}</h2><span class="ln"></span></div><div class="grid">${items||'<div class="empty">No items.</div>'}</div></section>`;
  });
}

/* calendar */
function renderCalendar(){
  const grid=document.getElementById('calGrid');
  document.getElementById('calTitle').textContent = MONTHS[state.calMonth]+' '+state.calYear;
  let html = DOW.map(d=>`<div class="dow">${d}</div>`).join('');
  const first=new Date(state.calYear,state.calMonth,1);
  let startDow=(first.getDay()+6)%7; // Monday-first
  const days=new Date(state.calYear,state.calMonth+1,0).getDate();
  for(let i=0;i<startDow;i++) html+='<div class="cell blank"></div>';
  for(let d=1;d<=days;d++){
    const ds=state.calYear+'-'+String(state.calMonth+1).padStart(2,'0')+'-'+String(d).padStart(2,'0');
    const has=PAYLOAD.editions[ds];
    let cls='cell '+(has?'has':'none')+(ds===state.date?' sel':'');
    const cnt=has?PAYLOAD.manifest[ds].total:0;
    html+=`<div class="${cls}" ${has?`data-d="${ds}" title="${cnt} stories"`:''}>${d}</div>`;
  }
  grid.innerHTML=html;
  grid.querySelectorAll('.cell.has').forEach(c=>{ c.onclick=()=>{ state.date=c.dataset.d; render(); }; });
  // arrows: disable beyond edition range
  const dates=editionDates();
  const minD=dates[0], maxD=dates[dates.length-1];
  const curFirst=new Date(state.calYear,state.calMonth,1);
  document.getElementById('calPrev').disabled = curFirst <= new Date(minD.slice(0,7)+'-01');
  const maxFirst=new Date(maxD.slice(0,4),parseInt(maxD.slice(5,7))-1,1);
  document.getElementById('calNext').disabled = curFirst >= maxFirst;
}

function stepDay(dir){
  const dates=editionDates(); let i=dates.indexOf(state.date);
  if(i+dir>=0 && i+dir<dates.length){ state.date=dates[i+dir];
    state.calYear=+state.date.slice(0,4); state.calMonth=+state.date.slice(5,7)-1; render(); }
}

function initTheme(){
  let t='light';
  try{ t=localStorage.getItem('db-theme')||'light'; }catch(e){}
  document.documentElement.setAttribute('data-theme',t);
  document.getElementById('themeIco').innerHTML = t==='dark'?'&#9728;':'&#9789;';
}
document.getElementById('themeBtn').onclick=()=>{
  let t=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';
  document.documentElement.setAttribute('data-theme',t);
  document.getElementById('themeIco').innerHTML = t==='dark'?'&#9728;':'&#9789;';
  try{ localStorage.setItem('db-theme',t); }catch(e){}
};
document.getElementById('prevDay').onclick=()=>stepDay(-1);
document.getElementById('nextDay').onclick=()=>stepDay(1);
document.getElementById('calPrev').onclick=()=>{ state.calMonth--; if(state.calMonth<0){state.calMonth=11;state.calYear--;} renderCalendar(); };
document.getElementById('calNext').onclick=()=>{ state.calMonth++; if(state.calMonth>11){state.calMonth=0;state.calYear++;} renderCalendar(); };

// init
initTheme();
state.date = PAYLOAD.latest;
state.calYear=+state.date.slice(0,4); state.calMonth=+state.date.slice(5,7)-1;
try{ const s=localStorage.getItem('db-section'); if(s) state.section=s; }catch(e){}
document.getElementById('sidefoot').innerHTML =
  `Independent daily intelligence across Cyber, AI &amp; Tech.<br>`+
  `${editionDates().length} edition(s) archived · generated ${esc(PAYLOAD.generated)}.<br>`+
  `<a href="${SRCMAP[state.section]}">Sources &amp; masthead &#8594;</a>`;
render();
// persist section
const _r=render; render=function(){ _r(); try{localStorage.setItem('db-section',state.section);}catch(e){} };
</script>
</body>
</html>
'''

if __name__ == '__main__':
    main()
