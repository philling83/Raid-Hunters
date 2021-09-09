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
            if (raid.tier === "mega" && raid.is_active === true) {
                megaRaids.push(raid);
            };

            return megaRaids;
        });

        return (
            <RaidCard raids={megaRaids}/>
        );
    };

    const generateRaidTierFive = () => {
        const tierFiveRaids = [];
        
        raids.map(raid => {
            if (raid.tier === "5" && raid.is_active === true) {
                tierFiveRaids.push(raid);
            };

            return tierFiveRaids;
        });

        return (
            <RaidCard raids={tierFiveRaids}/>
        );
    };

    const generateRaidTierThree = () => {
        const tierThreeRaids = [];
        
        raids.map(raid => {
            if (raid.tier === "3" && raid.is_active === true) {
                tierThreeRaids.push(raid);
            };

            return tierThreeRaids;
        });

        return (
            <RaidCard raids={tierThreeRaids}/>
        );
    };

    const generateRaidTierOne = () => {
        const tierOneRaids = [];
        
        raids.map(raid => {
            if (raid.tier === "1" && raid.is_active === true) {
                tierOneRaids.push(raid);
            };

            return tierOneRaids;
        });

        return (
            <RaidCard raids={tierOneRaids}/>
        );
    };

    return (
        <div className="raids_container">
            <div className="raids_op">
                <h1>
                    Tier Mega
                    {generateRaidTierMega()}
                </h1>
                <h1>
                    Tier 5
                    {generateRaidTierFive()}
                </h1>
            </div>
            <h1 className="raids_tier3">
                Tier 3
                {generateRaidTierThree()}
            </h1>
            <h1 className="raids_tier1">
                Tier 1
                {generateRaidTierOne()}
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