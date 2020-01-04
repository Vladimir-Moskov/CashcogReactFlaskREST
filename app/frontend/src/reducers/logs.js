import { GET_LOGS } from "../actions/types.js";

const initialState = {
  logs: []
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_LOGS:
      return {
        ...state,
        logs: action.payload
      };

    default:
      return state;
  }
}
