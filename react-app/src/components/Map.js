import React, { useEffect, useRef, useState, useSelector } from 'react'
// import L from 'leaflet'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { connect } from "react-redux";

import "./Map.css";
import { fetchGyms } from "../actions/gyms_actions";

function MapSimple({ fetch, gyms }) {

    useEffect(() => {
        fetch()
    }, [gyms.length])

    const generateGymMarkers = () => {
        return gyms.map((gym, i) => 
            <Marker position={[gym.latitude, gym.longitude]}>
                <Popup>
                    <Card className={classes.root}>
                        <CardContent>
                            <Typography className={classes.title} color="textSecondary" gutterBottom>
                                Word of the Day
                            </Typography>
                            <Typography variant="h5" component="h2">
                                be{bull}nev{bull}o{bull}lent
                            </Typography>
                            <Typography className={classes.pos} color="textSecondary">
                                adjective
                            </Typography>
                            <Typography variant="body2" component="p">
                                well meaning and kindly.
                                <br />
                                {'"a benevolent smile"'}
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <Button size="small">Learn More</Button>
                        </CardActions>
                    </Card>
                </Popup>
            </ Marker>
        )
    }

    // const useStyles = makeStyles({
    //     root: {
    //         minWidth: 275,
    //     },
    //     bullet: {
    //         display: 'inline-block',
    //         margin: '0 2px',
    //         transform: 'scale(0.8)',
    //     },
    //     title: {
    //         fontSize: 14,
    //     },
    //     pos: {
    //         marginBottom: 12,
    //     },
    // });

    // const classes = useStyles();
    // const bull = <span className={classes.bullet}>•</span>;

    // let mymap = L.map('mapid').setView([51.505, -0.09], 13);

    return (
        <MapContainer className="map_container" center={ [40.783, -74.698]} zoom={13} scrollWheelZoom={false}>
            <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {generateGymMarkers()}
        </MapContainer>
    );
};

const msp = state => ({
    gyms: state.gyms ? Object.values(state.gyms) : []
});

const mdp = dispatch => ({
    fetch: () => dispatch(fetchGyms()),
})

export default connect(msp, mdp)(MapSimple);