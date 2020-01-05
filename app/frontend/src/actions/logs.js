import axios from "axios";
import { GET_LOGS } from "./types";

// GET GET_LOGS
export const getLogs = () => (dispatch, getState) => {
  axios
    .get("http://127.0.0.1:5001/cashcogXCNT/api/v1/logs")
    .then(res => {
      dispatch({
        type: GET_LOGS,
        payload: res.data.data
      });
    })
    .catch(err =>console.log(err)
      //dispatch(returnErrors(err.response.data, err.response.status))
    );
};

