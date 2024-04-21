// results.js

document.addEventListener('DOMContentLoaded', function () {
  const homeIcon = document.getElementById('home-icon');
  const totalCnt = document.getElementById('total-counts');
  const pageInfo = document.getElementById('page-info');
  const resultsContainer = document.getElementById('result-details');
  const backIcon = document.getElementById('back-icon');
  const nextIcon = document.getElementById('next-icon');

  // Initialize search results data
  const searchResults = JSON.parse(resultsContainer.textContent)
  const itemsPerPage = 10;
  const totalResults = searchResults.length;
  let currentItems;
  let currentPage = 1;
  let totalPages = Math.ceil(totalResults / itemsPerPage);

  function navToSearchPage() {
    window.location.href = '/search';
  }

  function handlePrevious() {
    if (currentPage > 1)
      currentPage--;
    renderResults();
    window.scrollTo(0, 0);
  }

  function handleNext() {
    if (currentPage < totalPages)
      currentPage++;
    renderResults();
    window.scrollTo(0, 0);
  }

  function renderResults() {
    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    currentItems = searchResults.slice(start, end);

    // Insert innerHTML of resultItems
    resultsContainer.innerHTML = '';
    currentItems.forEach(item => {
      const div = document.createElement('div');
      div.className = 'result-item';
      div.innerHTML = `
        <h3>${item.title}</h3>
        <p><b>ID:</b> ${item.id} &emsp;&emsp; <b>Rank:</b> ${item.id}</p>
        <p><b>Content:</b> ${item.content}</p>
      `;
      resultsContainer.appendChild(div);
    });

    pageInfo.innerHTML = `<i>Showing Page</i> ${currentPage} of ${totalPages}`;
    totalCnt.innerHTML = `<b>Top ${totalResults} search ${totalResults === 1?'result':'results'}</b>`;
  }

  renderResults();
  homeIcon.addEventListener('click', navToSearchPage);
  backIcon.addEventListener('click', handlePrevious);
  nextIcon.addEventListener('click', handleNext);
  console.log(searchResults)
});