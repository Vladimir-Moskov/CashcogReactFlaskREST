import { combineReducers } from "redux";
import logs from "./logs";
import employees from "./employees";
import expenses from "./expenses";

export default combineReducers({
  expenses,
  employees,
  logs
});
