import axios from "axios";
import { GET_EMPLOYEES } from "./types";

// GET GET_EMPLOYEES
export const getEmployees = () => (dispatch, getState) => {
  axios
    .get("http://127.0.0.1:5001/cashcogReact/api/v1/employees")
    .then(res => {
      dispatch({
        type: GET_EMPLOYEES,
        payload: res.data.data
      });
    })
    .catch(err =>console.log(err)
      //dispatch(returnErrors(err.response.data, err.response.status))
    );
};

