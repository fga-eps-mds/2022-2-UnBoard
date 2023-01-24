import React from "react";

const NavBar = () => {
    return(
        <div className="Navbar">
            <a class="navbar-brand" href="#">
                <img src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-Squad06/main/Imagens/Captura_de_tela_de_2022-12-13_11-00-59-removebg-preview.png"/>
            </a>
            
            <div className="nav-items-a">
                <a href="/home">Home</a>
            </div>
            <div className="nav-items-b">
                <a href="/Dashboards">Dashboard</a>
            </div>
            <div className="nav-items-c">
                <a href="/sobre">Sobre nós</a>
            </div>
            <div className="nav-items-d">
                <a href="/contact">Contato</a>
            </div>
            <div className="nav-toggle">
                <div className="bar"></div>
            </div>
        </div>
    );
};

export default NavBar;