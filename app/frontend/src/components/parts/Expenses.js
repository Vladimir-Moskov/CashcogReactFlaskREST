import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getExpenses, approveExpense, disapproveExpense } from "../../actions/expenses";
import { APPROVE_VALUE, DISAPPROVE_VALUE} from "../../actions/types";

// Import React Table
import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';


 const approvedType = {
      0: 'None',
      1: 'Approved',
      2: 'Disapproved'
    };

class ApprovedFormatter extends React.Component {
  render() {
    return (

    <div>
        { this.props.approve_state == APPROVE_VALUE ?
        (<span className="text-success">&#10004;</span>):
        (<span className="text-danger">&#10539;</span>)
         }
    </div>
    );
  }
}

class ApprovedButtonFormatter extends React.Component {
  render() {
    return (

    <div>
       { this.props.approve_state == APPROVE_VALUE ?

        (<button
            onClick={this.props.parent.props.disapproveExpense.bind(this.props.parent, this.props.expense_item)}
            className="btn btn-danger btn-sm"
          >
            {" "}
            Disapprove
          </button>) :
          (
             <button
             onClick={this.props.parent.props.approveExpense.bind(this.props.parent, this.props.expense_item)}
            className="btn btn-primary"
          >
            {" "}
            Approve
          </button>
          )
         }
    </div>
    );
  }
}

function approveFormatter(cell, row) {
  return (
    <ApprovedFormatter approve_state={ cell } />
  );
}

export class Expenses extends Component {

    approvedButtonFormatter() {
      let parentVal = this;
      return (cell, row) => {
        return (<ApprovedButtonFormatter approve_state={ cell } expense_item={ row } parent={ parentVal }/>);
      }
    }
    static propTypes = {
        expenses: PropTypes.array.isRequired,
        getExpenses: PropTypes.func.isRequired,
        approveExpense: PropTypes.func.isRequired,
        disapproveExpense: PropTypes.func.isRequired,
     };

      componentDidMount() {
        this.props.getExpenses();
         this.options = {
          defaultSortName: 'name',  // default sort column name
          defaultSortOrder: 'desc'  // default sort order
        };
      }

    render(){
        return (
        <div>
            <h2>Expenses</h2>
            <BootstrapTable data={ this.props.expenses } options={ this.options } striped hover condensed pagination version='4'>
              <TableHeaderColumn dataField='id' isKey dataSort={ true }>ID</TableHeaderColumn>
              <TableHeaderColumn dataField='employee_name' dataSort={ true }>EMPLOYEE</TableHeaderColumn>
              {/*<TableHeaderColumn dataField='description'> DESCRIPTION </TableHeaderColumn>*/}
              <TableHeaderColumn dataField='created_at' dataSort={ true }  filter={ { type: 'DateFilter' } }> CREATED </TableHeaderColumn>
              <TableHeaderColumn dataField='currency' dataSort={ true }>CURRENCY</TableHeaderColumn>
              <TableHeaderColumn dataField='amount' filter={ { type: 'TextFilter', delay: 1000 } } dataSort={ true }>AMOUNT</TableHeaderColumn>
              <TableHeaderColumn dataField='approve_state' dataAlign='center' dataFormat={ approveFormatter }
                dataSort={ true } formatExtraData={ approvedType }
                filter={ { type: 'SelectFilter', options: approvedType } }>APPROVED</TableHeaderColumn>
              <TableHeaderColumn dataField='approve_state' dataAlign='center' dataFormat={ this.approvedButtonFormatter() }> </TableHeaderColumn>
            </BootstrapTable>
        </div>
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

