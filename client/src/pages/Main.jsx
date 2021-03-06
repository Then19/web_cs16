import React from 'react';
import ServerList from "../components/server/List/ServerList";
import BannerList from "../components/banner/BannerList";
import TopPlayersList from "../components/stats/top/TopPlayersList";
import Board from "../components/stats/board/Board";

const Main = ({servers = [], ...props}) => {
    return (
        <div>
            <ServerList servers={servers}/>
            <BannerList/>
            <TopPlayersList/>
            <Board/>
        </div>
    );
};

export default Main;