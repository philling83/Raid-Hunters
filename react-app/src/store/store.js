import { configureStore } from "@reduxjs/toolkit";
import logger from "redux-logger";

import { gymsReducer } from "../reducers/gyms_reducer";

export const configureAppStore = preloadedState => {
    const store = configureStore({
        reducer: gymsReducer,
        preloadedState
    });

    return store;
};