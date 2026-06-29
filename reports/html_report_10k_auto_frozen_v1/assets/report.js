const MAX_SELECT_OPTIONS = 250;

function tableRows(table) {
  return Array.from((table.tBodies[0] && table.tBodies[0].rows) || []);
}

function compactText(node) {
  return (node && node.innerText ? node.innerText : '').trim().split(/\s+/).join(' ');
}

function isColumnFilterableHeader(label) {
  const normalized = (label || '').trim().toLowerCase();
  return normalized !== 'sources' && normalized !== 'examples';
}

function parseFilterTerms(value) {
  return (value || '')
    .toLowerCase()
    .split(/[|,]/)
    .map(term => term.trim())
    .filter(Boolean);
}

function textMatchesTerms(text, terms) {
  if (!terms.length) return true;
  const lower = (text || '').toLowerCase();
  return terms.some(term => lower.includes(term));
}

function tableForColumnControl(control) {
  const bar = control.closest('.column-filter-bar');
  const wrap = bar && bar.nextElementSibling;
  return wrap ? wrap.querySelector('table') : null;
}

function applyTableFilters(table) {
  if (!table) return;
  const scope = table.closest('section') || table.parentElement;
  const globalInput = scope ? scope.querySelector('[data-filter-next-table]') : null;
  const globalTerms = parseFilterTerms(globalInput ? globalInput.value : '');
  const filters = table._columnFilters || [];

  for (const row of tableRows(table)) {
    let visible = true;
    const rowText = row.textContent;
    if (!textMatchesTerms(rowText, globalTerms)) visible = false;

    if (visible) {
      for (const filter of filters) {
        const cell = compactText(row.cells[filter.index]);
        const containsTerms = parseFilterTerms(filter.input.value);
        if (!textMatchesTerms(cell, containsTerms)) {
          visible = false;
          break;
        }
        if (filter.select) {
          const selected = Array.from(filter.select.selectedOptions).map(option => option.value);
          if (selected.length && !selected.includes(cell)) {
            visible = false;
            break;
          }
        }
      }
    }

    row.style.display = visible ? '' : 'none';
  }
}

function buildColumnFiltersForTable(table) {
  if (!table || table.dataset.columnFiltersInstalled === '1') return;
  const wrap = table.closest('.table-wrap');
  if (!wrap || !wrap.parentElement) return;
  const headers = Array.from(table.tHead ? table.tHead.rows[0].cells : []);
  if (!headers.length) return;

  const bar = document.createElement('div');
  bar.className = 'column-filter-bar';
  const filters = [];
  const rows = tableRows(table);

  for (const [index, th] of headers.entries()) {
    const headerLabel = compactText(th) || 'column';
    if (!isColumnFilterableHeader(headerLabel)) continue;

    const details = document.createElement('details');
    details.className = 'column-filter';

    const summary = document.createElement('summary');
    summary.textContent = headerLabel;
    details.appendChild(summary);

    const input = document.createElement('input');
    input.type = 'search';
    input.className = 'column-filter-input';
    input.placeholder = 'contains: a|b or a, b';
    input.autocomplete = 'off';
    details.appendChild(input);

    const counts = new Map();
    for (const row of rows) {
      const value = compactText(row.cells[index]);
      if (!value) continue;
      counts.set(value, (counts.get(value) || 0) + 1);
    }
    const values = Array.from(counts.entries()).sort((a, b) => {
      if (b[1] !== a[1]) return b[1] - a[1];
      return a[0].localeCompare(b[0], undefined, {numeric: true, sensitivity: 'base'});
    });

    let select = null;
    if (values.length && values.length <= MAX_SELECT_OPTIONS) {
      select = document.createElement('select');
      select.className = 'column-filter-select';
      select.multiple = true;
      select.size = Math.min(8, Math.max(3, values.length));
      select.title = 'Ctrl/Cmd click으로 여러 값을 선택';
      for (const [value, count] of values) {
        const option = document.createElement('option');
        option.value = value;
        option.textContent = value.length > 80 ? value.slice(0, 77) + '... (' + count + ')' : value + ' (' + count + ')';
        select.appendChild(option);
      }
      details.appendChild(select);
    } else {
      const note = document.createElement('div');
      note.className = 'filter-note';
      note.textContent = values.length + ' unique values. Use contains filter. OR: a|b or a, b';
      details.appendChild(note);
    }

    filters.push({index, input, select});
    bar.appendChild(details);
  }

  const actions = document.createElement('div');
  actions.className = 'filter-actions';
  const reset = document.createElement('button');
  reset.type = 'button';
  reset.className = 'column-filter-reset';
  reset.textContent = 'Reset filters';
  actions.appendChild(reset);
  bar.appendChild(actions);

  table._columnFilters = filters;
  table.dataset.columnFiltersInstalled = '1';
  wrap.parentElement.insertBefore(bar, wrap);
}

function installColumnFilterButtons() {
  for (const table of document.querySelectorAll('table.sortable')) {
    const wrap = table.closest('.table-wrap');
    if (!wrap || !wrap.parentElement || table.dataset.columnFilterButtonInstalled === '1') continue;
    const toolbar = document.createElement('div');
    toolbar.className = 'column-filter-toolbar';
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'column-filter-build';
    button.textContent = 'Show column filters';
    const note = document.createElement('span');
    note.textContent = 'Builds filters only when needed.';
    toolbar.appendChild(button);
    toolbar.appendChild(note);
    wrap.parentElement.insertBefore(toolbar, wrap);
    table.dataset.columnFilterButtonInstalled = '1';
  }
}

document.addEventListener('DOMContentLoaded', installColumnFilterButtons);

document.addEventListener('input', (event) => {
  const input = event.target;
  if (input.matches('[data-filter-next-table]')) {
    applyTableFilters(input.parentElement.querySelector('table'));
    return;
  }
  if (input.matches('.column-filter-input')) {
    applyTableFilters(tableForColumnControl(input));
  }
});

document.addEventListener('change', (event) => {
  const select = event.target;
  if (select.matches('.column-filter-select')) {
    applyTableFilters(tableForColumnControl(select));
  }
});

document.addEventListener('click', (event) => {
  const build = event.target.closest('.column-filter-build');
  if (build) {
    const toolbar = build.closest('.column-filter-toolbar');
    const wrap = toolbar && toolbar.nextElementSibling;
    const table = wrap ? wrap.querySelector('table') : null;
    if (table) {
      build.disabled = true;
      build.textContent = 'Building filters...';
      setTimeout(() => {
        buildColumnFiltersForTable(table);
        toolbar.remove();
      }, 0);
    }
    return;
  }

  const reset = event.target.closest('.column-filter-reset');
  if (reset) {
    const table = tableForColumnControl(reset);
    if (table) {
      for (const filter of table._columnFilters || []) {
        filter.input.value = '';
        if (filter.select) {
          for (const option of filter.select.options) option.selected = false;
        }
      }
      const scope = table.closest('section') || table.parentElement;
      const globalInput = scope ? scope.querySelector('[data-filter-next-table]') : null;
      if (globalInput) globalInput.value = '';
      applyTableFilters(table);
    }
    return;
  }

  const th = event.target.closest('th');
  if (!th || !th.closest('table.sortable')) return;
  const table = th.closest('table');
  const idx = Array.from(th.parentElement.children).indexOf(th);
  const rows = tableRows(table);
  const nextDir = th.dataset.sortDir === 'asc' ? 'desc' : 'asc';
  for (const other of th.parentElement.children) {
    other.classList.remove('sort-asc', 'sort-desc');
    other.removeAttribute('data-sort-dir');
    other.removeAttribute('aria-sort');
  }
  th.dataset.sortDir = nextDir;
  th.classList.add(nextDir === 'asc' ? 'sort-asc' : 'sort-desc');
  th.setAttribute('aria-sort', nextDir === 'asc' ? 'ascending' : 'descending');
  const dir = nextDir === 'asc' ? 1 : -1;
  rows.sort((a, b) => {
    const av = compactText(a.cells[idx]);
    const bv = compactText(b.cells[idx]);
    const an = Number(av.replaceAll(',', '').replace(/%$/, ''));
    const bn = Number(bv.replaceAll(',', '').replace(/%$/, ''));
    if (!Number.isNaN(an) && !Number.isNaN(bn)) return (an - bn) * dir;
    return av.localeCompare(bv, undefined, {numeric: true, sensitivity: 'base'}) * dir;
  });
  rows.forEach(row => table.tBodies[0].appendChild(row));
});
