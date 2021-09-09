import { createAction } from "@reduxjs/toolkit";

export const receiveRaids = createAction("RECEIVE_RAIDS");

export const fetchRaids = () => async dispatch => {
    try {
        const res = await fetch("/api/raids");
        const resJSON = await res.json()
        dispatch(receiveRaids(resJSON));
    } catch (err) {
        console.log(err, "No raids");
    };
};