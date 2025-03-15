// src/reducers/index.js
import { combineReducers } from 'redux';

// Example reducers (replace with your actual reducers)
const exampleReducer = (state = {}, action) => {
  switch (action.type) {
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  example: exampleReducer, // Add your reducers here
});

export default rootReducer;