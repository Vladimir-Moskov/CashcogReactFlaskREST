import axios from "axios";
import { GET_EXPENSES } from "./types";

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

