import React, { useEffect } from "react";
import { connect } from "react-redux";
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

import "./RaidCard.css";
import { fetchRaids } from "../actions/raids_actions";

const RaidCard = ({ fetch, raids }) => {
    
    useEffect(() => {
        fetch();
        console.log(raids);
    }, [raids.length]);

    return raids.map((raid, i) =>
        <div className="flip-card">
            <div className="flip-card-inner">
                <Card key={i} variant="outlined" className="raid_card flip-card-front">
                    <CardContent>
                        <img src={raid.url_img} alt={raid.pokemon} />
                        <Typography>
                            {raid.pokemon}
                        </Typography>
                    </CardContent>
                </Card>
                <Card key={i} variant="outlined" className="raid_card flip-card-back">
                    <CardContent>
                        <Typography>
                            {raid.pokemon}
                        </Typography>
                    </CardContent>
                </Card>
            </div> 
        </div>
    )
};

const msp = state => ({
    raids: state.raids ? Object.values(state.raids) : []
});

const mdp = dispatch => ({
    fetch: () => dispatch(fetchRaids()),
})

export default connect(msp, mdp)(RaidCard);