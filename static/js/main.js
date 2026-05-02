/* main.js — EduFees Global JS */

// ── Live Clock ────────────────────────────────────────────
(function liveClock() {
  const el = document.getElementById('topbarDate');
  if (!el) return;
  function tick() {
    const d = new Date();
    el.textContent = d.toLocaleDateString('en-PK', {weekday:'short', day:'2-digit', month:'short', year:'numeric'})
      + '  ' + d.toLocaleTimeString('en-PK', {hour:'2-digit', minute:'2-digit'});
  }
  tick(); setInterval(tick, 1000);
})();

// ── Sidebar Toggle ─────────────────────────────────────────
document.getElementById('sidebarToggle')?.addEventListener('click', () => {
  document.getElementById('sidebar').classList.toggle('open');
});
document.addEventListener('click', e => {
  const sidebar = document.getElementById('sidebar');
  const toggle  = document.getElementById('sidebarToggle');
  if (sidebar && toggle && !sidebar.contains(e.target) && !toggle.contains(e.target)) {
    sidebar.classList.remove('open');
  }
});

// ── Custom Tab System ──────────────────────────────────────
document.querySelectorAll('.custom-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const group  = tab.dataset.tabGroup;
    const target = tab.dataset.tab;
    document.querySelectorAll(`.custom-tab[data-tab-group="${group}"]`)
      .forEach(t => t.classList.remove('active'));
    document.querySelectorAll(`.tab-pane-custom[data-tab-group="${group}"]`)
      .forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    document.querySelector(`.tab-pane-custom[data-tab="${target}"][data-tab-group="${group}"]`)
      ?.classList.add('active');
  });
});

// ── Toast Helper ───────────────────────────────────────────
function showToast(msg, type = 'success') {
  const el   = document.getElementById('globalToast');
  const body = document.getElementById('toastBody');
  if (!el || !body) return;
  el.className = 'toast align-items-center border-0 toast-' + type;
  const icon = type === 'success' ? '✅' : type === 'error' ? '❌' : 'ℹ️';
  body.innerHTML = `${icon} ${msg}`;
  bootstrap.Toast.getOrCreateInstance(el, {delay: 3500}).show();
}

// ── AJAX POST helper ──────────────────────────────────────
async function apiPost(url, data) {
  const res = await fetch(url, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data),
  });
  return res.json();
}

// ── Number formatter (Rs.) ────────────────────────────────
function fmtPKR(n) {
  return 'Rs. ' + Number(n).toLocaleString('en-PK', {minimumFractionDigits: 0});
}

// ── Status Badge HTML ─────────────────────────────────────
function statusBadge(val) {
  if (val === 'Approved' || val === 'Yes')
    return `<span class="badge-approved">✓ ${val}</span>`;
  if (val === 'Pending' || val === 'No')
    return `<span class="badge-pending">⏳ ${val}</span>`;
  return `<span class="id-badge">${val}</span>`;
}

// ── Build DataTable ───────────────────────────────────────
function buildTable(id, data, columns, opts = {}) {
  const tbl = $(`#${id}`);
  if ($.fn.DataTable.isDataTable(`#${id}`)) $(`#${id}`).DataTable().destroy();
  tbl.find('thead tr').empty();
  columns.forEach(c => tbl.find('thead tr').append(`<th>${c.title}</th>`));

  return tbl.DataTable({
    data,
    columns,
    pageLength: opts.pageLength || 10,
    order: opts.order || [[0, 'asc']],
    responsive: true,
    language: {
      search: '',
      searchPlaceholder: '🔍  Search…',
      emptyTable: '<div style="padding:30px;color:var(--text-muted)">No records found</div>',
      loadingRecords: '<div class="loading-spinner"></div>',
    },
    dom: "<'row mb-3'<'col-sm-6'l><'col-sm-6 d-flex justify-content-end'f>>" +
         "<'row'<'col-12'tr>>" +
         "<'row mt-3'<'col-sm-5'i><'col-sm-7 d-flex justify-content-end'p>>",
    ...opts,
  });
}

// ── Auto-fill fee on department/program change ────────────
window.autoFillFee = function(selectEl, feesMap, targetInputId) {
  const val = selectEl.value;
  const fee = feesMap[val] || 0;
  const inp = document.getElementById(targetInputId);
  if (inp && fee) inp.value = fee;
};