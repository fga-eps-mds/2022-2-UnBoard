import React from "react";
import "../App.css";

class Sobre extends React.Component{
    render(){

        return(
            <>
             <div className="App">
               <center>
                    <h1>O que é o projeto UnBoard?</h1>
                    <br></br>
                    <div className="img-logo">
                        <img width="700" height="500" src="https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/Imagens/Fly%20bird%20logo.png"/>
                    </div>
                    <br></br>
                    <h2>O projeto UnBoard é desenvolvido e atualizado por uma equipe de estudantes da Universidade de Brasília (UnB), por meio da disciplina de Métodos de Desenvolvimento de Software. Nosso objetivo é disponibilizar dados estatísticos importantes sobre o acesso à UnB pelo vestibular tradicional, que é responsavel por 25% das vagas ofertadas. O projeto foi pensado para que seus usuários possam ter acesso a quantidade de vagas ofertadas, demanda de vagas e outros dados de cada Campus, de forma que essas informacões os ajudem na hora de escolher o curso e ingressar na tão sonhada Universidade.</h2>
                </center>
                <div className="container">
                    <div className="card">
                        <div className="images">
                            <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/breno.jpg'></img>
                            <br></br>
                        </div>
                        <div className="text">
                            
                            <h2 className="name">Breno Yuri</h2>
                            
                            <p className="contact">https://github.com/YuriBre</p>
                        </div>
                    </div>
                    <div className="card">
                        <div className="images">
                            <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/danilo.jpeg'></img>
                            <br></br>
                        </div>
                        <div className="text">
                            
                            <h2 className="name">Danilo Carvalho</h2>
                            
                            <p className="contact">https://github.com/Danilo-Carvalho-Antunes</p>
                        </div>
                    </div>
                    <div className="card">
                        <div className="images">
                            <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/guilherme.jpeg'></img>
                            <br></br>
                        </div>
                        <div className="text">
                            
                            <h2 className="name">Guilherme Kishimoto</h2>
                            
                            <p className="contact">https://github.com/guilhermekishimoto</p>
                        </div>
                    </div>
                </div>
                <div className="container">
                    <div className="card">
                        <div className="images">
                            <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/joao.jpeg'></img>
                            <br></br>
                        </div>
                        <div className="text">
                            
                            <h2 className="name">João Barreto</h2>
                            
                            <p className="contact">https://github.com/JoaoBarreto03</p>
                        </div>
                    </div>
                    <div className="card">
                        <div className="images">
                            <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/mizael.jpg'></img>
                            <br></br>
                        </div>
                        <div className="text">
                            
                            <h2 className="name">Francisco Mizael</h2>
                            
                            <p className="contact">https://github.com/frmiza</p>
                        </div>
                    </div>
                    <div className="card">
                        <div className="images">
                            <img clasName="photo" width="180" height="180" src='https://raw.githubusercontent.com/fga-eps-mds/2022-2-UnBoard/main/assets/Raphael%20(c%C3%B3pia).png'></img>
                            <br></br>
                        </div>
                        <div className="text">
                            
                            <h2 className="name">Raphael Mendes</h2>
                            
                            <p className="contact">https://github.com/Raphides</p>
                        </div>
                    </div>
                </div>
            </div>
           


           
            </>
        )

              
    }
}

export default Sobre