import { configureStore } from "@reduxjs/toolkit";
import logger from "redux-logger";

import { gymsReducer } from "../reducers/gyms_reducer";
// import { raidsReducer } from "../reducers/raids_reducer";

// const reducer = {
//     gyms: gymsReducer,
//     raids: raidsReducer,
// };

export const configureAppStore = preloadedState => {
    const store = configureStore({
        reducer: gymsReducer,
        preloadedState
    });

    return store;
};