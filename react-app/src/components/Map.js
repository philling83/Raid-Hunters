// import React, { useEffect, useRef, useState } from 'react'
// import L from 'leaflet'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

import "./Map.css";

function MapSimple() {

    // let mymap = L.map('mapid').setView([51.505, -0.09], 13);

    return (
        <MapContainer className="map_container" center={ [51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
            <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={[51.505, -0.09]}>
                <Popup>
                    
                </Popup>
            </Marker>
        </MapContainer>
    );
};

export default MapSimple;