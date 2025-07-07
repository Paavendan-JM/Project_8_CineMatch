async function getRecommendations() {
  const title = document.getElementById('movieInput').value;
  const response = await fetch('/recommend', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title })
  });
  const data = await response.json();

  const resultList = document.getElementById('resultList');
  resultList.innerHTML = '';

  if (data.length === 0) {
    resultList.innerHTML = '<p>No results found.</p>';
    return;
  }

  const table = document.createElement('table');
  table.innerHTML = `
    <tr>
      <th>Title</th>
      <th>Genre</th>
      <th>Description</th>
      <th>Actors</th>
      <th>Director</th>
    </tr>
  `;

  data.forEach(movie => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${movie.title || '-'}</td>
      <td>${movie.genre || '-'}</td>
      <td>${movie.description || '-'}</td>
      <td>${movie.actors || '-'}</td>
      <td>${movie.director || '-'}</td>
    `;
    table.appendChild(row);
  });

  resultList.appendChild(table);
}
