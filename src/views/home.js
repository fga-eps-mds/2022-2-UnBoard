import React from "react";
import "../App.css";




class Home extends React.Component{
    render(){

        return(
            <>
            <div className="App">
                <br></br><br></br><br></br><br></br>
                <h1>UnBoard</h1>
                <div className="box">
                    <img width="800" height="500" src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/front/Imagens/Design%20sem%20nome.png"/>
                </div>
               <h3>Informações sobre o ingresso na Universidade de Brasília</h3>
               <br></br>
               <div className="copy">
                    <center>
                        <h6>Squad6 2023 © </h6>
                    </center>
               </div>
            </div>

            </>
        )

              
    }
}

export default Home