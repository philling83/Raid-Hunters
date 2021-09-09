import React, { useEffect } from "react";
import { connect } from "react-redux";
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

import { fetchRaids } from "../actions/raids_actions";

const RaidCard = ({ fetch, raids }) => {
    
    useEffect(() => {
        fetch();
        console.log(raids);
    }, [raids.length]);

    return raids.map((raid, i) => {

    })
};

const msp = state => ({
    raids: state.raids ? Object.values(state.raids) : []
});

const mdp = dispatch => ({
    fetch: () => dispatch(fetchRaids()),
})

export default connect(msp, mdp)(RaidCard);