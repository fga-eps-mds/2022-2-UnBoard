import React from "react";
import "../App.css";

class Home extends React.Component {
  render() {
    return (
      <div className="App">
        <br></br><br></br><br></br><br></br>
        <h1>UnBoard</h1>
        <div className="box">
          <img
            style={{ width: "500px", height: "500px", marginTop: "20px", marginLeft:"1200px" }}
            src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/frontend/Imagens/Design%20sem%20nome.png"
          />
        </div>
        <h3>Informações sobre o ingresso na Universidade de Brasília</h3>
        <div className="copy">
          <center>
            <h6>Squad6 2023 © </h6>
          </center>
        </div>
      </div>
    );
  }
}

export default Home;
