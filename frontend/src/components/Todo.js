import axios from 'axios'
import React from 'react'

function TodoItem(props) {
    const deleteTodoHandler = (id) => {
     axios.delete(`http://localhost:5007/delete_todo/${id}`)
        .then(res => console.log(res.data)) }

    return (
        <div>
            <p>
                {props.todo.id} <span style={{ fontWeight: 'bold, underline' }}>{props.todo.title} : </span> {props.todo.description}
                <button onClick={() => deleteTodoHandler(props.todo.id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default TodoItem;