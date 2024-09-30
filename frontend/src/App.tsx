import React, { useState } from 'react';
import './App.css';
import CommandHistory from './components/CommandHistory';

function App() {
  const [command, setCommand] = useState('');
  const [response, setResponse] = useState('');
  const [history, setHistory] = useState<{ command: string, response: string }[]>([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch('http://localhost:5000/command', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ command }),
    });
    const data = await res.json();
    setResponse(data.response);
    setHistory([...history, { command, response: data.response }]);
  };

  // Voice command feature using Web Speech API
  const startListening = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.onresult = function (event: any) {
      setCommand(event.results[0][0].transcript);
    };
    recognition.start();
  };

  return (
    <div className="App">
      <h1>Smart Personal Assistant</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={command}
          onChange={(e) => setCommand(e.target.value)}
          placeholder="Enter your command"
        />
        <button type="submit">Submit</button>
      </form>
      <button onClick={startListening}>Voice Input</button>
      <h2>Response: {response}</h2>
      <CommandHistory history={history} />
    </div>
  );
}

export default App;
