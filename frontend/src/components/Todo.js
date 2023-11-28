import React from 'react'

function TodoItem(props) {

    return (
        <div>
            <p>
                {props.todo.id} <span style={{ fontWeight: 'bold, underline' }}>{props.todo.title} : </span> {props.todo.description}
                <button onClick={() => props.deleteTodo(props.todo.id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default TodoItem;