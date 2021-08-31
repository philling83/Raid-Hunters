import { createAction } from "reduxjs/toolkit";

export const receiveGyms = createAction("RECEIVE_GYMS");

export const fetchGyms = () => async dispatch => {
    try {
        const res = await fetch("/api/gyms");
        dispatch(receiveGyms(res.data));
    } catch (err) {
        console.log("Gyms broken");
    };
};