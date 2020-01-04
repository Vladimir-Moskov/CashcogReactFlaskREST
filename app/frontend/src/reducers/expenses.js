import { GET_EXPENSES } from "../actions/types.js";

const initialState = {
  expenses: []
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_EXPENSES:
      return {
        ...state,
        expenses: action.payload
      };

    default:
      return state;
  }
}
