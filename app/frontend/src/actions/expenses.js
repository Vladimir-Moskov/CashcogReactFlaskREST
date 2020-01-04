import axios from "axios";
import { GET_EXPENSES, APPROVE_EXPENSE, DISAPPROVE_EXPENSE} from "./types";
import { APPROVE_VALUE, DISAPPROVE_VALUE} from "./types";

// GET GET_EXPENSES
export const getExpenses = () => (dispatch, getState) => {
  axios
    .get("http://127.0.0.1:5001/cashcogXCNT/api/v1/expenses")
    .then(res => {
      dispatch({
        type: GET_EXPENSES,
        payload: res.data.data
      });
    })
    .catch(err =>console.log(err)

      //dispatch(returnErrors(err.response.data, err.response.status))
    );
};

const header_put = { 'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",}
// PUT APPROVE_EXPENSES
export const approveExpense = expense_item => (dispatch, getState) => {
  expense_item['approve'] = APPROVE_VALUE;
  axios
    .put(`http://127.0.0.1:5001/cashcogXCNT/api/v1/expense/${expense_item.id}/approve`,
        expense_item,
       {
        headers: header_put
        } )
    .then(res => {
      dispatch({
        type: APPROVE_EXPENSE,
        payload: expense_item.id
      });
       dispatch(getExpenses());
    })
    .catch(err =>console.log(err)

      //dispatch(returnErrors(err.response.data, err.response.status))
    );
};

// PUT DISAPPROVE_EXPENSE
export const disapproveExpense = expense_item => (dispatch, getState) => {
  expense_item['approve'] = DISAPPROVE_VALUE;
  axios
    .put(`http://127.0.0.1:5001/cashcogXCNT/api/v1/expense/${expense_item.id}/approve`,
        expense_item,
       {
        headers: header_put
        } )
    .then(res => {
      dispatch({
        type: APPROVE_EXPENSE,
        payload: expense_item.id
      });
      dispatch(getExpenses());
    })
    .catch(err =>console.log(err)

      //dispatch(returnErrors(err.response.data, err.response.status))
    );
};