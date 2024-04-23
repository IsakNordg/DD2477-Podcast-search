// results.js

document.addEventListener('DOMContentLoaded', function () {
  const homeIcon = document.getElementById('home-icon');
  const totalCnt = document.getElementById('total-counts');
  const pageInfo = document.getElementById('page-info');
  const resultsContainer = document.getElementById('result-details');
  const backIcon = document.getElementById('back-icon');
  const nextIcon = document.getElementById('next-icon');

  // Initialize search results data
  const searchResults = JSON.parse(resultsContainer.textContent);
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

    // Insert resultItems into HTML
    resultsContainer.innerHTML = '';
    currentItems.forEach(item => {
      const title = `<h3>${item.title}</h3>`;
      const div = document.createElement('div');
      div.className = 'result-item';
      // Define result text components
      let idInfo = `<p><b>ID:</b> ${item.id}`;
      let content = `</p><p><b>Content:</b> ${item.content}</p>`;
      let timeInfo = ``;
      // Append result text components
      if ('rank' in item)
        idInfo += `&emsp;&emsp; <b>Rank:</b> ${item['rank']}`;
      if ('score' in item)
        idInfo += `&emsp;&emsp; <b>Score:</b> ${item['score']}`;
      if ('start@' in item && 'end@' in item) {
        timeInfo += `</p><p><b>Start at:</b> ${item[`start@`]} 
                &emsp;&emsp;<b>End Time:</b> ${item[`end@`]}`;
      }
      // Replace text of innerHTML with resultItems
      div.innerHTML = title.concat(idInfo, timeInfo, content);
      resultsContainer.appendChild(div);
    });

    pageInfo.innerHTML = `<i>Showing Page</i> ${currentPage} of ${totalPages}`;
    totalCnt.innerHTML = `<b>Top ${totalResults} search ${totalResults === 1?'result':'results'}</b>`;
  }

  renderResults();
  homeIcon.addEventListener('click', navToSearchPage);
  backIcon.addEventListener('click', handlePrevious);
  nextIcon.addEventListener('click', handleNext);
  console.log(searchResults);
});