import React from "react";
import SideBar from "../Sidebars/sidebar";
import "../App.css";

class Dashboards extends React.Component {
    render() {
        return (
            <>
                <SideBar></SideBar>

                <div className="App">
                    <div className="search">
                        <h4>Pesquisar curso</h4>
                        <input type="text" className="search-course" />
                    </div>
                    <center><h1>Vestibular 2023 - UnB</h1></center><br></br><br></br>
                    <div className="img-d">
                        <center><iframe src="http://localhost:8050/" width="1500" height="700"></iframe></center>
                    </div>
                </div>




            </>
        )


    }
}

export default Dashboards