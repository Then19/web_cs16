import React from 'react';
import "./top.css"

const StatsLabel = ({StatsData, Title, obj, objTitle}) => {
    return (
        <div className={"body-top"}>
            <div className={"block-border-top"}/>
            <div className={"block-background-top"}/>
            <div className="top-label-block">
                <div className={"top-label-title"}>{Title}</div>
                <div className={"top-users-list-block-title"}>
                    <div>Name</div><div>{objTitle}</div>
                </div>
                {StatsData.map((item, index) =>
                    <div key={index} className={"top-users-list-block"}>
                        <div><a href="#">{index + 1}. {item.name}</a></div><div>{item[obj]}</div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default StatsLabel;