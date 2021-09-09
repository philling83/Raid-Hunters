import React, { useEffect } from "react";
import { connect } from "react-redux";

import "./Raid.css";
import RaidCard from "./RaidCard";
import { fetchRaids } from "../actions/raids_actions";

const Raid = ({ fetch, raids }) => {

    useEffect(() => {
        fetch();
        console.log(raids);
    }, [raids.length]);

    const generateRaidTierMega = () => {
        const megaRaids = [];
        
        raids.map(raid => {
            if (raid.tier === "mega") {
                megaRaids.push(raid);
            };
        });

        return (
            <RaidCard raids={megaRaids}/>
        )
    }

    return (
        <div className="raids_container">
            <div className="raids_op">
                <h1>
                    Tier Mega
                </h1>
                {generateRaidTierMega()}
                <h1>
                    Tier 5
                </h1>
            </div>
            <h1 className="raids_tier3">
                Tier 3
            </h1>
            <h1 className="raids_tier1">
                Tier 1
            </h1>
        </div>
    )
};

const msp = state => ({
    raids: state.raids ? Object.values(state.raids) : []
});

const mdp = dispatch => ({
    fetch: () => dispatch(fetchRaids()),
})

export default connect(msp, mdp)(Raid);