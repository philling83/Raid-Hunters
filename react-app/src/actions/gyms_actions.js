import { createAction } from "@reduxjs/toolkit";

export const receiveGyms = createAction("RECEIVE_GYMS");

export const fetchGyms = () => async dispatch => {
    try {
        const res = await fetch("/api/gyms");
        const resJSON = await res.json()
        dispatch(receiveGyms(resJSON));
    } catch (err) {
        console.log(err, "Gyms broken");
    };
};