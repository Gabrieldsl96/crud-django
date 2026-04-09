document.addEventListener('DOMContentLoaded', () => {
  // Live search
  const input = document.getElementById('search-input');
  const noResults = document.getElementById('no-results');

  if (input) {
    input.addEventListener('input', () => {
      const term = input.value.toLowerCase().trim();
      let visible = 0;

      document.querySelectorAll('tbody tr').forEach(row => {
        const match = row.textContent.toLowerCase().includes(term);
        row.style.display = match ? '' : 'none';
        if (match) visible++;
      });

      if (noResults) {
        noResults.classList.toggle('hidden', visible > 0 || term === '');
      }
    });
  }

  // Stock level badge coloring
  document.querySelectorAll('.stock-badge').forEach(badge => {
    const val = parseInt(badge.textContent.trim(), 10);
    if (isNaN(val)) return;
    if (val === 0) badge.classList.add('stock-out');
    else if (val <= 5) badge.classList.add('stock-low');
    else badge.classList.add('stock-ok');
  });
});
