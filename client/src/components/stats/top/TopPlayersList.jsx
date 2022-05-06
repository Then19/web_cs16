import React, {useEffect, useState} from 'react';
import StatsLabel from "./StatsLabel";
import {getUsersTop} from "../../../api/user";
import "./top.css"

const TopPlayersList = () => {

    const [userData, setUserData] = useState({})

    useEffect(() => {
        getUsersTop()
            .then(res =>{
                setUserData(res)
            })
    }, [])


    return (
        userData['top5_kills'] !== undefined &&
        <div className={'list-top-block'}>
            <StatsLabel StatsData={userData.top5_kills} Title={'Top 5 kills'} obj={'kills'} objTitle={"Kills"} key={userData.top5_kills[0].name}/>
            <StatsLabel StatsData={userData.top5_damage} Title={'Top 5 damage'} obj={'dmg'} objTitle={"Damage"} key={userData.top5_damage[0].name}/>
            <StatsLabel StatsData={userData.top5_time} Title={'Top 5 time'} obj={'connection_time'} objTitle={"Time"} key={userData.top5_time[0].name}/>
        </div>
    );


};

export default TopPlayersList;