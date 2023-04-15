import { useState } from "react";
import "./App.css";
const App = () => {
  const [value, setValue] = useState("");
  const [password, setPassword] = useState("");
  function handleChange(event) {
    setValue(event.target.value);
  }
  function handlePassword(event) {
    setPassword(event.target.password);
  }
  function handleSubmit(event) {
    alert("submitted");
    event.preventDefault();
  }
  return (
    <div className="container">
      <div className="item1">
        <iframe
          className="gif"
          src="https://giphy.com/embed/IsKFVXvVxyeN1aXfgj"
        ></iframe>
      </div>
      <div className="item2">
        <form onSubmit={handleSubmit}>
          <label>
            User Id
            <br />
            <br />
            <input type="text" value={value} onChange={handleChange} />
            <br />
            <br />
            Password
            <br />
            <br />
            <input type="password" value={password} onChange={handlePassword} />
            <br />
            <br />
            Face ID
            <br />
            <br />
            <input className="faceid" type="Submit" value="faceID" />
          </label>
        </form>
      </div>
    </div>
  );
};

export default App;
