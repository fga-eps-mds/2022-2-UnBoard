import React from 'react';
import Home from './views/home';
import NavBar from './Navbars/navbar';
import "./Navbars/navbar.css";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sobre from './views/sobre';
import Dashboards from './views/Dashboards';
import "./App.css";

function App() {
  return (
    <Router>
      <NavBar></NavBar>
      <Routes>
        <Route path="/home" element={<Home />}/>
        <Route path="/sobre" element={<Sobre />}/>
        <Route path="/Dashboards" element={<Dashboards />}/>

      </Routes>


    </Router>
  );
}

export default App;
