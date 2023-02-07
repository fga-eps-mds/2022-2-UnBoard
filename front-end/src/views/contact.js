import React from "react";
import "../App.css";

class Contact extends React.Component {
    render() {
        return (
            <>
                <div className="App">
                    <div className="contact">
                        <h1>Contato</h1>
                    </div>
                    <div className="container-t">
                        <div className="card-t">
                            <div className="images">

                                <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/breno.jpg'></img>
                                <br></br>
                            </div>
                            <div className="text">

                                <h2 className="name">Breno Yuri</h2>

                                <p className="contact"><a href="https://github.com/YuriBre">Contato GitHub</a></p>
                            </div>
                        </div>
                        <div className="card-t">
                            <div className="images">
                                <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/danilo.jpeg'></img>
                                <br></br>
                            </div>
                            <div className="text">

                                <h2 className="name">Danilo Carvalho</h2>

                                <p className="contact"><a href="https://github.com/Danilo-Carvalho-Antunes">Contato GitHub</a></p>
                            </div>
                        </div>
                        <div className="card-t">
                            <div className="images">
                                <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/guilherme.jpeg'></img>
                                <br></br>
                            </div>
                            <div className="text">

                                <h2 className="name">Guilherme Kishimoto</h2>

                                <p className="contact"><a href="https://github.com/guilhermekishimoto">Contato GitHub</a></p>
                            </div>
                        </div>
                    </div>
                    <div className="container-t2">
                        <div className="card-t">
                            <div className="images">
                                <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/joao.jpeg'></img>
                                <br></br>
                            </div>
                            <div className="text">

                                <h2 className="name">João Barreto</h2>

                                <p className="contact"><a href ="https://github.com/JoaoBarreto03">Contato Github</a></p>
                            </div>
                        </div>
                        <div className="card-t">
                            <div className="images">
                                <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/mizael.jpg'></img>
                                <br></br>
                            </div>
                            <div className="text">

                                <h2 className="name">Francisco Mizael</h2>

                                <p className="contact"><a href="https://github.com/frmiza">Contato GitHub</a></p>
                            </div>
                        </div>
                        <div className="card-t">
                            <div className="images">
                                <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/Raphael%20(c%C3%B3pia).png'></img>
                                <br></br>
                            </div>
                            <div className="text">

                                <h2 className="name">Raphael Mendes</h2>

                                <p className="contact"><a href="https://github.com/Raphides">Contato GitHub</a></p>
                            </div>
                        </div>
                    </div>

                </div>




            </>

        )
    }
}

export default Contact