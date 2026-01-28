// Load tasks when page opens
window.onload = loadTasks;

async function loadTasks() {
    const response = await fetch('/api/tasks');
    const tasks = await response.json();
    const list = document.getElementById('taskList');
    list.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.title;
        list.appendChild(li);
    });
}

async function addTask() {
    const input = document.getElementById('taskInput');
    const title = input.value.trim();
    if (!title) return;
    
    await fetch('/api/tasks', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({title})
    });
    
    input.value = '';
    loadTasks(); // Refresh list without page reload
}
