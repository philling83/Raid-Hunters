// import { createReducer } from "@reduxjs/toolkit";

// const initialState = {
//     raids: {},
// };

// export const raidsReducer = createReducer(initialState, builder => {
//     builder
//         .addCase("RECEIVE_RAIDS", (state, action) => {
//             const raids = {};
//             action.payload.raids.map(raid => raids[raid.id] = raid);
//             state.raids = raids;
//             return state
//         })
// });