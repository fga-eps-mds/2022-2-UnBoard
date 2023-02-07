import React from "react";
import "./sidebar.css"
import { slide as Menu } from 'react-burger-menu';

const SideBar = (props) => {
    return(
        <Menu>
            <h3>Ano do Vestibular</h3>
            <br></br>
            <a className="menu-item" onClick={() => props.onYearSelection(23)}>
                2023
            </a>
            <a className="menu-item" onClick={() => props.onYearSelection(22)}>
                2022
            </a>
            <a className="menu-item" onClick={() => props.onYearSelection(19)}>
                2019
            </a>
            <a className="menu-item" onClick={() => props.onYearSelection(18)}>
                2018
            </a>
            <a className="menu-item" onClick={() => props.onYearSelection(17)}>
                2017
            </a>
            <a className="menu-item" onClick={() => props.onYearSelection(16)}>
                2016
            </a>
            <a className="menu-item" onClick={() => props.onYearSelection(15)}>
                2015
            </a>
    </Menu>


    );
};
export default SideBar;