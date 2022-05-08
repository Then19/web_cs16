import React from 'react';
import "./top.css"
import {showToast} from "../../../tools/toast";

const StatsLabel = ({StatsData, Title, obj, objTitle, titleColor = 'title-gold'}) => {
    return (
        <div className={"body-top"}>
            <div className={"block-border-top " + "block-border-" + titleColor}/>
            <div className={"block-background-top"}/>
            <div className="top-label-block">
                <div className={"top-label-title " + "title-" + titleColor}>{Title}</div>
                <div className={"top-users-list-block-title"}>
                    <div>Name</div><div>{objTitle}</div>
                </div>
                {StatsData.map((item, index) =>
                    <a onClick={() => showToast('warn', 'Статистика пользователей пока не доступна')} href="#">
                        <div key={index} className={"top-users-list-block " + "top-color-" + index}>
                        <div>{index + 1}. {item.name}</div><div>{item[obj]}</div>
                    </div></a>
                )}
            </div>
        </div>
    );
};

export default StatsLabel;