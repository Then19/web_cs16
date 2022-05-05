import React, {useEffect, useState} from 'react';
import "./serverList.css"
import ServerLabel from "../Label/ServerLabel";
import {getServersInfo} from "../../../api/server";

const ServerList = () => {
    const [serverData, setServerData] = useState([])
    const [updServ, setUpdServ] = useState(0)

    useEffect(() => {
        getServersInfo()
            .then(res =>{
                setServerData(res)
            })
        setTimeout(() => setUpdServ(updServ + 1), 15000)
    }, [updServ])


    return (
        <div className={"list-server-block"}>
            {serverData.map(item => <div id={item.id} key={item.map + item.id + item.count_players}><ServerLabel serverInfo={item}/></div>)}
        </div>
    );
};

export default ServerList;