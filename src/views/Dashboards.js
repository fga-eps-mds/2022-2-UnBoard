import React from "react";
import SideBar from "../Sidebars/sidebar";
import "../App.css";

class Dashboards extends React.Component{
    render(){
        return(
            <>
            <SideBar></SideBar>
            
            <div className="App">
                <div className="search">
                    <h4>Pesquisar curso</h4>
                    <input type="text" className="search-course"/>
                </div>
               <center><h1>Vestibular 2023 - UnB</h1></center><br></br><br></br>
                <div className="img-d">
                <center><img src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/Imagens/WhatsApp%20Image%202022-12-14%20at%2019.15.56.jpeg"/></center>
                </div>
            </div>
            


                
            </>
        )

              
    }
}

export default Dashboards