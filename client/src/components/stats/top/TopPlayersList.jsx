import React, {useEffect, useState} from 'react';
import StatsLabel from "./StatsLabel";
import {getUsersTop} from "../../../api/user";
import "./top.css"

const TopPlayersList = () => {

    const [userData, setUserData] = useState({})

    useEffect(() => {
        getUsersTop()
            .then(res =>{
                res.top5_damage.map(a => a.dmg = (a.dmg / 1000).toFixed(1) + 'k')
                res.top5_time.map(a => a.connection_time = Math.floor(a.connection_time / 60 / 60) + ' ч.')
                setUserData(res)
            })
    }, [])


    return (
        userData['top5_kills'] !== undefined &&
        <div className={'list-top-block'}>
            <StatsLabel titleColor={'silver'} StatsData={userData.top5_damage} Title={'Top 5 damage'} obj={'dmg'} objTitle={"Damage"} key={userData.top5_damage[0].name + userData.top5_damage[0].dmg}/>
            <StatsLabel titleColor={'gold'} StatsData={userData.top5_kills} Title={'Top 5 kills'} obj={'kills'} objTitle={"Kills"} key={userData.top5_kills[0].name + userData.top5_damage[0].kills}/>
            <StatsLabel titleColor={'bronze'} StatsData={userData.top5_time} Title={'Top 5 time'} obj={'connection_time'} objTitle={"Time"} key={userData.top5_time[0].name + userData.top5_damage[0].connection_time}/>
        </div>
    );


};

export default TopPlayersList;