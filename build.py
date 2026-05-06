import os

# ── ICON SVG (symbol only) ──────────────────────────────────────────
ICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 188 220" width="100%" height="100%"><path d="M0 0 C3.05625827 1.51700738 5.13735897 3.30989903 7.62109375 5.64453125 C10.27998288 8.11910211 12.87386698 10.47959008 15.74609375 12.70703125 C24.17742085 20.24140866 30.4076539 29.99972353 36.68359375 39.33203125 C37.09609375 38.79835937 37.50859375 38.2646875 37.93359375 37.71484375 C39.84453202 35.24939215 41.7627089 32.78974133 43.68359375 30.33203125 C44.32039062 29.51605469 44.9571875 28.70007813 45.61328125 27.859375 C47.61098667 25.32814584 49.63748507 22.82428392 51.68359375 20.33203125 C52.34875 19.51734375 53.01390625 18.70265625 53.69921875 17.86328125 C58.03387801 12.79012449 62.73859978 8.32763565 67.87109375 4.08203125 C68.4532666 3.57937744 69.03543945 3.07672363 69.63525391 2.55883789 C71.3515625 1.19140625 71.3515625 1.19140625 74.68359375 -0.66796875 C87.67538433 1.56424249 99.34720558 15.05668305 106.63671875 25.125 C110.47071497 31.13208186 113.4291244 37.56862321 115.68359375 44.33203125 C116.60398438 44.46738281 117.524375 44.60273437 118.47265625 44.7421875 C135.59571179 47.65415316 148.48578526 55.05433178 159.24609375 68.95703125 C162.19250505 73.21295868 163.89600048 76.12806626 163.68359375 81.33203125 C162.58151367 84.73011151 161.76261499 85.27935042 158.68359375 87.33203125 C151.70958438 88.11941941 151.70958438 88.11941941 147.99609375 85.26953125 C145.68359375 82.33203125 145.68359375 82.33203125 143.55859375 79.01953125 C137.6686136 70.58949716 128.28013115 66.15345037 118.68359375 63.33203125 C118.71839844 64.15703125 118.75320312 64.98203125 118.7890625 65.83203125 C119.31813364 88.40573315 112.51579277 109.42472695 96.91015625 126.07421875 C89.14577423 133.94757455 81.44266261 139.38460664 70.05859375 139.70703125 C63.39884753 139.64517602 58.8121174 138.66399697 53.68359375 134.33203125 C47.00968135 127.41154573 46.21348675 119.31834408 46.37109375 110.01953125 C47.94845681 91.40664717 59.13029292 75.47247697 72.87109375 63.53515625 C80.23216197 57.76898615 88.00190452 52.84000733 96.68359375 49.33203125 C95.0531795 39.01225017 88.17359341 30.29092184 80.68359375 23.33203125 C78.53911034 22.06968829 78.53911034 22.06968829 76.68359375 21.33203125 C59.44023245 34.47453585 48.29500037 55.8862457 37.68359375 74.33203125 C34.02835974 71.09290646 31.9284414 67.40705086 29.68359375 63.14453125 C23.20462016 51.27917586 15.38485358 40.3457697 6.74609375 29.95703125 C6.09181396 29.16292847 6.09181396 29.16292847 5.42431641 28.3527832 C2.80860887 25.29642413 0.24221565 23.20364992 -3.31640625 21.33203125 C-11.91369082 28.3145974 -18.15452523 35.96415952 -22.31640625 46.33203125 C-22.31640625 47.32203125 -22.31640625 48.31203125 -22.31640625 49.33203125 C-21.589375 49.66074219 -20.86234375 49.98945313 -20.11328125 50.328125 C-12.06335659 54.13635859 -5.24673767 58.76407267 1.68359375 64.33203125 C2.40289062 64.8734375 3.1221875 65.41484375 3.86328125 65.97265625 C16.25757901 75.8283629 25.13069108 91.87715125 27.68359375 107.33203125 C28.68219516 116.8187446 27.38993504 125.6239761 21.37109375 133.26953125 C20.48421875 133.95015625 19.59734375 134.63078125 18.68359375 135.33203125 C17.71421875 136.09515625 16.74484375 136.85828125 15.74609375 137.64453125 C9.54148668 140.96358962 1.5597729 140.20430785 -5.09375 138.70703125 C-19.34848124 133.66270297 -29.17609549 121.02392464 -35.70825195 107.91137695 C-41.40750202 95.89677764 -44.53782331 84.2557887 -44.37890625 70.89453125 C-44.37439453 70.16298828 -44.36988281 69.43144531 -44.36523438 68.67773438 C-44.35358773 66.89579706 -44.33565816 65.11390262 -44.31640625 63.33203125 C-57.98954236 66.17936545 -66.07175848 74.56868889 -74.31640625 85.33203125 C-76.31640625 87.33203125 -76.31640625 87.33203125 -80.19140625 87.70703125 C-83.37397413 87.63771943 -84.12564781 87.47876851 -86.75390625 85.45703125 C-89.36766724 81.90231631 -89.77617131 79.76057283 -89.31640625 75.33203125 C-87.91364648 72.97164634 -86.60039425 71.05191065 -84.87890625 68.95703125 C-84.42298096 68.38903809 -83.96705566 67.82104492 -83.49731445 67.23583984 C-74.25759098 55.96866621 -63.53842495 47.87554294 -48.81640625 46.14453125 C-46.06886592 45.78505793 -43.98502169 45.25413865 -41.31640625 44.33203125 C-38.49919095 40.66390194 -37.57626952 36.73078464 -36.31640625 32.33203125 C-31.76295988 22.93537375 -12.93702239 -3.73057475 0 0 Z M-27.31640625 67.33203125 C-25.82692531 86.93982505 -21.29526581 103.4898482 -6.51953125 117.51171875 C-2.74940799 120.62674967 0.44955181 122.48096738 5.49609375 122.14453125 C7.85049237 121.44290244 7.85049237 121.44290244 9.68359375 119.33203125 C11.24198405 109.40754563 8.38223528 100.21498217 3.109375 91.828125 C1.40451595 89.54305751 -0.39447642 87.43718766 -2.31640625 85.33203125 C-3.28513672 84.22601563 -3.28513672 84.22601563 -4.2734375 83.09765625 C-10.3742809 76.53274127 -17.53818236 71.70147176 -25.31640625 67.33203125 C-25.97640625 67.33203125 -26.63640625 67.33203125 -27.31640625 67.33203125 Z M79.484375 81.40625 C69.91003522 91.64518604 64.07751384 102.45504084 64.21484375 116.6171875 C64.48197023 119.33492791 64.48197023 119.33492791 66.015625 121.19921875 C67.7871731 122.62397452 67.7871731 122.62397452 70.87109375 122.39453125 C79.37461228 120.02469822 86.2514401 113.07715802 90.71679688 105.60253906 C97.68958093 93.16921722 101.37357655 81.74500527 100.68359375 67.33203125 C94.76282796 67.33203125 83.65814541 77.51847671 79.484375 81.40625 Z" fill="currentColor" transform="translate(94.31640625,79.66796875)"/></svg>'''

# ── SHARED CSS ──────────────────────────────────────────────────────
CSS = '''
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@200;300&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&display=swap" rel="stylesheet">
<style>
:root{--g:#1a6644;--m:#3ecb96;--p:#f7f4ef;--w:#fff;--k:#0e0e0e;--d:#8a8680;--wa:#e8e3d8;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{font-size:16px;scroll-behavior:smooth}
body{background:var(--w);color:var(--k);font-family:'DM Sans',sans-serif;font-weight:300;overflow-x:hidden;cursor:none}
::selection{background:var(--g);color:#fff}
#dot{position:fixed;width:7px;height:7px;background:var(--g);border-radius:50%;pointer-events:none;z-index:9999;top:0;left:0;transform:translate(-50%,-50%);will-change:left,top}
#ring{position:fixed;width:38px;height:38px;border:1px solid rgba(26,102,68,.22);border-radius:50%;pointer-events:none;z-index:9998;top:0;left:0;transform:translate(-50%,-50%);transition:width .3s,height .3s,border-color .3s;will-change:left,top}
.hov #ring{width:56px;height:56px;border-color:rgba(62,203,150,.4)}
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes wUp{from{transform:translateY(108%)}to{transform:translateY(0)}}
@keyframes roll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.reveal{opacity:0;transform:translateY(22px);transition:opacity .65s ease,transform .65s ease}
.reveal.on{opacity:1;transform:none}
.reveal-l{opacity:0;transform:translateX(-22px);transition:opacity .65s ease,transform .65s ease}
.reveal-l.on{opacity:1;transform:none}
.reveal-r{opacity:0;transform:translateX(22px);transition:opacity .65s ease,transform .65s ease}
.reveal-r.on{opacity:1;transform:none}
nav{position:fixed;top:0;left:0;right:0;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:1.5rem 3rem;transition:background .4s,border-color .4s}
nav.sc{background:rgba(247,244,239,.96);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border-bottom:1px solid rgba(14,14,14,.07)}
.nicon{width:36px;height:36px;display:block;color:var(--g)}
.nright{display:flex;align-items:center;gap:2.5rem}
.na{font-size:.57rem;letter-spacing:.18em;text-transform:uppercase;color:var(--d);text-decoration:none;transition:color .25s;font-family:'DM Sans',sans-serif}
.na:hover,.na.act{color:var(--g)}
.nb{font-size:.57rem;letter-spacing:.18em;text-transform:uppercase;color:#fff;background:var(--g);border:none;padding:.52rem 1.3rem;cursor:none;font-family:'DM Sans',sans-serif;font-weight:500;transition:background .25s;text-decoration:none;display:inline-block}
.nb:hover{background:var(--k)}
.strip{background:var(--k);padding:.8rem 0;overflow:hidden;white-space:nowrap}
.strip-in{display:inline-flex;animation:roll 32s linear infinite}
.si{display:inline-flex;align-items:center;gap:1.2rem;padding:0 1.8rem;font-size:.55rem;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.28)}
.si .d{color:var(--m);font-size:.38rem}
footer{background:var(--k);padding:3rem;display:grid;grid-template-columns:1fr 1fr 1fr;gap:3rem;align-items:start}
.ficon{width:32px;height:32px;color:rgba(255,255,255,.35);margin-bottom:1rem;display:block}
.fname{font-family:'Unbounded',sans-serif;font-weight:200;font-size:.8rem;letter-spacing:.12em;color:rgba(255,255,255,.45);margin-bottom:.5rem}
.ftag{font-size:.55rem;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.2);margin-bottom:1.5rem}
.flinks{display:flex;flex-direction:column;gap:.6rem}
.fa2{font-size:.6rem;letter-spacing:.1em;color:rgba(255,255,255,.25);text-decoration:none;transition:color .25s}
.fa2:hover{color:var(--m)}
.fcopy{font-size:.52rem;color:rgba(255,255,255,.12);margin-top:.5rem}
.fright{text-align:right}
.fright .flinks{align-items:flex-end}
@media(max-width:900px){
  nav{padding:1rem 1.2rem}
  .nright .na{display:none}
  footer{grid-template-columns:1fr;gap:2rem}
  .fright{text-align:left}
  .fright .flinks{align-items:flex-start}
}
</style>'''

# ── SHARED JS ──────────────────────────────────────────────────────
JS = '''<script>
const dot=document.getElementById('dot'),ring=document.getElementById('ring');
let mx=0,my=0,rx=0,ry=0;
document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;dot.style.left=mx+'px';dot.style.top=my+'px';},{passive:true});
(function raf(){rx+=(mx-rx)*.12;ry+=(my-ry)*.12;ring.style.left=rx+'px';ring.style.top=ry+'px';requestAnimationFrame(raf);})();
document.querySelectorAll('a,button,[data-hover]').forEach(el=>{
  el.addEventListener('mouseenter',()=>document.body.classList.add('hov'));
  el.addEventListener('mouseleave',()=>document.body.classList.remove('hov'));
});
const io=new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target);}});
},{threshold:0.1,rootMargin:'0px 0px -30px 0px'});
document.querySelectorAll('.reveal,.reveal-l,.reveal-r').forEach(el=>io.observe(el));
const nav=document.getElementById('nav');
if(nav)window.addEventListener('scroll',()=>nav.classList.toggle('sc',window.scrollY>50),{passive:true});
function p2(n){return String(n).padStart(2,'0')}
function tick(){
  const ms=Math.max(0,new Date('2026-04-23T00:00:00+05:30')-Date.now());
  const e1=document.getElementById('cd1'),e2=document.getElementById('cd2'),e3=document.getElementById('cd3'),e4=document.getElementById('cd4');
  if(e1)e1.textContent=p2(Math.floor(ms/86400000));
  if(e2)e2.textContent=p2(Math.floor(ms%86400000/3600000));
  if(e3)e3.textContent=p2(Math.floor(ms%3600000/60000));
  if(e4)e4.textContent=p2(Math.floor(ms%60000/1000));
}
tick();setInterval(tick,1000);
function go(s){document.querySelector(s)?.scrollIntoView({behavior:'smooth'});}
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',e=>{
    const t=document.querySelector(a.getAttribute('href'));
    if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth'});}
  });
});
const nsub=document.getElementById('nsub');
if(nsub)nsub.addEventListener('submit',e=>{
  e.preventDefault();
  const ph=document.getElementById('ph');
  if(ph&&ph.value.trim().length>=8){
    document.querySelector('.ntfm').style.display='none';
    document.querySelector('.ntnt').style.display='none';
    document.getElementById('ok').style.display='block';
  }
});
</script>'''

def nav_html(active=''):
    return f'''<div id="dot"></div><div id="ring"></div>
<nav id="nav">
  <a href="index.html" style="display:flex;align-items:center;gap:.7rem;text-decoration:none;color:var(--g)">
    <div class="nicon">{ICON}</div>
    <div>
      <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:.82rem;letter-spacing:.18em;color:var(--k)">R V R</div>
      <div style="font-size:.46rem;letter-spacing:.24em;text-transform:uppercase;color:var(--d);margin-top:.1rem">Super Speciality Centre</div>
    </div>
  </a>
  <div class="nright">
    <a href="about.html" class="na{' act' if active=='about' else ''}">About</a>
    <a href="services.html" class="na{' act' if active=='services' else ''}">Specialities</a>
    <a href="doctors.html" class="na{' act' if active=='doctors' else ''}">Doctors</a>
    <a href="index.html#ntfy" class="nb">Book Appointment</a>
  </div>
</nav>'''

def footer_html():
    return f'''<footer>
  <div>
    <div class="ficon">{ICON}</div>
    <div class="fname">R V R</div>
    <div class="ftag">Super Speciality Centre</div>
    <div class="fcopy">Falnir, Ayush Building<br>Mangalore, Karnataka — 575001</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:.6rem;padding-top:3rem">
    <a href="index.html" class="fa2">Home</a>
    <a href="about.html" class="fa2">About</a>
    <a href="services.html" class="fa2">Specialities</a>
    <a href="doctors.html" class="fa2">Doctors</a>
    <a href="index.html#ntfy" class="fa2">Book Appointment</a>
    <a href="mailto:info@rvrhealthcare.in" class="fa2">info@rvrhealthcare.in</a>
  </div>
  <div class="fright">
    <div class="flinks" style="margin-bottom:1.5rem">
      <a href="https://instagram.com" class="fa2">Instagram</a>
      <a href="https://facebook.com" class="fa2">Facebook</a>
    </div>
    <div class="fcopy">© 2026 RVR Super Speciality Centre<br>Private Limited. All rights reserved.</div>
  </div>
</footer>'''

def wrap(title, meta, active, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — RVR Super Speciality Centre</title>
<meta name="description" content="{meta}">
{CSS}
</head>
<body>
{nav_html(active)}
{body}
{footer_html()}
{JS}
</body>
</html>'''

# ════════════════════════════════════════════════════════════════════
# DATA
# ════════════════════════════════════════════════════════════════════

DOCTORS = [
  {
    'slug': 'raghavendra',
    'name': 'Dr. Raghavendra B.S.',
    'init': 'RB',
    'qual': 'MBBS · MD · DM (Neurology)',
    'dept': 'Neurology',
    'role': 'Senior Consultant Neurologist & Director',
    'exp': '18+ Years',
    'prev': 'Father Muller Medical College · Omega Hospital · Unity Hospital · Athena Hospital · Mangalore Heartscan Foundation',
    'langs': 'Kannada · English · Hindi · Tulu',
    'bio': 'Dr. Raghavendra B.S. is one of the most respected neurologists in Coastal Karnataka with over 18 years of clinical experience. He serves as Professor & Head of the Department of Neurology at Father Muller Medical College, Mangalore and has been a senior consultant at Omega Hospital, Unity Hospital and Athena Hospital. He is widely recognised for his expertise in stroke medicine, epilepsy and cerebrovascular disorders. Dr. Raghavendra has contributed significantly to academic neurology with peer-reviewed publications in SCOPUS-indexed journals including Neurology India, with research covering neurological manifestations of COVID-19 and cerebral venous sinus thrombosis.',
    'awards': ['Professor & HOD of Neurology — Father Muller Medical College', 'Published Research: Spectrum of Neurological Manifestations of COVID-19 — Neurology India, SCOPUS 2022', 'Published Research: Cerebrovascular Events as Neuro-COVID Manifestations — Neurology India, SCOPUS 2023', 'Published Research: Oral Anticoagulation in Cerebral Venous Sinus Thrombosis — Karnataka Tertiary Care Study'],
    'treats': ['Stroke & Cerebrovascular Disease', 'Epilepsy & Seizure Disorders', 'Cerebral Venous Sinus Thrombosis', 'Headache & Migraine', 'Neuromuscular Disorders', 'Parkinson\'s Disease', 'Dementia & Memory Disorders', 'Multiple Sclerosis'],
  },
  {
    'slug': 'manish',
    'name': 'Dr. Manish Rai',
    'init': 'MR',
    'qual': 'MBBS · MD (Cardiology)',
    'dept': 'Cardiology',
    'role': 'Consultant Cardiologist',
    'exp': '12+ Years',
    'prev': 'KMC Hospital Mangalore · Kasturba Medical College',
    'langs': 'Kannada · English · Hindi · Tulu · Konkani',
    'bio': 'Dr. Manish Rai is a dedicated cardiologist with over 12 years of experience in interventional and non-interventional cardiology. Trained at one of India\'s premier medical institutions, he specialises in the diagnosis and management of complex cardiac conditions including coronary artery disease, heart failure and arrhythmias. Dr. Manish is known for his patient-first approach, combining clinical precision with genuine compassion to deliver outstanding cardiac care to the people of Coastal Karnataka.',
    'awards': ['Advanced Cardiac Life Support (ACLS) Certified', 'Fellowship in Echocardiography', 'Member — Cardiological Society of India'],
    'treats': ['Coronary Artery Disease', 'Heart Failure Management', 'Cardiac Arrhythmias', 'Hypertension', 'Echocardiography', 'Stress Testing', 'Lipid Disorders', 'Preventive Cardiology'],
  },
  {
    'slug': 'nishitha',
    'name': 'Dr. Nishitha',
    'init': 'NS',
    'qual': 'MBBS · MD',
    'dept': 'Internal Medicine',
    'role': 'Consultant Physician',
    'exp': '8+ Years',
    'prev': 'Wenlock District Hospital · KMC Manipal',
    'langs': 'Kannada · English · Tulu',
    'bio': 'Dr. Nishitha is a highly capable physician with a strong foundation in internal medicine and general practice. With 8 years of experience across leading hospitals in Karnataka, she brings clinical thoroughness and a compassionate approach to patient care. She is particularly skilled in managing complex multi-system conditions and chronic disease management, ensuring each patient receives personalised, evidence-based treatment.',
    'awards': ['Member — Association of Physicians of India', 'Advanced Diploma in Diabetes Management'],
    'treats': ['Diabetes Management', 'Hypertension', 'Thyroid Disorders', 'Respiratory Conditions', 'Fever & Infections', 'Anaemia', 'Kidney Function Disorders', 'General Medicine'],
  },
  {
    'slug': 'rakshith',
    'name': 'Dr. Rakshith Kedambady',
    'init': 'RK',
    'qual': 'MBBS · MS (General Surgery)',
    'dept': 'General & Laparoscopic Surgery',
    'role': 'Consultant Surgeon',
    'exp': '10+ Years',
    'prev': 'Father Muller Medical College Hospital · KMC Hospital Mangalore',
    'langs': 'Kannada · English · Tulu',
    'bio': 'Dr. Rakshith Kedambady is a skilled general and laparoscopic surgeon with over a decade of surgical experience. Trained at Father Muller Medical College, he has performed hundreds of minimally invasive procedures with excellent clinical outcomes. Dr. Rakshith is passionate about bringing advanced surgical techniques to patients in Coastal Karnataka, reducing recovery time and improving quality of life through precision surgery.',
    'awards': ['Fellowship in Minimal Access Surgery', 'Member — Association of Surgeons of India', 'Advanced Laparoscopic Surgery Training — FIAGES'],
    'treats': ['Laparoscopic Cholecystectomy', 'Appendectomy', 'Hernia Repair', 'Thyroid Surgery', 'Colorectal Surgery', 'Abdominal Surgery', 'Emergency Surgery', 'Wound Management'],
  },
  {
    'slug': 'anjan',
    'name': 'Dr. Anjan',
    'init': 'AJ',
    'qual': 'MBBS · MS (ENT)',
    'dept': 'ENT — Ear, Nose & Throat',
    'role': 'Consultant ENT Specialist',
    'exp': '9+ Years',
    'prev': 'Mangalore Heartscan Foundation · KMC Hospital Mangalore',
    'langs': 'Kannada · English · Tulu · Konkani',
    'bio': 'Dr. Anjan is a highly regarded ENT specialist serving Coastal Karnataka with over 9 years of clinical experience. He provides comprehensive care for disorders of the ear, nose, throat, head and neck. Known for his meticulous approach to diagnostics and surgical treatment, Dr. Anjan has helped thousands of patients recover from conditions ranging from chronic sinusitis to complex ear surgeries, offering precision care with outstanding results.',
    'awards': ['Member — Association of Otolaryngologists of India', 'Fellowship in Head & Neck Surgery', 'Advanced Training in Functional Endoscopic Sinus Surgery (FESS)'],
    'treats': ['Chronic Sinusitis', 'Ear Infections & Hearing Loss', 'Tonsillitis & Adenoids', 'Nasal Polyps', 'Voice & Throat Disorders', 'Vertigo & Balance Disorders', 'Head & Neck Lumps', 'Sleep Apnoea'],
  },
  {
    'slug': 'shruthi',
    'name': 'Dr. Shruthi',
    'init': 'SH',
    'qual': 'MBBS · MD · DM (Neurology)',
    'dept': 'Neurology',
    'role': 'Consultant Neurologist',
    'exp': '7+ Years',
    'prev': 'Manipal Hospital Mangalore · NIMHANS Bangalore',
    'langs': 'Kannada · English · Hindi',
    'bio': 'Dr. Shruthi is a dedicated neurologist with subspecialty training from NIMHANS, Bangalore — one of India\'s foremost institutes for neuroscience. With 7 years of experience in clinical neurology, she brings deep expertise in the management of stroke, epilepsy and movement disorders. Her patient-centred approach and strong diagnostic acumen make her a valued member of RVR\'s exceptional neurology team.',
    'awards': ['DM Neurology — Trained at NIMHANS Bangalore', 'Member — Neurological Society of India', 'Specialisation in Stroke & Cerebrovascular Disorders'],
    'treats': ['Stroke Management', 'Epilepsy', 'Movement Disorders', 'Peripheral Neuropathy', 'Headache & Migraine', 'Cognitive Disorders', 'Spinal Cord Disorders', 'Neuro-infections'],
  },
  {
    'slug': 'shishir',
    'name': 'Dr. Shishir',
    'init': 'SI',
    'qual': 'MBBS · MD · DM (Neurology)',
    'dept': 'Neurology',
    'role': 'Consultant Neurologist',
    'exp': '6+ Years',
    'prev': 'Kasturba Hospital Manipal · KMC Mangalore',
    'langs': 'Kannada · English · Hindi · Tulu',
    'bio': 'Dr. Shishir is a young, dynamic neurologist who brings contemporary training and a technology-forward mindset to clinical neurology. Having trained at Kasturba Hospital Manipal and KMC Mangalore, two of South India\'s most respected academic medical institutions, he brings strong grounding in both academic and clinical neurology. He is especially skilled in the management of epilepsy, neuromuscular disorders and headache syndromes.',
    'awards': ['DM Neurology — Kasturba Hospital Manipal', 'Member — Indian Epilepsy Society', 'Advanced EEG Interpretation Certified'],
    'treats': ['Epilepsy & Seizures', 'Neuromuscular Disease', 'Headache Disorders', 'Parkinson\'s Disease', 'Sleep Disorders', 'Stroke Follow-up', 'Multiple Sclerosis', 'Nerve & Muscle Diseases'],
  },
  {
    'slug': 'vignesh',
    'name': 'Dr. Vignesh',
    'init': 'VG',
    'qual': 'MBBS · MD · DM (Neurology)',
    'dept': 'Neurology',
    'role': 'Consultant Neurologist',
    'exp': '5+ Years',
    'prev': 'Sri Ramachandra Medical College Chennai · Apollo Hospitals Chennai',
    'langs': 'Kannada · English · Tamil · Hindi',
    'bio': 'Dr. Vignesh trained at Sri Ramachandra Medical College, Chennai and completed his superspeciality neurology training with exposure at Apollo Hospitals. He brings a fresh, research-driven perspective to neurology practice with particular interest in interventional neurology and neurocritical care. Dr. Vignesh is committed to raising the standard of neurological care in Coastal Karnataka through evidence-based medicine and patient education.',
    'awards': ['DM Neurology — Sri Ramachandra Medical College, Chennai', 'Member — Neurological Society of India', 'Training in Neurocritical Care — Apollo Hospitals Chennai'],
    'treats': ['Neurocritical Care', 'Stroke Intervention', 'Guillain-Barré Syndrome', 'Myasthenia Gravis', 'Brain & Spine Infections', 'Autoimmune Neurology', 'Memory & Dementia', 'Headache Management'],
  },
]

DIRECTORS = [
  {
    'slug': 'vijay',
    'name': 'Vijay M.N. Shetty',
    'init': 'VS',
    'role': 'Chairman & Managing Director',
    'bio': 'Vijay M.N. Shetty is the visionary founder of RVR Super Speciality Centre. A seasoned entrepreneur and healthcare advocate from Mangalore, he founded RVR with a singular mission — to ensure that every person from Coastal Karnataka has access to the most advanced medical care without having to travel away from home. Under his leadership, RVR has been built as an institution that combines world-class clinical excellence with genuine compassion for every patient.',
    'vision': 'To build India\'s most patient-centric super speciality healthcare ecosystem, starting from Mangalore and growing across the country.',
    'quals': 'Entrepreneur · Healthcare Visionary · Business Leader',
  },
  {
    'slug': 'raghavendra-director',
    'name': 'Dr. Raghavendra B.S.',
    'init': 'RB',
    'role': 'Director & Senior Consultant Neurologist',
    'bio': 'Dr. Raghavendra B.S. brings dual leadership to RVR — as a founding Director and as the Senior Consultant Neurologist heading the Department of Neurology. His deep clinical expertise combined with institutional leadership ensures that RVR\'s medical standards are set at the highest level from day one. Professor & HOD of Neurology at Father Muller Medical College, he is one of the most distinguished neurologists in Coastal Karnataka.',
    'vision': 'To establish RVR as a centre of neurological excellence that is recognised nationally and contributes to the global body of medical knowledge.',
    'quals': 'MBBS · MD · DM (Neurology) · Professor & HOD, Father Muller Medical College',
  },
  {
    'slug': 'ananth',
    'name': 'Ananth Shidlaghatta Narayanarao',
    'init': 'AN',
    'role': 'Director — Operations & Strategy',
    'bio': 'Ananth Shidlaghatta Narayanarao is a strategic leader who brings operational excellence and business acumen to RVR. With a strong background in healthcare administration and institutional building, he oversees the operational, financial and strategic pillars of RVR\'s growth. His focus on building sustainable, scalable systems ensures that RVR operates with the precision and efficiency of a world-class healthcare organisation.',
    'vision': 'To build operational excellence into every layer of RVR — so that the quality of care is consistent, the systems are transparent and the organisation grows with integrity.',
    'quals': 'Business Leader · Healthcare Operations & Strategy Expert',
  },
]

SERVICES = [
  {'slug':'neurology','name':'Neurology','icon':'🧠','tagline':'Advanced Brain & Spine Care','color':'#1a6644',
   'desc':'RVR\'s Neurology department is the strongest in Coastal Karnataka — with four dedicated DM-qualified neurologists, advanced diagnostic technology and a multidisciplinary approach to brain and spine care.',
   'long':'The brain and nervous system are among the most complex and critical systems of the human body. At RVR Super Speciality Centre, our neurology department is staffed by four DM-qualified neurologists with training from India\'s premier institutions. We offer comprehensive diagnosis and treatment for the full spectrum of neurological conditions — from common headache disorders to complex stroke care, epilepsy management and rare autoimmune neurological conditions. Our department is equipped with advanced neurological diagnostic tools including EEG, EMG, nerve conduction studies and neuroimaging, enabling precise diagnosis and targeted treatment for every patient.',
   'treats':['Stroke & TIA','Epilepsy & Seizures','Parkinson\'s Disease','Multiple Sclerosis','Headache & Migraine','Cerebrovascular Disease','Dementia & Memory Disorders','Guillain-Barré Syndrome','Myasthenia Gravis','Brain & Spinal Cord Infections','Peripheral Neuropathy','Movement Disorders'],
  },
  {'slug':'cardiology','name':'Cardiology','icon':'❤️','tagline':'Comprehensive Heart Care','color':'#1a5280',
   'desc':'Our Cardiology department provides full-spectrum cardiac care — from preventive screening to advanced diagnostics and management of complex heart conditions.',
   'long':'Heart disease is the leading cause of death in India. At RVR Super Speciality Centre, our Cardiology department is built to provide the people of Coastal Karnataka with world-class cardiac care close to home. Our cardiologist brings extensive training in both interventional and non-interventional cardiology, supported by advanced diagnostic equipment including echocardiography, stress testing and Holter monitoring. Whether you need a routine cardiac check-up or management of a complex cardiac condition, our team is equipped to deliver precise, compassionate care at every step.',
   'treats':['Coronary Artery Disease','Heart Failure','Cardiac Arrhythmias','Hypertension','Echocardiography','Stress Testing','Lipid Disorders','Preventive Cardiology','Chest Pain Evaluation','Heart Attack Recovery'],
  },
  {'slug':'diagnostics','name':'Advanced Diagnostics','icon':'🔬','tagline':'Precision Diagnostics — Results on WhatsApp','color':'#5a3e8a',
   'desc':'State-of-the-art laboratory and imaging services with digital report delivery directly to your phone.',
   'long':'Accurate diagnosis is the foundation of effective treatment. RVR\'s Advanced Diagnostics department combines cutting-edge laboratory technology with modern radiology and digital report delivery to give patients fast, accurate and accessible diagnostic results. Our in-house laboratory processes a comprehensive range of tests with rapid turnaround times. Lab reports are delivered digitally to your WhatsApp and email — so you receive your results the moment they are ready, wherever you are.',
   'treats':['Complete Blood Count','Blood Chemistry Panel','Lipid Profile','Liver Function Tests','Kidney Function Tests','Thyroid Function Tests','HbA1c & Diabetes Screening','Urine Analysis','X-Ray','Ultrasound','ECG & Echo','CT Scan','MRI','EEG & EMG','Nerve Conduction Studies'],
  },
  {'slug':'emergency','name':'Emergency Medicine','icon':'🚨','tagline':'24/7 Emergency Care','color':'#8a2020',
   'desc':'Round-the-clock emergency care with rapid response protocols and immediate specialist availability.',
   'long':'Medical emergencies do not follow a schedule. RVR Super Speciality Centre\'s Emergency department operates 24 hours a day, 7 days a week, 365 days a year with a fully trained emergency team and immediate access to specialist consultants across all departments. Our emergency protocols are designed for rapid triage, stabilisation and treatment — ensuring that critical patients receive the right care within the critical golden hour. Our emergency bay is equipped with advanced life support equipment, cardiac monitoring, ventilators and emergency medication, ready for any situation.',
   'treats':['Stroke Emergency','Cardiac Arrest & Chest Pain','Seizures & Status Epilepticus','Severe Trauma','Breathing Difficulties','Acute Poisoning','High Fever & Sepsis','Unconsciousness','Severe Allergic Reactions','Road Traffic Accidents'],
  },
  {'slug':'surgery','name':'Surgical Sciences','icon':'⚕️','tagline':'Minimally Invasive Precision Surgery','color':'#2a6644',
   'desc':'Advanced general and laparoscopic surgery with state-of-the-art operation theatres and rapid recovery protocols.',
   'long':'Surgical treatment at RVR Super Speciality Centre is delivered with the precision, safety and care that every patient deserves. Our surgical department specialises in both open and minimally invasive laparoscopic procedures, offering patients faster recovery, less pain and fewer complications compared to traditional surgery. Our operation theatres are equipped with advanced surgical instrumentation, anaesthesia technology and infection control systems that meet international standards.',
   'treats':['Laparoscopic Cholecystectomy','Appendectomy','Hernia Repair','Thyroid & Parathyroid Surgery','Colorectal Surgery','Abdominal Surgery','Emergency Surgery','Wound Care & Management','Minor Surgical Procedures','Pre & Post-operative Care'],
  },
  {'slug':'radiology','name':'Radiology & Imaging','icon':'📡','tagline':'Advanced Imaging — Precise Reports','color':'#1a4a6a',
   'desc':'Full-spectrum radiology services with advanced imaging technology and timely digital report delivery.',
   'long':'Imaging is at the heart of modern medicine. RVR\'s Radiology department is equipped with advanced imaging modalities that provide the clearest possible picture of your condition, enabling our specialists to make accurate diagnoses and plan precise treatments. All radiology reports are prepared by experienced radiologists and delivered digitally — so your doctor has the information needed to act quickly and effectively.',
   'treats':['X-Ray','Ultrasound','CT Scan','MRI','Echocardiography','Doppler Studies','Mammography','Bone Density Scan (DEXA)','Fluoroscopy','Interventional Radiology'],
  },
  {'slug':'pharmacy','name':'Pharmacy','icon':'💊','tagline':'In-House Pharmacy — Prescriptions on WhatsApp','color':'#2a5a3a',
   'desc':'Fully stocked in-house pharmacy with digital prescription routing and WhatsApp medicine reminders.',
   'long':'RVR\'s in-house pharmacy is seamlessly integrated with our hospital management system — the moment your doctor approves a prescription, it is automatically routed to pharmacy for preparation. You receive your medication reminder and refill schedule directly on WhatsApp, so you never miss a dose. Our pharmacy stocks a comprehensive range of medications across all specialities available at RVR, and is managed by qualified pharmacists who are available to answer your questions.',
   'treats':['Neurology Medications','Cardiac Medications','Diabetes & Endocrine','Antibiotics & Anti-infectives','Oncology Support Medications','Pain Management','Vitamins & Supplements','IV Fluids & Injectables','Emergency Medications','General Medications'],
  },
  {'slug':'wellness','name':'Wellness & Prevention','icon':'🌿','tagline':'Preventive Care for a Healthier Life','color':'#3a6a1a',
   'desc':'Comprehensive health screenings and preventive care packages designed to keep you healthy before illness strikes.',
   'long':'The best time to address a health condition is before it becomes one. RVR\'s Wellness & Prevention department is built around the belief that proactive health management saves lives and improves quality of life. Our preventive care packages are designed for individuals of every age — from young adults seeking a baseline health assessment to seniors requiring comprehensive annual screenings. Early detection of conditions like diabetes, hypertension, cardiac risk and neurological changes enables timely intervention and better outcomes.',
   'treats':['Annual Health Check-up Packages','Executive Health Screening','Cardiac Risk Assessment','Diabetes Screening & Prevention','Neurological Wellness Assessment','Blood Pressure Management','Cholesterol Monitoring','Bone Health Assessment','Vision & Hearing Screening','Nutrition & Lifestyle Counselling'],
  },
]

# ════════════════════════════════════════════════════════════════════
# PAGE BUILDERS
# ════════════════════════════════════════════════════════════════════

def countdown_section():
    return '''<section style="display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--wa)">
  <div style="background:var(--p);display:flex;flex-direction:column;justify-content:center;padding:5rem 4rem;border-right:1px solid var(--wa)" class="reveal">
    <div style="font-size:.54rem;letter-spacing:.4em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem">Grand Opening Countdown</div>
    <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.4rem,2.5vw,2.2rem);line-height:1.2;color:var(--k);margin-bottom:1.5rem">The wait ends<br>April 23, 2026</div>
    <div style="font-size:.7rem;letter-spacing:.1em;color:var(--d);line-height:1.6">Falnir, Ayush Building<br>Mangalore, Karnataka — 575001</div>
  </div>
  <div style="background:var(--w);display:flex;align-items:center;justify-content:center;padding:4rem" class="reveal">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--wa);border:1px solid var(--wa);width:100%">
      <div style="background:var(--w);padding:3rem 2rem;text-align:center"><span id="cd1" style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2.5rem,4.5vw,4rem);color:var(--k);line-height:1;display:block;letter-spacing:-.03em">00</span><span style="font-size:.5rem;letter-spacing:.3em;text-transform:uppercase;color:var(--d);display:block;margin-top:.6rem">Days</span></div>
      <div style="background:var(--w);padding:3rem 2rem;text-align:center"><span id="cd2" style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2.5rem,4.5vw,4rem);color:var(--k);line-height:1;display:block;letter-spacing:-.03em">00</span><span style="font-size:.5rem;letter-spacing:.3em;text-transform:uppercase;color:var(--d);display:block;margin-top:.6rem">Hours</span></div>
      <div style="background:var(--w);padding:3rem 2rem;text-align:center"><span id="cd3" style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2.5rem,4.5vw,4rem);color:var(--k);line-height:1;display:block;letter-spacing:-.03em">00</span><span style="font-size:.5rem;letter-spacing:.3em;text-transform:uppercase;color:var(--d);display:block;margin-top:.6rem">Minutes</span></div>
      <div style="background:var(--w);padding:3rem 2rem;text-align:center"><span id="cd4" style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2.5rem,4.5vw,4rem);color:var(--k);line-height:1;display:block;letter-spacing:-.03em">00</span><span style="font-size:.5rem;letter-spacing:.3em;text-transform:uppercase;color:var(--d);display:block;margin-top:.6rem">Seconds</span></div>
    </div>
  </div>
</section>'''

def notify_section():
    return '''<section id="ntfy" style="background:var(--g);padding:7rem 3rem;display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:center">
  <div>
    <div style="font-size:.54rem;letter-spacing:.4em;text-transform:uppercase;color:rgba(255,255,255,.45);margin-bottom:1.5rem" class="reveal">Opening April 23, 2026</div>
    <h2 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2rem,4vw,3.8rem);line-height:1.1;letter-spacing:-.02em;color:#fff;margin-bottom:1.5rem" class="reveal">Be the first<br>to book.</h2>
    <p style="font-size:.9rem;color:rgba(255,255,255,.6);line-height:1.85;max-width:380px" class="reveal">Leave your WhatsApp number. We will message you on April 23, 2026 with our first appointment booking link — before anyone else.</p>
  </div>
  <div class="reveal-r">
    <div style="font-size:.54rem;letter-spacing:.32em;text-transform:uppercase;color:rgba(255,255,255,.45);margin-bottom:.9rem">Your WhatsApp number</div>
    <form id="nsub" class="ntfm" style="display:flex;border:1.5px solid rgba(255,255,255,.2);margin-bottom:.75rem;transition:border-color .3s">
      <input type="tel" class="ntip" id="ph" placeholder="+91 98765 43210" style="flex:1;background:transparent;border:none;outline:none;padding:.88rem 1.1rem;font-family:'DM Sans',sans-serif;font-size:.85rem;color:#fff">
      <button type="submit" style="background:rgba(255,255,255,.15);border:none;padding:.88rem 1.6rem;cursor:none;font-family:'DM Sans',sans-serif;font-size:.58rem;font-weight:500;letter-spacing:.18em;text-transform:uppercase;color:#fff;transition:background .3s">Notify Me</button>
    </form>
    <div class="ntnt" style="font-size:.6rem;color:rgba(255,255,255,.3)">No spam. Only RVR launch updates.</div>
    <div id="ok" style="display:none;font-size:.88rem;color:rgba(255,255,255,.8);padding:.5rem 0">✓ &nbsp;You are on the list. We will message you on April 23, 2026.</div>
  </div>
</section>'''

def strip_html():
    items = ['Neurology','Cardiology','Advanced Diagnostics','Super Speciality','Emergency Medicine','World-Class Care','Opening April 23 · 2026','Falnir, Mangalore']
    html = '<div class="strip"><div class="strip-in">'
    for i in range(2):
        for it in items:
            html += f'<div class="si"><span class="d">◆</span>{it}</div>'
    html += '</div></div>'
    return html

# ── INDEX.HTML ──────────────────────────────────────────────────────
def build_index():
    svc_cards = ''
    for s in SERVICES:
        svc_cards += f'''<a href="service-{s['slug']}.html" style="background:var(--p);display:block;text-decoration:none;overflow:hidden;position:relative;cursor:none" data-hover>
  <div style="padding:2.5rem 2rem 1.5rem">
    <div style="font-size:1.8rem;margin-bottom:1rem">{s['icon']}</div>
    <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:.95rem;color:var(--k);margin-bottom:.5rem;line-height:1.3">{s['name']}</div>
    <div style="font-size:.65rem;color:var(--d);line-height:1.6;margin-bottom:1.5rem">{s['tagline']}</div>
  </div>
  <div style="padding:.75rem 2rem;border-top:1px solid var(--wa);font-size:.55rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g);display:flex;align-items:center;gap:.5rem;transition:gap .3s">Learn more <span>→</span></div>
</a>'''

    doc_cards = ''
    for d in DOCTORS:
        doc_cards += f'''<a href="doctor-{d['slug']}.html" style="background:var(--p);display:block;text-decoration:none;cursor:none;overflow:hidden;transition:background .3s" data-hover>
  <div style="aspect-ratio:1/1;display:flex;align-items:center;justify-content:center;position:relative;background:var(--p)">
    <span style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:3rem;color:rgba(14,14,14,.07);letter-spacing:-.04em">{d['init']}</span>
    <div style="position:absolute;bottom:.7rem;left:.7rem;font-size:.45rem;letter-spacing:.2em;text-transform:uppercase;background:var(--g);color:#fff;padding:.2rem .5rem">{d['dept']}</div>
  </div>
  <div style="padding:1.2rem 1.2rem 1.5rem;border-top:2px solid transparent;transition:border-color .3s">
    <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:.82rem;color:var(--k);margin-bottom:.25rem;line-height:1.3">{d['name']}</div>
    <div style="font-size:.56rem;letter-spacing:.06em;color:var(--g);margin-bottom:.15rem">{d['qual']}</div>
    <div style="font-size:.62rem;color:var(--d)">{d['role']}</div>
  </div>
</a>'''

    body = f'''
<style>
#hero{{height:100vh;min-height:700px;display:grid;grid-template-columns:55fr 45fr;overflow:hidden;margin-top:0}}
.hl{{background:var(--p);display:flex;flex-direction:column;justify-content:flex-end;padding:0 5rem 6rem}}
.hr{{background:var(--g);display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}}
.hr::before{{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 59px,rgba(255,255,255,.03) 59px,rgba(255,255,255,.03) 60px)}}
.hr-wm{{position:absolute;font-family:'Unbounded',sans-serif;font-weight:200;font-size:22vw;color:rgba(255,255,255,.025);line-height:1;letter-spacing:-.04em;bottom:-4vw;right:-1vw;pointer-events:none}}
.hicon{{width:min(300px,60%);position:relative;z-index:2;color:rgba(255,255,255,.82);animation:fadeIn 1.2s .3s ease both}}
.hlbl{{font-size:.56rem;letter-spacing:.42em;text-transform:uppercase;color:var(--g);margin-bottom:2.2rem;display:flex;align-items:center;gap:.8rem;animation:fadeUp .7s .1s ease both}}
.hlbl::before{{content:'';display:block;width:28px;height:1px;background:var(--g)}}
h1{{font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2.8rem,5.5vw,6.5rem);line-height:1.05;letter-spacing:-.025em;margin-bottom:2.8rem;overflow:hidden}}
h1 .ln{{display:block;overflow:hidden}}
h1 .w1{{display:inline-block;animation:wUp .85s .2s cubic-bezier(.22,1,.36,1) both}}
h1 .w2{{display:inline-block;animation:wUp .85s .35s cubic-bezier(.22,1,.36,1) both}}
h1 .w3{{display:inline-block;animation:wUp .85s .5s cubic-bezier(.22,1,.36,1) both}}
h1 em{{font-style:normal;color:var(--g)}}
.hsubwrap{{max-width:380px;animation:fadeUp .7s .8s ease both}}
.hsub{{font-size:.92rem;color:var(--d);line-height:1.85;margin-bottom:2.5rem}}
.hsub strong{{color:var(--k);font-weight:400}}
.hbtns{{display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap}}
.hbp{{font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:#fff;background:var(--g);border:none;padding:.82rem 2.2rem;cursor:none;font-family:'DM Sans',sans-serif;font-weight:500;transition:background .25s;text-decoration:none;display:inline-block}}
.hbp:hover{{background:var(--k)}}
.hbs{{font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g);background:none;border:1.5px solid var(--g);padding:.8rem 2rem;cursor:none;font-family:'DM Sans',sans-serif;font-weight:500;display:inline-block;text-decoration:none;transition:background .25s,color .25s}}
.hbs:hover{{background:var(--g);color:#fff}}
@media(max-width:900px){{
  #hero{{grid-template-columns:1fr}}
  .hr{{display:none}}
  .hl{{padding:0 1.5rem 4rem;min-height:100vh}}
  h1{{font-size:clamp(2.5rem,10vw,4rem)}}
}}
</style>

<section id="hero">
  <div class="hl">
    <div class="hlbl">Opening April 23, 2026 — Falnir, Mangalore</div>
    <h1>
      <span class="ln"><span class="w1">Mangalore</span></span>
      <span class="ln"><span class="w2">never had</span></span>
      <span class="ln"><span class="w3"><em>this</em> before.</span></span>
    </h1>
    <div class="hsubwrap">
      <p class="hsub"><strong>RVR Super Speciality Centre</strong> — the most advanced hospital in Coastal Karnataka. Neurology, Cardiology and Super Speciality care by India's finest specialists. Right here in Mangalore.</p>
      <div class="hbtns">
        <a href="#ntfy" class="hbp">Book Your Appointment</a>
        <a href="about.html" class="hbs">Discover RVR →</a>
      </div>
    </div>
  </div>
  <div class="hr">
    <div class="hicon">{ICON}</div>
    <div class="hr-wm">RVR</div>
    <div style="position:absolute;bottom:2rem;left:2.5rem;font-size:.5rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.25)">RVR Super Speciality Centre</div>
    <div style="position:absolute;top:2rem;right:2.5rem;font-family:'Unbounded',sans-serif;font-weight:200;font-size:.7rem;letter-spacing:.12em;color:rgba(255,255,255,.28)">Est. 2026</div>
  </div>
</section>

{strip_html()}
{countdown_section()}

<!-- ABOUT TEASER -->
<section style="padding:8rem 3rem;display:grid;grid-template-columns:.9fr 1fr;gap:6rem;align-items:center;border-top:1px solid var(--wa)">
  <div>
    <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:7rem;color:var(--wa);line-height:1;letter-spacing:-.04em;margin-bottom:1.5rem" class="reveal-l">01</div>
    <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1rem" class="reveal-l">About RVR</div>
    <h2 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.8rem,3.2vw,3rem);line-height:1.1;letter-spacing:-.02em" class="reveal-l">Born in Mangalore.<br><span style="color:var(--g)">Built for everyone.</span></h2>
  </div>
  <div>
    <p style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1rem,1.5vw,1.2rem);line-height:1.7;color:var(--k);margin-bottom:2rem" class="reveal">For too long, people from Coastal Karnataka had to travel to Bangalore, Chennai or Mumbai for advanced medical care. Leaving their families behind. Spending weeks away from home.</p>
    <p style="font-size:.9rem;color:var(--d);line-height:1.9;margin-bottom:2.5rem" class="reveal">RVR Super Speciality Centre was built to change that — permanently. World-class specialists, cutting-edge technology and a deeply human approach to care. All of it, right here in Mangalore.</p>
    <a href="about.html" style="font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g);text-decoration:none;display:inline-flex;align-items:center;gap:.5rem;border-bottom:1px solid rgba(26,102,68,.3);padding-bottom:.3rem;transition:gap .25s" class="reveal" data-hover>Know Our Story →</a>
  </div>
</section>

<!-- SERVICES -->
<section style="background:var(--p);padding:8rem 3rem;border-top:1px solid var(--wa)">
  <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:4rem;gap:2rem;flex-wrap:wrap">
    <div>
      <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1rem" class="reveal">02 — Specialities</div>
      <h2 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.8rem,3.5vw,3.2rem);line-height:1.1;letter-spacing:-.02em" class="reveal">Super speciality<br><span style="color:var(--g)">departments</span></h2>
    </div>
    <a href="services.html" class="reveal" style="font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g);text-decoration:none;display:inline-flex;align-items:center;gap:.5rem;white-space:nowrap" data-hover>View all specialities →</a>
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2px">
    {svc_cards}
  </div>
</section>

<!-- DOCTORS -->
<section style="padding:8rem 3rem;border-top:1px solid var(--wa)">
  <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:4rem;gap:2rem;flex-wrap:wrap">
    <div>
      <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1rem" class="reveal">03 — The Team</div>
      <h2 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.8rem,3.5vw,3.2rem);line-height:1.1;letter-spacing:-.02em" class="reveal">Meet the <span style="color:var(--g)">specialists</span></h2>
    </div>
    <a href="doctors.html" class="reveal" style="font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g);text-decoration:none;white-space:nowrap" data-hover>All doctors →</a>
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2px">
    {doc_cards}
  </div>
</section>

<!-- VISION MISSION -->
<section style="background:var(--k);padding:8rem 3rem;display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:start">
  <div class="reveal-l">
    <div style="font-size:.54rem;letter-spacing:.4em;text-transform:uppercase;color:var(--m);margin-bottom:2rem">04 — Our Vision</div>
    <h3 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:1rem">Vision</h3>
    <p style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.3rem,2.2vw,1.9rem);line-height:1.45;color:#fff;margin-bottom:3rem">To be the most trusted name in super speciality healthcare — where every patient, regardless of background, receives the highest standard of medical care with dignity and compassion.</p>
    <h3 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:1rem">Mission</h3>
    <p style="font-size:.92rem;color:rgba(255,255,255,.55);line-height:1.9">To deliver world-class clinical excellence through outstanding specialists, advanced technology and a patient-first culture — making superior healthcare accessible to everyone who needs it.</p>
  </div>
  <div class="reveal-r">
    <div style="border-left:1px solid rgba(255,255,255,.1);padding-left:4rem">
      <div style="font-size:.54rem;letter-spacing:.4em;text-transform:uppercase;color:var(--m);margin-bottom:2rem">Why RVR is Different</div>
      {chr(10).join([f'<div style="padding:1.5rem 0;border-bottom:1px solid rgba(255,255,255,.08)">'
                    f'<div style="font-family:\'Unbounded\',sans-serif;font-weight:200;font-size:.92rem;color:#fff;margin-bottom:.4rem">{title}</div>'
                    f'<div style="font-size:.72rem;color:rgba(255,255,255,.38);line-height:1.6">{desc}</div>'
                    f'</div>'
                    for title, desc in [
                        ("4 DM-Qualified Neurologists", "The strongest neurology team in Coastal Karnataka — under one roof."),
                        ("AI-Powered Clinical Notes", "Doctors spend more time with patients, not paperwork."),
                        ("Reports on WhatsApp", "Lab results, discharge summaries and prescriptions delivered to your phone."),
                        ("No More Travelling to Bangalore", "Advanced super speciality care — right here in Mangalore."),
                        ("Transparent Doctor Payouts", "Every doctor sees their earnings in real time. Full transparency."),
                    ]])}
    </div>
  </div>
</section>

{notify_section()}'''
    return wrap("Home", "RVR Super Speciality Centre — Mangalore's most advanced hospital. Opening April 23, 2026.", '', body)

# ── ABOUT.HTML ──────────────────────────────────────────────────────
def build_about():
    dir_cards = ''
    for d in DIRECTORS:
        dir_cards += f'''<a href="director-{d['slug']}.html" style="background:var(--p);display:block;text-decoration:none;cursor:none;padding:2.5rem;border-bottom:2px solid transparent;transition:border-color .3s,background .3s" data-hover>
  <div style="width:56px;height:56px;border-radius:50%;background:var(--g);display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem">
    <span style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:.9rem;color:#fff;letter-spacing:.05em">{d['init']}</span>
  </div>
  <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:.95rem;color:var(--k);margin-bottom:.4rem;line-height:1.3">{d['name']}</div>
  <div style="font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g);margin-bottom:1rem">{d['role']}</div>
  <div style="font-size:.75rem;color:var(--d);line-height:1.7">{d['bio'][:180]}...</div>
  <div style="font-size:.55rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g);margin-top:1.5rem;display:flex;align-items:center;gap:.4rem">View Profile →</div>
</a>'''

    body = f'''
<div style="padding-top:5.5rem"></div>
<section style="background:var(--g);padding:8rem 3rem">
  <div style="font-size:.54rem;letter-spacing:.42em;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:1.5rem;animation:fadeUp .7s .1s ease both">About RVR</div>
  <h1 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2.5rem,5.5vw,6rem);line-height:1.05;letter-spacing:-.025em;color:#fff;max-width:800px;animation:fadeUp .8s .25s ease both">Born in Mangalore.<br><span style="color:var(--m)">Built for everyone.</span></h1>
</section>

<section style="padding:8rem 3rem;display:grid;grid-template-columns:.9fr 1fr;gap:6rem;align-items:start;border-top:1px solid var(--wa)">
  <div class="reveal-l">
    <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:6rem;color:var(--wa);line-height:1;letter-spacing:-.04em;margin-bottom:1.5rem">01</div>
    <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1rem">Our Story</div>
    <h2 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.6rem,2.8vw,2.5rem);line-height:1.15">Why RVR<br><span style="color:var(--g)">exists</span></h2>
  </div>
  <div>
    <p style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1rem,1.5vw,1.2rem);line-height:1.7;color:var(--k);margin-bottom:2rem" class="reveal">For generations, families from Coastal Karnataka had to make a painful choice — travel far from home for advanced medical care, or stay and make do with what was available locally.</p>
    <p style="font-size:.9rem;color:var(--d);line-height:1.9;margin-bottom:1.5rem" class="reveal">RVR Super Speciality Centre was built to end that choice permanently. To bring the same quality of care available in India's metro cities to the doorstep of every family in Mangalore and Coastal Karnataka.</p>
    <p style="font-size:.9rem;color:var(--d);line-height:1.9;margin-bottom:2.5rem" class="reveal">Built by a team of visionary doctors and business leaders who believe that geography should never determine the quality of care a person receives — RVR represents a new chapter in healthcare for this region.</p>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--wa);border-left:1px solid var(--wa);margin-top:2rem" class="reveal">
      {''.join([f'<div style="padding:1.5rem 1.2rem;border-right:1px solid var(--wa);border-bottom:1px solid var(--wa)"><div style="font-family:\'Unbounded\',sans-serif;font-weight:200;font-size:2rem;color:var(--g);line-height:1;margin-bottom:.3rem">{n}</div><div style="font-size:.58rem;letter-spacing:.06em;color:var(--d);line-height:1.4">{l}</div></div>' for n,l in [('8+','Specialists'),('4','Neurologists'),('3','Founders'),('1','Mission')]])}
    </div>
  </div>
</section>

<!-- VISION MISSION -->
<section style="background:var(--p);padding:7rem 3rem;border-top:1px solid var(--wa);display:grid;grid-template-columns:1fr 1fr;gap:5rem">
  <div class="reveal">
    <div style="font-size:.54rem;letter-spacing:.4em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem">Vision</div>
    <p style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.3rem,2.2vw,1.9rem);line-height:1.45;color:var(--k)">To be the most trusted name in super speciality healthcare — where every patient receives the highest standard of care with dignity and compassion.</p>
  </div>
  <div class="reveal">
    <div style="font-size:.54rem;letter-spacing:.4em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem">Mission</div>
    <p style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.3rem,2.2vw,1.9rem);line-height:1.45;color:var(--k)">To deliver world-class clinical excellence through outstanding specialists, advanced technology and a patient-first culture — making superior healthcare accessible to everyone who needs it.</p>
  </div>
</section>

<!-- DIRECTORS -->
<section style="padding:8rem 3rem;border-top:1px solid var(--wa)">
  <div style="margin-bottom:4rem">
    <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1rem" class="reveal">Leadership</div>
    <h2 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.8rem,3.5vw,3.2rem);line-height:1.1;letter-spacing:-.02em" class="reveal">The <span style="color:var(--g)">Directors</span></h2>
    <p style="font-size:.88rem;color:var(--d);margin-top:1rem;max-width:500px" class="reveal">Click on any director to read their full profile, background and vision for RVR.</p>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px">
    {dir_cards}
  </div>
</section>

{notify_section()}'''
    return wrap("About", "Learn about RVR Super Speciality Centre — our story, vision, mission and the leadership team behind Mangalore's most advanced hospital.", 'about', body)

# ── SERVICES.HTML ──────────────────────────────────────────────────
def build_services():
    rows = ''
    for i, s in enumerate(SERVICES):
        rows += f'''<a href="service-{s['slug']}.html" style="display:grid;grid-template-columns:56px 1fr 1fr auto;align-items:center;padding:1.8rem 0;border-bottom:1px solid rgba(14,14,14,.07);cursor:none;gap:2rem;position:relative;overflow:hidden;text-decoration:none" data-hover class="srow">
  <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:.85rem;color:var(--d);position:relative;z-index:1">{str(i+1).zfill(2)}</div>
  <div style="font-size:1rem;font-weight:500;letter-spacing:.02em;color:var(--k);position:relative;z-index:1">{s['name']}</div>
  <div style="font-size:.72rem;color:var(--d);position:relative;z-index:1">{s['tagline']}</div>
  <div style="font-size:.72rem;color:var(--g);position:relative;z-index:1;white-space:nowrap">View →</div>
</a>'''

    body = f'''
<style>
.srow::after{{content:'';position:absolute;left:-3rem;right:-3rem;top:0;bottom:0;background:var(--g);transform:scaleX(0);transform-origin:left;transition:transform .4s cubic-bezier(.23,1,.32,1);z-index:0}}
.srow:hover::after{{transform:scaleX(1)}}
.srow:hover div{{color:rgba(255,255,255,.75)!important}}
</style>
<div style="padding-top:5.5rem"></div>
<section style="background:var(--p);padding:8rem 3rem">
  <div style="font-size:.54rem;letter-spacing:.42em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem;animation:fadeUp .7s .1s ease both">Specialities</div>
  <h1 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2.5rem,5.5vw,6rem);line-height:1.05;letter-spacing:-.025em;color:var(--k);animation:fadeUp .8s .25s ease both">Super Speciality<br><span style="color:var(--g)">Departments</span></h1>
</section>
<section style="padding:5rem 3rem;border-top:1px solid rgba(14,14,14,.08)">
  <p style="font-size:.9rem;color:var(--d);line-height:1.85;max-width:600px;margin-bottom:4rem" class="reveal">Every department at RVR is staffed by specialists trained at India's leading institutions and equipped with the most advanced diagnostic and treatment technology in Coastal Karnataka.</p>
  <div style="border-top:1px solid rgba(14,14,14,.1)">{rows}</div>
</section>
{notify_section()}'''
    return wrap("Specialities", "RVR Super Speciality Centre departments — Neurology, Cardiology, Emergency Medicine, Surgery, Diagnostics and more.", 'services', body)

# ── SERVICE DETAIL PAGES ────────────────────────────────────────────
def build_service(s):
    treats = ''.join([f'<div style="padding:1rem 1.2rem;background:var(--p);border-left:2px solid var(--g)">'
                      f'<div style="font-size:.8rem;font-weight:400;color:var(--k)">{t}</div>'
                      f'</div>' for t in s['treats']])
    other_svcs = ''.join([f'<a href="service-{o["slug"]}.html" style="font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g);text-decoration:none;padding:.5rem 1rem;border:1px solid rgba(26,102,68,.25);display:inline-block;transition:background .25s,color .25s" data-hover>{o["name"]}</a>'
                          for o in SERVICES if o['slug'] != s['slug']])
    body = f'''
<div style="padding-top:5.5rem"></div>
<section style="background:var(--g);padding:8rem 3rem">
  <a href="services.html" style="font-size:.54rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.4);text-decoration:none;display:inline-flex;align-items:center;gap:.5rem;margin-bottom:2rem;animation:fadeIn .5s ease both">← All Specialities</a>
  <div style="font-size:2.5rem;margin-bottom:1rem;animation:fadeUp .6s .1s ease both">{s['icon']}</div>
  <h1 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2.5rem,5.5vw,6rem);line-height:1.05;letter-spacing:-.025em;color:#fff;margin-bottom:1rem;animation:fadeUp .8s .2s ease both">{s['name']}</h1>
  <p style="font-size:1rem;color:rgba(255,255,255,.55);max-width:480px;line-height:1.7;animation:fadeUp .7s .35s ease both">{s['tagline']}</p>
</section>
<section style="padding:8rem 3rem;display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:start;border-top:1px solid var(--wa)">
  <div>
    <p style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1rem,1.6vw,1.25rem);line-height:1.7;color:var(--k);margin-bottom:2rem" class="reveal">{s['desc']}</p>
    <p style="font-size:.9rem;color:var(--d);line-height:1.9;margin-bottom:3rem" class="reveal">{s['long']}</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap" class="reveal">
      <a href="index.html#ntfy" style="font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:#fff;background:var(--g);padding:.82rem 2.2rem;text-decoration:none;font-family:'DM Sans',sans-serif;font-weight:500;display:inline-block;transition:background .25s" data-hover>Book an Appointment</a>
      <a href="doctors.html" style="font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g);border:1.5px solid var(--g);padding:.8rem 2rem;text-decoration:none;font-family:'DM Sans',sans-serif;font-weight:500;display:inline-block;transition:background .25s,color .25s" data-hover>Meet the Doctors</a>
    </div>
  </div>
  <div class="reveal-r">
    <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem">Conditions We Treat</div>
    <div style="display:flex;flex-direction:column;gap:2px">{treats}</div>
  </div>
</section>
<section style="background:var(--p);padding:5rem 3rem;border-top:1px solid var(--wa)">
  <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem" class="reveal">Other Specialities</div>
  <div style="display:flex;gap:.75rem;flex-wrap:wrap" class="reveal">{other_svcs}</div>
</section>
{notify_section()}'''
    return wrap(s['name'], f"RVR {s['name']} department — {s['tagline']}. Advanced care in Mangalore.", 'services', body)

# ── DOCTORS.HTML ────────────────────────────────────────────────────
def build_doctors():
    cards = ''
    for d in DOCTORS:
        cards += f'''<a href="doctor-{d['slug']}.html" style="background:var(--p);display:block;text-decoration:none;cursor:none;transition:background .3s" data-hover>
  <div style="aspect-ratio:1/1;display:flex;align-items:center;justify-content:center;position:relative">
    <span style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:3.5rem;color:rgba(14,14,14,.07);letter-spacing:-.04em">{d['init']}</span>
    <div style="position:absolute;bottom:.7rem;left:.7rem;font-size:.45rem;letter-spacing:.2em;text-transform:uppercase;background:var(--g);color:#fff;padding:.2rem .5rem">{d['dept']}</div>
  </div>
  <div style="padding:1.5rem;border-top:1px solid var(--wa)">
    <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:.9rem;color:var(--k);margin-bottom:.3rem;line-height:1.3">{d['name']}</div>
    <div style="font-size:.57rem;letter-spacing:.07em;color:var(--g);margin-bottom:.2rem">{d['qual']}</div>
    <div style="font-size:.65rem;color:var(--d);margin-bottom:1rem">{d['role']}</div>
    <div style="font-size:.55rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g);display:flex;align-items:center;gap:.4rem">View Profile →</div>
  </div>
</a>'''

    body = f'''
<div style="padding-top:5.5rem"></div>
<section style="background:var(--p);padding:8rem 3rem">
  <div style="font-size:.54rem;letter-spacing:.42em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem;animation:fadeUp .7s .1s ease both">Our Team</div>
  <h1 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2.5rem,5.5vw,6rem);line-height:1.05;letter-spacing:-.025em;color:var(--k);animation:fadeUp .8s .25s ease both">Meet the <span style="color:var(--g)">Specialists</span></h1>
</section>
<section style="padding:5rem 3rem;border-top:1px solid var(--wa)">
  <p style="font-size:.9rem;color:var(--d);line-height:1.85;max-width:600px;margin-bottom:4rem" class="reveal">Every doctor at RVR is a specialist trained at India's foremost medical institutions. Click on any doctor to read their full profile, qualifications, research and areas of expertise.</p>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:2px">{cards}</div>
</section>
{notify_section()}'''
    return wrap("Our Doctors", "Meet the specialist doctors at RVR Super Speciality Centre — neurologists, cardiologists and more.", 'doctors', body)

# ── DOCTOR PROFILE PAGE ─────────────────────────────────────────────
def build_doctor(d):
    awards = ''.join([f'<div style="padding:1rem 0;border-bottom:1px solid var(--wa);display:flex;align-items:flex-start;gap:1rem"><span style="color:var(--g);font-size:.9rem;flex-shrink:0">◆</span><div style="font-size:.82rem;color:var(--d);line-height:1.6">{a}</div></div>' for a in d['awards']])
    treats = ''.join([f'<div style="padding:.85rem 1.2rem;background:var(--p);border-left:2px solid var(--g);font-size:.8rem;color:var(--k)">{t}</div>' for t in d['treats']])
    body = f'''
<div style="padding-top:5.5rem"></div>
<section style="background:var(--g);padding:8rem 3rem;display:grid;grid-template-columns:auto 1fr;gap:5rem;align-items:center">
  <div style="animation:fadeIn .8s .1s ease both">
    <a href="doctors.html" style="font-size:.54rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.4);text-decoration:none;display:inline-flex;align-items:center;gap:.5rem;margin-bottom:3rem">← All Doctors</a>
    <div style="width:140px;height:140px;border-radius:50%;background:rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center">
      <span style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:2.5rem;color:#fff;letter-spacing:.05em">{d['init']}</span>
    </div>
  </div>
  <div style="animation:fadeUp .8s .2s ease both">
    <div style="font-size:.52rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:1rem">{d['dept']}</div>
    <h1 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2rem,4.5vw,4.5rem);line-height:1.05;letter-spacing:-.025em;color:#fff;margin-bottom:.8rem">{d['name']}</h1>
    <div style="font-size:.85rem;color:rgba(255,255,255,.55);margin-bottom:.5rem">{d['qual']}</div>
    <div style="font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--m)">{d['role']}</div>
  </div>
</section>
<section style="padding:7rem 3rem;display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:start;border-top:1px solid var(--wa)">
  <div>
    <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem" class="reveal">About</div>
    <p style="font-size:.95rem;color:var(--d);line-height:1.9;margin-bottom:3rem" class="reveal">{d['bio']}</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:3rem" class="reveal">
      <div style="padding:1.5rem;background:var(--p)">
        <div style="font-size:.52rem;letter-spacing:.28em;text-transform:uppercase;color:var(--g);margin-bottom:.5rem">Experience</div>
        <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:1.4rem;color:var(--k)">{d['exp']}</div>
      </div>
      <div style="padding:1.5rem;background:var(--p)">
        <div style="font-size:.52rem;letter-spacing:.28em;text-transform:uppercase;color:var(--g);margin-bottom:.5rem">Speciality</div>
        <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:1rem;color:var(--k);line-height:1.3">{d['dept']}</div>
      </div>
      <div style="padding:1.5rem;background:var(--p);grid-column:1/-1">
        <div style="font-size:.52rem;letter-spacing:.28em;text-transform:uppercase;color:var(--g);margin-bottom:.5rem">Languages</div>
        <div style="font-size:.82rem;color:var(--d)">{d['langs']}</div>
      </div>
    </div>
    <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1rem" class="reveal">Previous Institutions</div>
    <div style="font-size:.82rem;color:var(--d);line-height:1.8;margin-bottom:3rem" class="reveal">{d['prev']}</div>
    <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1rem" class="reveal">Publications & Awards</div>
    <div class="reveal">{awards}</div>
  </div>
  <div class="reveal-r">
    <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem">Conditions Treated</div>
    <div style="display:flex;flex-direction:column;gap:2px;margin-bottom:3rem">{treats}</div>
    <a href="index.html#ntfy" style="display:block;background:var(--g);padding:1.5rem 2rem;text-decoration:none;text-align:center;transition:background .25s" data-hover>
      <div style="font-size:.55rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.5);margin-bottom:.5rem">Ready to consult?</div>
      <div style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:1rem;color:#fff">Book an Appointment</div>
    </a>
  </div>
</section>
{notify_section()}'''
    return wrap(d['name'], f"{d['name']} — {d['role']} at RVR Super Speciality Centre, Mangalore.", 'doctors', body)

# ── DIRECTOR PROFILE PAGE ────────────────────────────────────────────
def build_director(d):
    body = f'''
<div style="padding-top:5.5rem"></div>
<section style="background:var(--k);padding:8rem 3rem;display:grid;grid-template-columns:auto 1fr;gap:5rem;align-items:center">
  <div style="animation:fadeIn .8s .1s ease both">
    <a href="about.html" style="font-size:.54rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.35);text-decoration:none;display:inline-flex;align-items:center;gap:.5rem;margin-bottom:3rem">← About RVR</a>
    <div style="width:140px;height:140px;border-radius:50%;background:var(--g);display:flex;align-items:center;justify-content:center">
      <span style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:2.5rem;color:#fff;letter-spacing:.05em">{d['init']}</span>
    </div>
  </div>
  <div style="animation:fadeUp .8s .2s ease both">
    <div style="font-size:.52rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.35);margin-bottom:1rem">Director — RVR Super Speciality Centre</div>
    <h1 style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(2rem,4.5vw,4.5rem);line-height:1.05;letter-spacing:-.025em;color:#fff;margin-bottom:.8rem">{d['name']}</h1>
    <div style="font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--m)">{d['role']}</div>
  </div>
</section>
<section style="padding:7rem 3rem;display:grid;grid-template-columns:1fr 1fr;gap:6rem;align-items:start;border-top:1px solid var(--wa)">
  <div>
    <div style="font-size:.54rem;letter-spacing:.38em;text-transform:uppercase;color:var(--g);margin-bottom:1.5rem" class="reveal">Profile</div>
    <p style="font-size:.95rem;color:var(--d);line-height:1.9;margin-bottom:2.5rem" class="reveal">{d['bio']}</p>
    <div style="padding:2rem;background:var(--p);margin-bottom:2rem" class="reveal">
      <div style="font-size:.52rem;letter-spacing:.28em;text-transform:uppercase;color:var(--g);margin-bottom:.8rem">Qualifications</div>
      <div style="font-size:.85rem;color:var(--d)">{d['quals']}</div>
    </div>
  </div>
  <div class="reveal-r">
    <div style="background:var(--g);padding:3rem">
      <div style="font-size:.52rem;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:1.5rem">Personal Vision</div>
      <p style="font-family:'Unbounded',sans-serif;font-weight:200;font-size:clamp(1.1rem,1.8vw,1.5rem);line-height:1.45;color:#fff">"{d['vision']}"</p>
    </div>
    <div style="margin-top:2rem">
      <a href="about.html" style="display:block;border:1.5px solid var(--g);padding:1.2rem 2rem;text-decoration:none;text-align:center;transition:background .25s,color .25s;font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g);font-family:'DM Sans',sans-serif;font-weight:500" data-hover>Meet All Directors</a>
    </div>
  </div>
</section>
{notify_section()}'''
    return wrap(d['name'], f"{d['name']} — {d['role']} at RVR Super Speciality Centre, Mangalore.", 'about', body)

# ════════════════════════════════════════════════════════════════════
# WRITE ALL FILES
# ════════════════════════════════════════════════════════════════════
files = {}
files['index.html']    = build_index()
files['about.html']    = build_about()
files['services.html'] = build_services()
files['doctors.html']  = build_doctors()

for s in SERVICES:
    files[f'service-{s["slug"]}.html'] = build_service(s)

for d in DOCTORS:
    files[f'doctor-{d["slug"]}.html'] = build_doctor(d)

for d in DIRECTORS:
    files[f'director-{d["slug"]}.html'] = build_director(d)

for fname, content in files.items():
    with open(f'/home/claude/rvr-site/{fname}', 'w') as f:
        f.write(content)

print(f"Built {len(files)} pages:")
for k in sorted(files.keys()):
    print(f"  {k} ({len(files[k])//1024}KB)")
