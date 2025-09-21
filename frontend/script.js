const analyzeButton = document.getElementById('analyzeButton');
const urlInput = document.getElementById('urlInput');
const resultsDiv = document.getElementById('results');

analyzeButton.addEventListener('click', () => {
    const url = urlInput.value;
    if (!url) {
        alert("Please enter a URL to analyze!");
        return;
    }

    resultsDiv.innerHTML = "<p>Analyzing...</p>";
    resultsDiv.classList.remove('visible');

    fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ "url": url })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultsDiv.innerHTML = `<p style="color: red;"><strong>Error:</strong> ${data.error}</p>`;
        } else {
            resultsDiv.innerHTML = `
                <h3>${data.title}</h3>
                <p><strong>Article Preview:</strong></p>
                <p>${data.scraped_text_preview}</p>
                <hr>
                <h4>AI Analysis of Tone:</h4>
                <div class="ai-analysis">${data.ai_analysis}</div>
            `;
        }
        resultsDiv.classList.add('visible');
    })
    .catch(error => {
        resultsDiv.innerHTML = `<p style="color: red;"><strong>Connection Error:</strong> Could not reach the backend.</p>`;
        resultsDiv.classList.add('visible');
    });
});