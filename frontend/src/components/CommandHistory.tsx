import React from 'react';

interface CommandHistoryProps {
  history: { command: string, response: string }[];
}

const CommandHistory: React.FC<CommandHistoryProps> = ({ history }) => {
  return (
    <div>
      <h3>Command History</h3>
      <ul>
        {history.map((item, index) => (
          <li key={index}>{item.command} - {item.response}</li>
        ))}
      </ul>
    </div>
  );
};

export default CommandHistory;
