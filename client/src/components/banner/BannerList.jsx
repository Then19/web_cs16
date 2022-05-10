import React from 'react';
import "./banner.css"
import BannerLabel from "./BannerLabel";

const BannerList = () => {
    return (
        <div className={"list-banner-block"}>
            <BannerLabel gifName={'giphy'} href={"https://www.hltv.org/player/3741/niko"}/>
            <BannerLabel gifName={'giphy1'} href={"https://www.hltv.org/player/19230/m0nesy"}/>
        </div>
    );
};

export default BannerList;