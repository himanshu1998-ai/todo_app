import React, { useState, useEffect} from 'react';
import './App.css';
import TodoView from './components/TodoListView';
import { AddTodo } from './components/addTodo';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {

  const [todoList, setTodoList] = useState([{}])
  const [refreshKey, setRefreshKey] = useState(0);

  // Read all todos
  useEffect(() => {
  axios.get('http://localhost:5007/fetch_all_todo')
      .then(res => {
        setTodoList(res.data)
      })
  }, [refreshKey]);

  // Post a todo
  const addTodoHandler = (id,title,desc) => {
     axios.post('http://localhost:5007/create_todo', { 'id':  id, 'title': title, 'description': desc })
      .then(res => setRefreshKey(oldKey => oldKey +1))
};
// PUT a todo
const updateTodoHandler = (id,title,desc) => {
     axios.put("http://localhost:5007/update_todo", {"id": id,  "title": title, "description": desc})
        .then(res => setRefreshKey(oldKey => oldKey +1)) }

// DELETE a todo
const deleteTodoHandler = (id) => {
     axios.delete(`http://localhost:5007/delete_todo/${id}`)
        .then(setRefreshKey(oldKey => oldKey +1)) }
  return (
    <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"400px", "backgroundColor":"white", "marginTop":"15px"}} >
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Task Manager</h1>
      <h6 className="card text-white bg-primary mb-3">FASTAPI - React - MongoDB</h6>
     <div className="card-body">
      <h5 className="card text-white bg-dark mb-3">Add Your Task</h5>
        <AddTodo addTodo={addTodoHandler} updateTodo={updateTodoHandler} />
      <h5 className="card text-white bg-dark mb-3">Your Tasks</h5>
      <div >
      <TodoView todoList={todoList} deleteTodo={deleteTodoHandler} />
      </div>
      </div>
      <h6 className="card text-dark bg-warning py-1 mb-0" >Copyright 2021, All rights reserved &copy;</h6>
    </div>
  );
}

export default App;