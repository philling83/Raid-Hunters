import { createReducer } from "@reduxjs/toolkit";

const initialState = {
    gyms: {},
    raids: {},
};

export const gymsReducer = createReducer(initialState, builder => {
    builder
        .addCase("RECEIVE_GYMS", (state, action) => {
            const gyms = {};
            action.payload.gyms.map(gym => gyms[gym.id] = gym);
            state.gyms = gyms;
            return state
        })
        .addCase("RECEIVE_RAIDS", (state, action) => {
            const raids = {};
            action.payload.raids.map(raid => raids[raid.id] = raid);
            state.raids = raids;
            return state
        })
});