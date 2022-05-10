import React from 'react';
import "./banner.css"

const BannerLabel = ({gifName, href='#'}) => {
    return (
        <div className={"body-banner"}>
            <div className={"block-border-top block-border-silver"}/>
            <a href={href}>
            <div className={"block-banner-map-img block-border-banner-map"}>
                <img draggable={"false"} loading={"lazy"} src={`image/banner/${gifName}.webp`} alt=""/>
            </div></a>
        </div>
    );
};

export default BannerLabel;