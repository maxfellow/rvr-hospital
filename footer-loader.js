document.addEventListener('DOMContentLoaded', function() {
  // Inject CSS
  var style = document.createElement('style');
  style.textContent = '\
    .fb-wrap { position: fixed; bottom: 2rem; right: 2rem; z-index: 9999; }\
    .fb-btn {\
      display: flex; align-items: center; gap: 0.5rem;\
      background: #25a169ff; color: #fff; border: none; border-radius: 50px;\
      padding: 0.8rem 1.4rem; font-size: 0.9rem; font-weight: 600;\
      cursor: pointer; box-shadow: 0 4px 20px rgba(26,102,68,0.4);\
      transition: all 0.3s ease; font-family: inherit;\
    }\
    .fb-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(26,102,68,0.5); }\
    .fb-btn svg { width: 20px; height: 20px; flex-shrink: 0; }\
    .fb-btn span { display: inline-block; }\
    .fb-overlay {\
      display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5);\
      z-index: 10000; justify-content: center; align-items: center; padding: 1rem;\
    }\
    .fb-wrap.open .fb-overlay { display: flex !important; }\
    .fb-form {\
      background: #fff; border-radius: 16px; box-shadow: 0 8px 40px rgba(0,0,0,0.2);\
      width: 100%; max-width: 380px; max-height: 90vh; overflow-y: auto;\
      animation: fbFadeIn 0.25s ease;\
    }\
    @keyframes fbFadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }\
    .fb-form-head {\
      display: flex; justify-content: space-between; align-items: center;\
      padding: 1rem 1.2rem; border-bottom: 1px solid #eee;\
    }\
    .fb-form-head h3 { margin: 0; font-size: 1.1rem; color: #1a6644; }\
    .fb-close { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #999; line-height: 1; padding: 0 0.2rem; font-family: inherit; }\
    .fb-close:hover { color: #333; }\
    #fb-form-inner { padding: 1rem 1.2rem 1.2rem; }\
    .fb-field { margin-bottom: 0.9rem; }\
    .fb-field label { display: block; font-size: 0.8rem; font-weight: 600; margin-bottom: 0.3rem; color: #555; }\
    .fb-field input, .fb-field select, .fb-field textarea {\
      width: 100%; padding: 0.6rem 0.8rem; border: 1px solid #ddd; border-radius: 8px;\
      font-size: 0.9rem; font-family: inherit; box-sizing: border-box; transition: border 0.2s;\
    }\
    .fb-field input:focus, .fb-field select:focus, .fb-field textarea:focus { outline: none; border-color: #1a6644; }\
    .fb-field textarea { resize: vertical; }\
    .fb-submit {\
      width: 100%; padding: 0.8rem; background: #1a6644; color: #fff; border: none;\
      border-radius: 8px; font-size: 0.95rem; font-weight: 600; cursor: pointer;\
      transition: background 0.2s; font-family: inherit;\
    }\
    .fb-submit:hover { background: #145a3a; }\
    @media(max-width:1200px){.fg{gap:2.5rem;padding:3rem 2.5rem;}}@media(max-width:960px){.fg{display:grid;grid-template-columns:1fr 1fr;gap:2rem;padding:2.5rem 2rem;}.ficons{display:flex;flex-wrap:wrap;gap:.7rem;}.ficon{width:2.5rem;height:2.5rem;display:flex;align-items:center;justify-content:center;}.fct{font-size:.9rem;margin-bottom:.8rem;}.fl{font-size:.8rem;line-height:1.5;}.f-desc{font-size:.8rem;line-height:1.7;}.fbot{padding:1rem 2rem;gap:.6rem;}}@media(max-width:768px){.fg{grid-template-columns:1fr;gap:2rem;padding:2.4rem 1.8rem;}.ficons{display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1rem;}.flinks{display:flex;flex-direction:column;gap:.55rem;}.fbot{display:flex;flex-direction:column;align-items:center;text-align:center;gap:.5rem;padding:1rem 1.5rem;}}@media(max-width:600px){.fg{padding:2.2rem 1.4rem;gap:1.8rem;text-align:left;}.ficon{width:2.5rem;height:2.5rem;display:flex;align-items:center;justify-content:center;}.fct{font-size:.88rem;}.fl{font-size:.82rem;line-height:1.5;}.f-desc{font-size:.82rem;line-height:1.7;max-width:100%;}.fcopy{font-size:.7rem;line-height:1.5;}}@media(max-width:480px){.fg{padding:2rem 1.2rem;gap:1.6rem;}.ficons{gap:.6rem;}.ficon{width:2.4rem;height:2.4rem;}.fct{font-size:.85rem;}.fl{font-size:.78rem;}.f-desc{font-size:.78rem;line-height:1.65;}.fcopy{font-size:.68rem;}}@media(max-width:360px){.fg{padding:1.8rem 1rem;}.ficons{gap:.5rem;}.ficon{width:2.2rem;height:2.2rem;}.fl{font-size:.75rem;}.f-desc{font-size:.75rem;}.fcopy{font-size:.65rem;}}\
    @media(max-width:768px){#fb-date{width:100%!important;height:48px!important;padding:.6rem .8rem!important;font-size:.9rem!important;line-height:1.2;border:1px solid #ddd;border-radius:8px;box-sizing:border-box;background:#fff;display:block;min-width:0;}}\
  ';
  document.head.appendChild(style);

  // Footer + Button HTML
  var html = '\
  <footer data-green>\
    <div class="fg">\
      <div>\
        <div style="margin-bottom:1rem;"><img src="images/logo-white-full.svg" style="height:5.5rem;width:auto;opacity:0.85;"></div>\
        <p class="f-desc">Super Speciality Care by India’s Finest Specialists</br> Right Here in Mangalore</p>\
        <div class="ficons">\
          <a href="https://www.instagram.com/rvrhealthcare/" target="_blank" rel="noopener" class="ficon" data-h aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>\
          <a href="https://www.facebook.com/people/RVR-Super-Speciality-Centre/61572227856553/" target="_blank" rel="noopener" class="ficon" data-h aria-label="Facebook"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>\
          <a href="https://youtube.com/@rvrhealthcare" target="_blank" rel="noopener" class="ficon" data-h aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31.4 31.4 0 0 0 0 12a31.4 31.4 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31.4 31.4 0 0 0 24 12a31.4 31.4 0 0 0-.5-5.8zM9.6 15.5v-7L15.8 12l-6.2 3.5z"/></svg></a>\
          <a href="https://www.linkedin.com/company/rvrhealthcare" target="_blank" rel="noopener" class="ficon" data-h aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></a>\
          </br><a href="https://wa.me/918050454112" class="ficon" data-h aria-label="WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 00-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>\
          <a href="tel:08242005000" class="ficon" data-h aria-label="Call"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 10.8 19.79 19.79 0 01.07 2.18 2 2 0 012.06 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></a>\
          <a href="mailto:info@rvrhealthcare.in" class="ficon" data-h aria-label="Email"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></a>\
        </div>\
      </div>\
      <div>\
        <div class="fct">Quick Links</div>\
        <div class="flinks">\
          <a href="index.html" class="fl" data-h>Home</a>\
          <a href="about.html" class="fl" data-h>About Us</a>\
          <a href="our-care.html" class="fl" data-h>Our Care</a>\
          <a href="specialists.html" class="fl" data-h>Our Specialists</a>\
          <a href="spaces.html" class="fl" data-h>Spaces</a>\
          <a href="welldesk.html" class="fl" data-h>Welldesk</a>\
          <a href="reach-us.html" class="fl" data-h>Reach Us</a>\
        </div>\
      </div>\
      <div>\
        <div class="fct">Our Care</div>\
        <div class="flinks">\
          <a href="neurology.html" class="fl" data-h>Neurology & Nuerosergery</a>\
          <a href="interventional-neuroradiology.html" class="fl" data-h>Interventional Nuroradiology</a>\
          <a href="cardiology.html" class="fl" data-h>Cardiology</a>\
          <a href="oncology.html" class="fl" data-h>Oncology</a>\
          <a href="rheumatology.html" class="fl" data-h>Rheumatology & Immunology</a>\
          <a href="urology.html" class="fl" data-h>Urology and Andrology</a>\
          <a href="nephrology.html" class="fl" data-h>Nephrology</a>\
          <a href="ent.html" class="fl" data-h>Neuroequilibrium & Vertigo</a>\
          <a href="physiotherapy.html" class="fl" data-h>Physiotherapy & Rehabilitation</a>\
        </div>\
      </div>\
      <div>\
        <div class="fct">Contact</div>\
        <div class="flinks">\
          <a href="tel:08242005000" class="fl" data-h>0824 2005000</a>\
          <a href="tel:08242006000" class="fl" data-h>0824 2006000</a>\
          <a href="tel:+918050454119" class="fl" data-h>+91 80504 54119</a>\
          <a href="https://wa.me/918050454112" class="fl" data-h>+91 80504 54112</a>\
          <a href="mailto:info@rvrhealthcare.in" class="fl" data-h>info@rvrhealthcare.in</a>\
          <a href="mailto:dr@rvrhealthcare.in" class="fl" data-h>dr@rvrhealthcare.in</a>\
        </div>\
        <div style="margin-top:1.4rem;font-size:0.66rem;color:rgba(255,255,255,0.25);line-height:1.75;">RVR Super Speciality Centre<br>2nd Floor, Landmark Ayush<br>Opposite Highland Hospital<br>Falnir, Mangaluru 575002</div>\
      </div>\
    </div>\
    <div class="fbot">\
      <span class="fcopy">2026 RVR Super Speciality Centre Private Limited. All rights reserved.</span>\
      <span class="fcopy">rvrhealthcare.in</span>\
    </div>\
  </footer>\
  <div class="fb-wrap" id="fb-wrap">\
    <button class="fb-btn" id="fb-btn" aria-label="Book Appointment">\
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>\
      <span>Book Now</span>\
    </button>\
    <div class="fb-overlay" id="fb-overlay">\
      <div class="fb-form">\
        <div class="fb-form-head">\
          <h3>Book an Appointment</h3>\
          <button class="fb-close" id="fb-close">&times;</button>\
        </div>\
        <form id="fb-form-inner">\
          <div class="fb-field"><label for="fb-name">Your Name</label><input type="text" id="fb-name" placeholder="Enter your name" required></div>\
          <div class="fb-field"><label for="fb-phone">Phone Number</label><input type="tel" id="fb-phone" placeholder="Enter your phone" required></div>\
          <div class="fb-field"><label for="fb-dept">Department</label><select id="fb-dept" required><option value="">Select Department</option><option value="Neurology & Neurosurgery">Neurology & Neurosurgery</option><option value="Interventional Radiology & Neuro Radiology">Interventional Radiology & Neuro Radiology</option><option value="Cardiology">Cardiology</option><option value="Oncology">Oncology</option><option value="Rheumatology & Immunology">Rheumatology & Immunology</option><option value="Nephrology">Nephrology</option><option value="Urology & Andrology">Urology & Andrology</option><option value="Neuroequilibrium & Vertigo">Neuroequilibrium & Vertigo</option><option value="Physiotherapy & Rehabilitation">Physiotherapy & Rehabilitation</option></select></div>\
          <div class="fb-field"><label for="fb-doctor">Preferred Doctor</label><select id="fb-doctor" required><option value="">Select Doctor</option></select></div>\
          <div class="fb-field"><label for="fb-date">Preferred Date</label><input type="date" id="fb-date" required></div>\
          <div class="fb-field"><label for="fb-msg">Message</label><textarea id="fb-msg" rows="3" placeholder="Brief description of your concern"></textarea></div>\
          <button type="submit" class="fb-submit">Submit</button>\
        </form>\
      </div>\
    </div>\
  </div>\
  ';

  var fp = document.getElementById('footer-placeholder');
  if (fp) { fp.insertAdjacentHTML('afterend', html); fp.remove(); }
  else { document.body.insertAdjacentHTML('beforeend', html); }

  // Form logic
  var wrap = document.getElementById('fb-wrap');
  var btn = document.getElementById('fb-btn');
  var overlay = document.getElementById('fb-overlay');
  var closeBtn = document.getElementById('fb-close');
  var formInner = document.getElementById('fb-form-inner');

  if (!btn || !wrap) return;

  btn.addEventListener('click', function() { wrap.classList.toggle('open'); });

  if (closeBtn) {
    closeBtn.addEventListener('click', function() { wrap.classList.remove('open'); });
  }
  if (overlay) {
    overlay.addEventListener('click', function(e) { if (e.target === overlay) wrap.classList.remove('open'); });
  }
  if (formInner) {
    formInner.addEventListener('submit', function(e) {
      e.preventDefault();
      var name = document.getElementById('fb-name').value.trim();
      var phone = document.getElementById('fb-phone').value.trim();
      var dept = document.getElementById('fb-dept').value;
      var doctor = document.getElementById('fb-doctor').value.trim();
      var date = document.getElementById('fb-date').value;
      var msg = document.getElementById('fb-msg').value.trim();
      var text = 'Hello RVR Super Speciality Centre, I would like to book an appointment.';
      if (name) text += '\nName: ' + name;
      if (phone) text += '\nPhone: ' + phone;
      if (dept) text += '\nDepartment: ' + dept;
      if (doctor) text += '\nPreferred Doctor: ' + doctor;
      if (date) { var d = new Date(date); text += '\nPreferred Date: ' + d.getDate() + '/' + (d.getMonth()+1) + '/' + d.getFullYear(); }
      if (msg) text += '\nMessage: ' + msg;
      window.open('https://wa.me/918050454112?text=' + encodeURIComponent(text), '_blank');
      wrap.classList.remove('open');
      formInner.reset();
    });
  }
});

const deptDoctors = {
  "Neurology & Neurosurgery": [
    "Dr. Sunil Shetty K R",
    "Dr. (Prof.) Raghavendra B S",
    "Dr. Vignesh Sampath Iyer",
    "Dr. Abu T",
    "Dr. Shishir Duble"
  ],

  "Interventional Radiology & Neuro Radiology": [
    "Dr. Keerthiraj B",
    "Dr. Ariharan Krishnaraj"
  ],

  "Cardiology": [
    "Dr. Maneesh Rai"
  ],

  "Oncology": [
    "Dr. (Prof.) Nishitha Shetty"
  ],

  "Rheumatology & Immunology": [
    "Dr. Sahana G Baliga"
  ],

  "Nephrology": [
    "Dr. Amith V. L Dsouza"
  ],

  "Urology & Andrology": [
    "Dr. Nandakishore B"
  ],

  "Neuroequilibrium & Vertigo": [
    "Dr. Anjan Kumar A N"
  ],

  "Physiotherapy & Rehabilitation": [
    "Dr. Mohammad Rameez Panangai"
  ]
};

document.addEventListener('DOMContentLoaded', function () {

  const deptSelect = document.getElementById('fb-dept');
  const doctorSelect = document.getElementById('fb-doctor');

  if (!deptSelect || !doctorSelect) return;

  deptSelect.addEventListener('change', function () {

    const selectedDept = this.value;

    doctorSelect.innerHTML =
      '<option value="">Select Doctor</option>';

    if (deptDoctors[selectedDept]) {

      deptDoctors[selectedDept].forEach(function (doctor) {

        const option = document.createElement('option');

        option.value = doctor;
        option.textContent = doctor;

        doctorSelect.appendChild(option);

      });

    }

  });

});
