import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getExpenses } from "../../actions/expenses";

export class Expenses extends Component {
    static propTypes = {
        expenses: PropTypes.array.isRequired,
        getExpenses: PropTypes.func.isRequired
     };

      componentDidMount() {
        this.props.getExpenses();
      }

    render(){
        return (

        <Fragment>
        <h2>Expenses</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>UUID</th>
              <th>DESCRIPTION</th>
              <th>CREATED AT</th>
              <th>CURRENCY</th>
              <th>AMOUNT</th>
              <th>APPROVED BY</th>
              <th>APPROVED TIME</th>
              <th>APPROVE </th>
            </tr>
          </thead>
          <tbody>


            {this.props.expenses.map(expense_item => (
              <tr key={expense_item.id}>
                <td>{expense_item.id}</td>
                <td>{expense_item.uuid}</td>
                <td>{expense_item.description}</td>
                <td>{expense_item.created_at}</td>
                <td>{expense_item.currency}</td>
                <td>{expense_item.amount}</td>
                <td>{expense_item.approved_by}</td>
                <td>{expense_item.approved_datetime}</td>
                <td>{expense_item.approve_state}</td>
                <td>
                    <button

                    className="btn btn-danger btn-sm"
                  >
                    {" "}
                    Approve
                  </button>
                  </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
        )
    }
}
//  onClick={this.props.deleteLead.bind(this, lead.id)}

const mapStateToProps = state => ({
  expenses: state.expenses.expenses
});

export default connect(
  mapStateToProps,
  { getExpenses }
)(Expenses);

