import React, { useState, useEffect } from "react";
import axios from "axios";
import TodoForm from "./TodoForm";
import TodoList from "./TodoList";

const BACKEND_URL = "/todos"; // Will change later in Docker/K8s

function App() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    axios.get(BACKEND_URL).then((res) => setTodos(res.data));
  }, []);

  const addTodo = (task) => {
    axios.post(BACKEND_URL, { task }).then((res) => {
      setTodos([...todos, res.data]);
    });
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>DevOpsify – To-Do App</h2>
      <TodoForm addTodo={addTodo} />
      <TodoList todos={todos} />
    </div>
  );
}

export default App;

