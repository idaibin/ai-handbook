from pathlib import Path
from xml.sax.saxutils import escape
import textwrap, hashlib, json
import cairosvg

W,H=1920,1080
BG='#F7F5F0'
FONT='Noto Sans CJK SC, Noto Sans CJK JP, sans-serif'
OUT=Path('/mnt/data/story_studio_sync')

svg=[]
def add(s): svg.append(s)
def rect(x,y,w,h,fill='#fff',stroke='#5B6573',sw=2,rx=14, dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
def line(x1,y1,x2,y2,stroke='#697386',sw=2,dash=None,arrow=True):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    m=' marker-end="url(#arrow)"' if arrow else ''
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>')
def poly(points,stroke='#697386',sw=2,dash=None,arrow=True):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    m=' marker-end="url(#arrow)"' if arrow else ''
    pts=' '.join(f'{x},{y}' for x,y in points)
    add(f'<polyline points="{pts}" fill="none" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>')
def text(x,y,s,size=22,weight=400,fill='#29313A',anchor='middle'):
    add(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')
def multiline(x,y,lines,size=20,weight=400,fill='#29313A',anchor='middle',lineh=None):
    if isinstance(lines,str): lines=lines.split('\n')
    lineh=lineh or int(size*1.35)
    add(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">')
    for i,l in enumerate(lines):
        dy=0 if i==0 else lineh
        add(f'<tspan x="{x}" dy="{dy}">{escape(l)}</tspan>')
    add('</text>')
def box(x,y,w,h,title,lines,fill,stroke,title_fill='#1F2933',title_size=22,body_size=17,sw=2):
    rect(x,y,w,h,fill,stroke,sw)
    text(x+w/2,y+32,title,title_size,700,title_fill)
    if lines:
        multiline(x+w/2,y+60,lines,body_size,400,'#35404A','middle',int(body_size*1.35))
def label_pill(x,y,w,s,fill,stroke,text_fill='#29313A'):
    rect(x,y,w,30,fill,stroke,1.5,15)
    text(x+w/2,y+21,s,14,700,text_fill)

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
add('<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#697386"/></marker><filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.12"/></filter></defs>')
add(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

text(60,42,'Story Studio｜《班超：定远》24 集系列短剧关系路径',30,800,'#1E2933','start')
text(1860,40,'设计先行 × 证据驱动｜1920×1080',16,500,'#59636E','end')
line(60,58,1860,58,'#C9C4BA',1,arrow=False)

# Lane 1
text(60,92,'A–B｜设计冻结与系列故事完整性',19,800,'#3A675D','start')
rect(50,105,1820,205,'#FAFBF9','#3A7D6F',2,18,'8 6')
xs=[75,385,695,1105,1490]
widths=[250,250,350,310,300]
boxes=[
 ('Evidence → Architecture', ['读取真实来源与状态','Review → Freeze → 版本/SHA'],'#EEEAF8','#7367A8'),
 ('Source Ledger / Bible', ['《后汉书·班超传》主线','World / Character / Continuity'],'#E7F2EE','#3A7D6F'),
 ('24 集处理稿｜6×4', ['投笔出塞｜西域立足｜孤城五年','联盟与背叛｜破龟兹、立都护','焉耆、封侯与归乡'],'#D8ECE5','#3A7D6F'),
 ('24/24 Episode Matrix', ['目标·阻力·策略·转折·高潮·钩子','地点·人物·道具·史料·改编'],'#E7F2EE','#3A7D6F'),
 ('Series Story Gate', ['全季因果完整','0 orphan Event / Source','F / I / A / V 可追溯'],'#CDE4DD','#3A7D6F')]
for x,w,b in zip(xs,widths,boxes): box(x,130,w,145,*b,title_size=19,body_size=15)
for i in range(4): line(xs[i]+widths[i],202,xs[i+1]-10,202,'#697386',2)

# Lane 2
text(60,346,'C–F｜单集生产闭环（EP01 验证后复制到 EP02–EP24）',19,800,'#2D628F','start')
rect(50,360,1820,330,'#FBFCFD','#2D628F',2,18,'8 6')
# Top row
coords_top=[(75,395),(430,395),(785,395),(1140,395)]
node_w=300; node_h=105
top=[
 ('E00 单集合同',['Episode Treatment','与全季因果/前后集对齐']),
 ('E01–E02 编辑基线',['Screenplay → Shot List','→ Storyboard → Timed Animatic']),
 ('E03 生产设计',['HOD → Canonical Asset','→ Continuity / Work Orders']),
 ('E04 资产技术 Gate',['Vertical Slice → Asset / CLMC','→ G07 / Readiness Decision'])]
for (x,y),(t,ls) in zip(coords_top,top): box(x,y,node_w,node_h,t,ls,'#E6EEF7','#2D628F',title_size=18,body_size=15)
for i in range(3): line(coords_top[i][0]+node_w,448,coords_top[i+1][0]-10,448,'#697386',2)
# shared assets
box(1495,395,330,240,'共享 Asset & Continuity Graph',[
 'Character States / Locations / Props',
 'ShowLook / Camera / Lighting / Motion / Sound',
 '只生产被当前 Episode Contract 引用的资产',
 '跨集年龄、伤痕、服装、地理、政治关系连续'], '#FFF1D9','#B17A22',title_size=18,body_size=14)
line(1495,475,1440,475,'#B17A22',2,dash='6 5')
# down and lower row
poly([(1290,500),(1290,520),(1040,520),(1040,535)],'#697386',2)
coords_bottom=[(915,535),(620,535),(325,535),(75,535)]
bottom=[
 ('E05 镜头生产',['Shot Contract / Keyframe','Video Attempt / Dailies / Selects']),
 ('E06 Picture Lock',['完整镜头、节奏、时长锁定']),
 ('E07 Post & QC',['对白 / Foley / SFX / Score / Mix','VFX / Colour / Subtitles / QC']),
 ('E08 Episode Master',['Master + SRT + Manifest + Evidence'])]
for (x,y),(t,ls) in zip(coords_bottom,bottom): box(x,y,250,115,t,ls,'#E6EEF7','#2D628F',title_size=17,body_size=14)
for i in range(3): line(coords_bottom[i][0],592,coords_bottom[i+1][0]+250+10,592,'#697386',2)
# Final chain
box(1215,535,220,115,'篇章 Review',['每 4 集','因果 / 角色 / 视觉 / 声音'],'#F9E6D5','#A75E2A',title_size=17,body_size=14)
box(1495,535,160,115,'全季 Review',['24/24 Masters','6/6 Chapters','0 Orphans'],'#F9E6D5','#A75E2A',title_size=17,body_size=13)
box(1690,535,135,115,'Series Release',['正片 / 字幕','Manifest / 章节包'],'#DCEBD5','#4F7A3A',title_size=16,body_size=13)
poly([(200,650),(200,670),(1325,670),(1325,660)],'#697386',2); line(1435,592,1485,592); line(1655,592,1680,592)
# From story gate to episode
poly([(1790,275),(1790,335),(225,335),(225,385)],'#3A7D6F',2)

# Lane 3 - current pilot + batches
text(60,728,'当前 Pilot 与后续批次',19,800,'#A74B36','start')
rect(50,742,1110,220,'#FFFDFC','#C05D43',2,18)
text(75,770,'EP01《佣书》当前状态：105s｜14 Shots｜27 Panels｜1920×1080｜24 fps｜G07 2/10',16,700,'#8E3E2E','start')
# unit boxes
u_x=[75,285,495,705,915]
u_data=[
 ('Unit 01',['Camera / Light','BLOCKED · NOT WAIVED'],'#F6D0C7','#B33D2E'),
 ('Unit 02',['Minimal Set','COMPLETED'],'#DDEED8','#4F7A3A'),
 ('Unit 03',['Hero Brush','ACTIVE'],'#FFE5B5','#B17A22'),
 ('Unit 04',['Writing Surface','QUEUED'],'#FFF1D9','#B17A22'),
 ('Unit 05',['CLMC Core Proxy','PENDING'],'#EEF0F2','#7A828B')]
for x,(t,ls,f,s) in zip(u_x,u_data): box(x,800,175,95,t,ls,f,s,title_size=16,body_size=13,sw=2.2 if t=='Unit 03' else 2)
for i in range(1,4): line(u_x[i]+175,848,u_x[i+1]-10,848,'#697386',2)
# unit 01 path to review
box(495,910,385,38,'Vertical Slice Review → 处理 Unit 01 / Deferred Lanes → G07 Gate',[], '#FCE9E3','#C05D43',title_size=14,body_size=12)
poly([(162,895),(162,929),(485,929)],'#B33D2E',2,dash='6 5')
poly([(1002,895),(1002,929),(890,929)],'#697386',2)

# Batch panel
rect(1190,742,680,220,'#FFFDFC','#A75E2A',2,18)
text(1215,770,'系列分批执行：先证明闭环，再扩展；不并行铺开 24 集媒体生产',16,700,'#884A25','start')
batches=[('B0','架构/来源冻结'),('B1','EP01 Master'),('B2','提取验证模板'),('B3–B8','按篇章 4 集生产'),('B9','全季连续性/权利/发布')]
bx=[1215,1340,1465,1590,1740]; bw=[105,105,105,135,105]
for x,w,(bid,desc) in zip(bx,bw,batches):
    rect(x,810,w,95,'#F9E6D5','#A75E2A',1.6,12)
    text(x+w/2,838,bid,16,800,'#884A25')
    lines=textwrap.wrap(desc,width=8)
    multiline(x+w/2,862,lines,12,500,'#4A3C32','middle',17)
for i in range(4): line(bx[i]+bw[i],857,bx[i+1]-8,857,'#A75E2A',1.8)
text(1215,935,'篇章一在 B3 只补 EP02–EP04，并回看 EP01 跨集连续性。',14,500,'#665549','start')

# Footer evidence chain
rect(50,982,1820,70,'#F0F2F4','#67717D',1.8,14)
text(70,1008,'统一证据链',15,800,'#37404A','start')
chain=['Requirement','Work Order','Execution-native','Receipt / Attempt','Dailies','Manifest / Readback','Current Status','GitHub Projection','Next Unit']
cx=225
for i,c in enumerate(chain):
    w=150 if i<6 else 145
    label_pill(cx,996,w,c,'#FFFFFF','#8A939D')
    if i<len(chain)-1: line(cx+w,1011,cx+w+18,1011,'#697386',1.6)
    cx+=w+26
text(70,1040,'失败分流：Implementation → 新 Attempt｜Contract/Dependency → 修 Work Order｜Architecture/Baseline/Rights → Freeze + ChangeRecord + Impact + Reauthorize',13,500,'#4B5560','start')

add('</svg>')
svg_text=''.join(svg)
(OUT/'2026-08-21-banchao-series-production-path.svg').write_text(svg_text,encoding='utf-8')
cairosvg.svg2png(bytestring=svg_text.encode('utf-8'),write_to=str(OUT/'2026-08-21-banchao-series-production-path-1920x1080.png'),output_width=1920,output_height=1080)
print(hashlib.sha256(svg_text.encode()).hexdigest())
