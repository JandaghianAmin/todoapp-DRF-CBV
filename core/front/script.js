// Function to fetch and display the To-Do list
function fetchTodoList() {
    const apiUrl = 'http://127.0.0.1:8000/api/v1/tasks/'; // Replace with your API URL
    const todoList = document.getElementById('todo-list');

    // Make a GET request to the API
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            // Process the API response and update the webpage
            data.forEach(todo => {
                const li = document.createElement('li');
                li.textContent = `${todo.id}. ${todo.title}`;
                todoList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Call the function to fetch and display the To-Do list
fetchTodoList();
