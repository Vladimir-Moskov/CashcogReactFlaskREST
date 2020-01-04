import axios from "axios";
import { GET_EXPENSES, APPROVE_EXPENSE, DISAPPROVE_EXPENSE} from "./types";

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
//, "Access-Control-Request-Method":
//{ "Content-Type": "application/x-www-form-urlencoded", "Access-Control-Allow-Origin": "*",  }
var header_put = { "Content-Type": "application/x-www-form-urlencoded"  }
const headers_0 = {
  'Content-Type': 'text/html',
  "Access-Control-Allow-Origin": "*",
}

const headers_1 = { 'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",}
// PUT APPROVE_EXPENSES
export const approveExpense = expense_item => (dispatch, getState) => {
  axios
    .put(`http://127.0.0.1:5001/cashcogXCNT/api/v1/expense/${expense_item.id}/approve`,
        expense_item,
       {
        headers: headers_1
        } )
    .then(res => {
      dispatch({
        type: APPROVE_EXPENSE,
        payload: res.data.data
      });
    })
    .catch(err =>console.log(err)

      //dispatch(returnErrors(err.response.data, err.response.status))
    );
};
