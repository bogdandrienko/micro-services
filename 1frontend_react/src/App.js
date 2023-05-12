import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import { useState } from 'react';


function App() {
  const [getterLogs, setterLogs] = useState([])

  async function getData(){
    const response = await axios.get("http://192.168.0.144:8001/api")
    console.log(response)
    // let logs_ = [
    //   {id: 1, title: "Title 1", value: 666},
    //   {id: 2, title: "Title 2", value: 667},
    //   {id: 3, title: "Title 3", value: 668},
    // ]
    setterLogs(response.data)
  }


  return (
    <div className="App">
      <header className="App-header">
        <button onClick={getData}>getData</button>
      <div>
        {getterLogs && getterLogs.length > 0 ? (
          <ul>
            {getterLogs.map((item, index) => (
              <li>({item.id}) {item.title} [{item.value}]</li>
            ))}
          </ul>
        ) : "Data not found"}
      </div>
      </header>
    </div>
  );
}

export default App;
