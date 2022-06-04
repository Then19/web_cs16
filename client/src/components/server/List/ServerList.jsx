import React from 'react';
import "./serverList.css"
import ServerLabel from "../Label/ServerLabel";


const ServerList = ({servers = [], ...props}) => {


    return (
        <div className={"list-server-block"}>
            {servers.map(item => <div id={item.id} key={item.map + item.id + item.count_players}><ServerLabel serverInfo={item}/></div>)}
        </div>
    );
};

export default ServerList;