import React, { useEffect } from "react";
import { connect } from "react-redux";
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

import "./RaidCard.css";
import { fetchRaids } from "../actions/raids_actions";

const RaidCard = ({ raids }) => {

    return raids.map((raid, i) =>
        <div className="flip-card">
            <div className="flip-card-inner">
                <Card variant="outlined" className="raid_card flip-card-front">
                    <CardContent>
                        <img src={raid.url_img} alt={raid.pokemon} />
                        <Typography>
                            {raid.pokemon}
                        </Typography>
                    </CardContent>
                </Card>
                <Card variant="outlined" className="raid_card flip-card-back">
                    <CardContent>
                        <Typography>
                            {raid.pokemon}
                        </Typography>
                        <Typography>
                            CP Range: {raid.min_cp_range} - {raid.max_cp_range}
                        </Typography>
                        <Typography>
                            Boosted CP Range: {raid.boosted_min_cp_range} - {raid.boosted_max_cp_range}
                        </Typography>
                    </CardContent>
                </Card>
            </div> 
        </div>
    )
};

export default RaidCard;