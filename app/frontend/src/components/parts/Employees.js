import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getEmployees } from "../../actions/employees";
import { Table } from 'react-bootstrap';

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
        <Table striped bordered hover size="sm">
        {/*<table className="table table-striped">*/}
          <thead>
            <tr>
              <th>ID</th>
              <th>UUID</th>
              <th>FIRST NAME</th>
              <th>LAST NAME</th>
              <th>CREATED AT</th>
              <th>EXPENSE ID</th>
            </tr>
          </thead>
          <tbody>

            {this.props.employees.map(employee_item => (
              <tr key={employee_item.id}>
                <td>{employee_item.id}</td>
                <td>{employee_item.uuid}</td>
                <td>{employee_item.first_name}</td>
                <td>{employee_item.last_name}</td>
                <td>{employee_item.created_at}</td>
                <td>{employee_item.expense}</td>
              </tr>
            ))}
          </tbody>
          </Table>
         {/*</table>*/}
         </div>
        )
    }
}
//

const mapStateToProps = state => ({
  employees: state.employees.employees
});

export default connect(
  mapStateToProps,
  { getEmployees }
)(Employees);

