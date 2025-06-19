// Load candidate data from the global variables in vote.html
function getCandidateById(list, id) {
  return list.find(c => c.id == id);
}

function renderCard(container, candidate) {
  if (!candidate) return;
  const cardHTML = `
    <div class="preview-card-landscape">
      <img src="static/${candidate.image_url}" alt="${candidate.name}">
      <div class="info">
        <h4>${candidate.name}</h4>
        <p>${candidate.bio}</p>
      </div>
    </div>`;
  container.innerHTML += cardHTML;
}

function updatePreviewCards() {
  const boySelects = document.querySelectorAll('.boy-select');
  const girlSelects = document.querySelectorAll('.girl-select');

  const leftContainer = document.getElementById('left-cards');
  const rightContainer = document.getElementById('right-cards');
  leftContainer.innerHTML = '';
  rightContainer.innerHTML = '';

  boySelects.forEach(sel => {
    const candidate = getCandidateById(window.boysData, sel.value);
    if (candidate) renderCard(leftContainer, candidate);
  });

  girlSelects.forEach(sel => {
    const candidate = getCandidateById(window.girlsData, sel.value);
    if (candidate) renderCard(rightContainer, candidate);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.form-select').forEach(select => {
    select.addEventListener('change', updatePreviewCards);
  });
  updatePreviewCards(); // Initial render
});
