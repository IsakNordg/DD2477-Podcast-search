// search.js

document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('searchInput');
  const selectInput = document.getElementById('selector');

  function setLoading(state) {
    if (state === true) {
      document.getElementById('spinnerContainer').style.display = 'flex'; // To show the spinner
      document.getElementById('pageContainer').style.display = 'none'; // To hide the page
    } else {
      document.getElementById('spinnerContainer').style.display = 'none'; // To hide the spinner
      document.getElementById('pageContainer').style.display = 'block'; // To show the page
    }
  }

  function handleInput(event) {
    if (event.key === 'Enter' || event.target.classList.contains('searchButton')) {
      setLoading(true);
      const methodID = selectInput.value;
      const searchQuery = searchInput.value;
      const input = 'http://127.0.0.1:5000/search?query=' + searchQuery + '&method=' + methodID;
      fetch(input, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: searchQuery,
          method: methodID
        })
      })
      .then(response => {
        setLoading(false);
        if (response.redirected) {
          window.location.href = response.url; // Follow the redirect
        }
      })
      .catch(error => {
        setLoading(false);
        console.error("Failed to fetch data: ", error);
      });
    }
  }

  setLoading(false);
  window.onload = searchInput.select();
  searchInput.addEventListener('keydown', handleInput);
  document.querySelector('.searchButton').addEventListener('click', handleInput);
});