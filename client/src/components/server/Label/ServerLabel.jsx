import React from 'react';
import "./serverLabel.css";
import copyImage from "./image/copy2.svg";
import playImage from "./image/play.svg";
import {useClipboard} from "use-clipboard-copy";
import {showToast} from "../../../tools/toast";

const ServerLabel = ({serverInfo}) => {

    const clipboard = useClipboard()

    return (
        <div className={"body-servers"}>
            <div className={"block-border-prime"}/>
            <div className={"block-servers-map-img block-border-map"}>
                <img draggable={"false"} loading={"lazy"} src={`image/maps/${serverInfo.map}.jpg`} alt=""/>
            </div>
            <div className={"block-servers-name"}>{serverInfo.name}</div>
            <div className={"block-servers-desc"}>{serverInfo.count_players}/{serverInfo.max_players} | {serverInfo.map}</div>
            <a className={"copy-ip"} onClick={() => {clipboard.copy(`${serverInfo.host}:${serverInfo.port}`);
                showToast('success', 'IP скопирован')}}>
                <img loading={'lazy'} src={copyImage} alt=""/>
            </a>
            <a href={"steam://connect/" + `${serverInfo.host}:${serverInfo.port}`}>
                <img loading={'lazy'} className={"h-23"} src={playImage} alt=""/>
            </a>
        </div>
    );
};

export default ServerLabel;