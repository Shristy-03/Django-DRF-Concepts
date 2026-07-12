const API = "http://127.0.0.1:8000/api/tasks/";

const form = document.getElementById("taskForm");
const tasksDiv = document.getElementById("tasks");

let editTaskId = null;

// Load all tasks when page opens
window.onload = loadTasks;

// ======================
// GET ALL TASKS
// ======================

async function loadTasks() {

    const response = await fetch(API);
    const tasks = await response.json();

    tasksDiv.innerHTML = "";

    tasks.forEach(task => {

        tasksDiv.innerHTML += `

        <div class="task-card">

            <h3>${task.title}</h3>

            <p><b>Description:</b> ${task.description}</p>

            <p><b>Due Date:</b> ${task.due_date}</p>

            <p><b>Status:</b> ${task.status}</p>

            <button onclick="editTask(${task.id})">
                Edit
            </button>

            <button onclick="deleteTask(${task.id})">
                Delete
            </button>

            <hr>

        </div>

        `;

    });

}



// ======================
// ADD OR UPDATE TASK
// ======================

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const task = {

        title: document.getElementById("title").value,

        description: document.getElementById("description").value,

        due_date: document.getElementById("due_date").value,

        status: document.getElementById("status").value

    };


    if(editTaskId == null){

        // POST

        await fetch(API,{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(task)

        });

    }

    else{

        // PUT

        await fetch(API + editTaskId + "/",{

            method:"PUT",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify(task)

        });

        editTaskId = null;

        document.querySelector("button[type='submit']").innerText = "Add Task";

    }

    form.reset();

    loadTasks();

});



// ======================
// DELETE
// ======================

async function deleteTask(id){

    if(confirm("Delete this task?")){

        await fetch(API + id + "/",{

            method:"DELETE"

        });

        loadTasks();

    }

}



// ======================
// EDIT
// ======================

async function editTask(id){

    const response = await fetch(API + id + "/");

    const task = await response.json();

    document.getElementById("title").value = task.title;

    document.getElementById("description").value = task.description;

    document.getElementById("due_date").value = task.due_date;

    document.getElementById("status").value = task.status;

    editTaskId = id;

    document.querySelector("button[type='submit']").innerText = "Update Task";

}