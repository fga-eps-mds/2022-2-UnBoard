import React, { useState } from "react";
import SideBar from "../Sidebars/sidebar";
import "../App.css";

const Dashboards = () => {
  const [year, setYear] = useState(23);

  const handleYearSelection = (selectedYear) => {
    setYear(selectedYear);
  };

  return (
    <>

      <div className="App">
        <div className="search">
          <center>
            <h2>Vestibular - UnB</h2>
          </center>
        </div>
        <br />
        <br />
        <div className="img-d">
            <center>
                    <iframe 
                    src="http://localhost:8050/" 
                    width="1300" height="700" 
                    style={{ 
                    marginTop: "20px", 
                    marginLeft: "50px", 
                    position: "absolute",
                    top: "200px", 
                    left: "40px" 
                    }} 
                    />
                </center>
        </div>

      </div>
    </>
  );
};

export default Dashboards;