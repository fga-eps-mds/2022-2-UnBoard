import React from "react";
import "./sidebar.css"
import { slide as Menu } from 'react-burger-menu';

const SideBar = () => {
    return(
        <Menu>
            <h3>Ano do Vestibular</h3>
            <br></br>
            <a className="menu-item" href="/dashboards">
                2023
            </a>
            <a className="menu-item" href="/dashboards">
                2022
            </a>
            <a className="menu-item" href="/dashboards">
                2019
            </a>
            <a className="menu-item" href="/dashboards">
                2018
            </a>
            <a className="menu-item" href="/dashboards">
                2017
            </a>
            <a className="menu-item" href="/dashboards">
                2016
            </a>
            <a className="menu-item" href="/dashboards">
                2015
            </a>
    </Menu>


    );
};
export default SideBar;