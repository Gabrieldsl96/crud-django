document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('search-input');
  const noResults = document.getElementById('no-results');
  if (!input) return;

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
});
