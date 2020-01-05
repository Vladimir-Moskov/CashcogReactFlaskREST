import React, { Component, Fragment } from "react";
import ReactDOM from 'react-dom';
import Header from './layout/Header'
import Dashboard from "./parts/Dashboard";
import { Provider } from "react-redux";
import store from "../store";
import { HashRouter } from "react-router-dom";

class App extends Component {
    render(){
         return (
             <Provider store={store}>
               <HashRouter>
                    <Header/>
                    <div className="container">
                        <Dashboard/>
                    </div>
                </HashRouter>
             </Provider>
         )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
