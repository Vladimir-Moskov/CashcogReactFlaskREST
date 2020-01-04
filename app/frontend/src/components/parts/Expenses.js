import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getExpenses, approveExpense, disapproveExpense } from "../../actions/expenses";
import { APPROVE_VALUE, DISAPPROVE_VALUE} from "../../actions/types";

export class Expenses extends Component {
    static propTypes = {
        expenses: PropTypes.array.isRequired,
        getExpenses: PropTypes.func.isRequired,
        approveExpense: PropTypes.func.isRequired,
        disapproveExpense: PropTypes.func.isRequired,
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
             {/* <th>APPROVED BY</th>
              <th>APPROVED TIME</th>
              */}
              <th>APPROVE </th>
              <th> </th>
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
              {/*   <td>{expense_item.approved_by}</td>
                <td>{expense_item.approved_datetime}</td>
                <td align="center" style="text-align:center; font-size:150%; font-weight:bold; color:green;">&#10004;</td>
               */}
                   {expense_item.approve_state == APPROVE_VALUE ?
                    (<td className="text-success">&#10004;</td>):
                    (<td className="text-danger">&#10539;</td>)
                   }
                <td>
                 {expense_item.approve_state == APPROVE_VALUE ? (
                    <button
                     onClick={this.props.disapproveExpense.bind(this, expense_item)}
                    className="btn btn-danger btn-sm"
                  >
                    {" "}
                    Disapprove
                  </button>
                  ) : (
                     <button
                     onClick={this.props.approveExpense.bind(this, expense_item)}
                    className="btn btn-primary"
                  >
                    {" "}
                    Approve
                  </button>
                  )}
                  </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
        )
    }
}
//

const mapStateToProps = state => ({
  expenses: state.expenses.expenses
});

export default connect(
  mapStateToProps,
  { getExpenses, approveExpense, disapproveExpense }
)(Expenses);

