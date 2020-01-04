import React, { Fragment } from "react";
import Logs from "./Logs";
import Employees from "./Employees";
import Expenses from "./Expenses";
import Home from "./Home";

import { Route } from "react-router-dom";

export default function Dashboard() {
  return (
        <Fragment>

          <div className="content">
            <Route exact  path="/" component={Home}/>
            <Route path="/expenses" component={Expenses}/>
            <Route path="/employees" component={Employees}/>
            <Route path="/logs" component={Logs}/>
          </div>
        </Fragment>
  );
}
