import React from 'react';
import "./board.css"

const Board = () => {
    const example = {
        "id": 650,
        "steamid": "STEAM_0:1:44389722",
        "name": "kOsmo",
        "skill": 138.77,
        "kills": 112,
        "deaths": 44,
        "hs": 44,
        "tks": 0,
        "shots": 1242,
        "hits": 304,
        "dmg": 15683,
        "bombdef": 0,
        "bombdefused": 0,
        "bombplants": 0,
        "bombexplosions": 0,
        "h_0": 0,
        "h_1": 63,
        "h_2": 48,
        "h_3": 20,
        "h_4": 122,
        "h_5": 40,
        "h_6": 8,
        "h_7": 3,
        "connection_time": 2935,
        "connects": 5,
        "roundt": 73,
        "wint": 56,
        "roundct": 46,
        "winct": 27,
        "assists": 8,
        "first_join": "2022-04-19T14:48:40",
        "last_join": "2022-04-19T15:38:27"
    }


    return (
        <div className={"body-board"}>
            <div className={"block-border-prime"}/>
            <div className={"block-background-top"}/>
            <div className={"block-user-board"}>

            </div>
        </div>
    );
};

export default Board;