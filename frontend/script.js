async function analyzeTasks() {
    const input = document.getElementById('taskInput').value;
    let tasks;

    try {
        tasks = JSON.parse(input);
    } catch {
        alert("Invalid JSON format");
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(tasks)
    });

    const data = await response.json();
    displayResults(data);
}

function displayResults(data) {
    const output = document.getElementById('output');
    output.innerHTML = ""; // clear previous results

    data.forEach(task => {
        const div = document.createElement("div");
        div.classList.add("result-item");

        if (task.score >= 70) div.classList.add("high");
        else if (task.score >= 50) div.classList.add("medium");
        else div.classList.add("low");

        div.innerHTML = `<strong>${task.title}</strong> - Score: ${task.score}`;

        output.appendChild(div);
    });
}
