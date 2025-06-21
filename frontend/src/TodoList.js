import React from "react";

function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((t) => (
        <li key={t.id}>{t.task}</li>
      ))}
    </ul>
  );
}

export default TodoList;

