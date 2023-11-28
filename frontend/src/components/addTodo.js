import React, { useState } from 'react';

export const AddTodo = ({ addTodo, updateTodo }) => {
    const [id, setId] = useState("")
    const [title, setTitle] = useState("");
    const [desc, setDesc] = useState("");


    const submit = (e) => {
        e.preventDefault();
        if (!id || !title || !desc) {
            alert("TodoId or Title or Description cannot be blank");
        }
        else {
        if (e.nativeEvent.submitter.name === 'submit-btn') {
        addTodo(id, title, desc);
            setId("")
            setTitle("");
            setDesc("");
        }
    if (e.nativeEvent.submitter.name === 'update-btn') {
        updateTodo(id, title, desc);
            setId("")
            setTitle("");
            setDesc("");
        }
        }

    }
    return (
        <div className="container my-3">
            <h3>Add a Todo</h3>
            <form onSubmit={submit}>
                <div className="mb-3">
                    <label htmlFor="todoId" className="form-label">Todo Id</label>
                    <input type="text" value={id} onChange={(e) => setId(e.target.value)} className="form-control" id="todoId"/>

                </div>
                <div className="mb-3">
                    <label htmlFor="title" className="form-label">Todo Title</label>
                    <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} className="form-control" id="title" aria-describedby="emailHelp" />

                </div>
                <div className="mb-3">
                    <label htmlFor="desc" className="form-label">Todo Description</label>
                    <input type="text" value={desc} onChange={(e) => setDesc(e.target.value)} className="form-control" id="desc" />
                </div>
                <button type="submit" className="btn btn-sm btn-success" name='submit-btn'>Add Todo</button>
                <button  type= "submit" className="btn btn-outline-primary mx-2 mb-3" name='update-btn' style={{'borderRadius':'50px',"font-weight":"bold"}} >Update Todo</button>

            </form>

        </div>
    )
}
