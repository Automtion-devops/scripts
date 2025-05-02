function displayResult(data) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ""; // Limpia los resultados anteriores

    if (data.status === "success") {
        const resultContent = document.createElement('pre');
        resultContent.textContent = data.result;
        resultsDiv.appendChild(resultContent);
    } else {
        const errorMessage = document.createElement('p');
        errorMessage.style.color = "red";
        errorMessage.textContent = `Error: ${data.message}`;
        resultsDiv.appendChild(errorMessage);
    }
}

async function fetchStatus() {
    const response = await fetch('/status');
    const data = await response.json();
    displayResult(data);
}

async function cleanBasic() {
    const response = await fetch('/clean/basic', { method: 'POST' });
    const data = await response.json();
    displayResult(data);
}

async function cleanAdvanced() {
    const response = await fetch('/clean/advanced', { method: 'POST' });
    const data = await response.json();
    displayResult(data);
}

async function cleanVolumes() {
    const response = await fetch('/clean/volumes', { method: 'POST' });
    const data = await response.json();
    displayResult(data);
}

async function showDisk() {
    const response = await fetch('/disk');
    const data = await response.json();
    displayResult(data);
}