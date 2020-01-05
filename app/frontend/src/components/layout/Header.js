import React, { Component } from "react";
import { NavLink } from "react-router-dom";

export class Header extends Component {

  render() {
    return (
            <nav className="navbar navbar-expand-sm navbar-light bg-light" >
              <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01"
                 aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
              </button>
              <div className="collapse navbar-collapse" id="navbarTogglerDemo01">
                <a className="navbar-brand" href="#">Interview XCNT GmbH </a>
                <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
                    <li className="nav-item active">
                        <NavLink className="nav-link" to="/">Home<span className="sr-only">(current)</span></NavLink>
                    </li>
                    <li className="nav-item active">
                         <NavLink className="nav-link" to="/expenses">Expenses<span className="sr-only">(current)</span></NavLink>
                    </li>
                    <li className="nav-item active">
                         <NavLink className="nav-link" to="/employees">Employees<span className="sr-only">(current)</span></NavLink>
                    </li>
                    <li className="nav-item active">
                         <NavLink className="nav-link" to="/Logs">Logs<span className="sr-only">(current)</span></NavLink>
                    </li>
                </ul>
              </div>
            </nav>
    )

  }
}

export default Header

