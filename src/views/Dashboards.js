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
      <SideBar onYearSelection={handleYearSelection} />

      <div className="App">
        <div className="search">
          <h4>Pesquisar curso</h4>
          <input type="text" className="search-course" />
        </div>
        <center>
          <h1>Vestibular 20{year} - UnB</h1>
        </center>
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