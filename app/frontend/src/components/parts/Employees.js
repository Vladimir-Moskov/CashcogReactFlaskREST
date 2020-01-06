import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getEmployees } from "../../actions/employees";
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';

export class Employees extends Component {
    static propTypes = {
        employees: PropTypes.array.isRequired,
        getEmployees: PropTypes.func.isRequired
     };

      componentDidMount() {
        this.props.getEmployees();
      }

    render(){
        return (
        <div>
        <h2>Employees</h2>
         <BootstrapTable data={ this.props.employees } striped hover condensed pagination version='4'>
              <TableHeaderColumn dataField='id' isKey dataSort={ true }>ID</TableHeaderColumn>
              <TableHeaderColumn dataField='uuid' dataSort={ true }>UUID</TableHeaderColumn>
              <TableHeaderColumn dataField='first_name' dataSort={ true } > FIRST NAME</TableHeaderColumn>
              <TableHeaderColumn dataField='last_name' dataSort={ true }>LAST NAME</TableHeaderColumn>
              <TableHeaderColumn dataField='created_at' dataSort={ true }>CREATED AT</TableHeaderColumn>
              <TableHeaderColumn dataField='expense' dataSort={ true }>EXPENSE ID</TableHeaderColumn>
            </BootstrapTable>
         </div>
        )
    }
}

const mapStateToProps = state => ({
  employees: state.employees.employees
});

export default connect(
  mapStateToProps,
  { getEmployees }
)(Employees);

