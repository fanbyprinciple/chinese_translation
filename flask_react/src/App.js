import React, {useState, useEffect} from 'react'
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0)
  const [currentMessage, setMessage] = useState("nil")
  // we are setting getter and setter here, 0 and nil are the default values

  //useeffect comes into play whenever the application nees to render itself
  useEffect(()=>{
    fetch('/time').then(res=> res.json()).then(data=>{
      setCurrentTime(data.time)
      setMessage(data.message)
    })
  }, [])


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Well its {currentMessage}.

          current time is {currentTime}.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
