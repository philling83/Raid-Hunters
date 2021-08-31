import { createReducer } from "@reduxjs/toolkit";

const initialState = {
    gyms: {},
};

export const gymsReducer = createReducer(initialState, builder => {
    builder
        .addCase("RECEIVE_GYMS", (state, action) => {
            const gyms = {};
            action.payload.map(gym => gyms[gym.id] = gym);
            state.gyms = gyms;
        })
});