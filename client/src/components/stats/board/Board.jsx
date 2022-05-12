import React, {useEffect, useState} from 'react';
import "./board.css"
import {showToast} from "../../../tools/toast";
import {getUsersList} from "../../../api/user";
import ReactPaginate from 'react-paginate';
import {Link} from "react-router-dom";

const Board = () => {
    const [usersData, setUsersData] = useState([])
    const [sortSelect, setSortSelect] = useState('skill')

    const [selectPage, setSelectPage] = useState(0)
    const [countPage, setCountPage] = useState(0)

    useEffect(() => {
        getUsersList(15, 15 * selectPage, sortSelect)
            .then(res =>{
                setUsersData(res.items)
                setCountPage(Math.ceil(res.count / 15))
            })
    }, [selectPage, sortSelect])


    function changeSelectPage({selected}) {
        setSelectPage(selected)
    }

    return (
        <div className={"body-board"}>
            <div className={"block-border-prime"}/>
            <div className={"block-background-top"}/>
            <div className={"block-user-board b-s-title"}>
                <div className={"block-user-board-name"}>Name</div>
                <div className={"block-user-board-stats"}>
                    <div onClick={() => setSortSelect('skill')} className={'b-s-skill b-s-select'}>Skill</div>
                    <div onClick={() => setSortSelect('kills')} className={'b-s-kills b-s-select'}>Kills</div>
                    <div className={'b-s-deaths'}>Deaths</div>
                    <div className={'b-s-kd'}>K/D</div>
                    <div className={'b-s-hs'}>Head</div>
                    <div className={'b-s-accuracy'}>Меткость</div>
                    <div onClick={() => setSortSelect('dmg')} className={'b-s-dmg b-s-select'}>Урон</div>
                    <div className={'b-s-assist'}>Assists</div>
                </div>
            </div>
            {usersData.map((item, index) =>
                <Link  key={item.id} onClick={() => showToast('warn', 'Статистика пользователей пока не доступна')} to={"/user/" + item.id}>
                    <div className={"block-user-board b-s-color-" + index % 2}>
                    <div className={"block-user-board-name"}>{index + 1 + (15 * selectPage)}. {item.name}</div>
                    <div className={"block-user-board-stats"}>
                        <div className={'b-s-skill'}>{item.skill}</div>
                        <div className={'b-s-kills'}>{item.kills}</div>
                        <div className={'b-s-deaths'}>{item.deaths}</div>
                        <div className={'b-s-kd'}>{(item.kills / item.deaths).toFixed(2)}</div>
                        <div className={'b-s-hs'}>{item.hs}</div>
                        <div className={'b-s-accuracy'}>{((item.hits / item.shots) * 100).toFixed(1)}%</div>
                        <div className={'b-s-dmg'}>{(item.dmg / 1000).toFixed(1)}k</div>
                        <div className={'b-s-assist'}>{item.assists}</div>
                    </div>
                </div></Link>
            )}
            <div className={'b-s-pagination-block'}>
                <ReactPaginate
                    previousLabel={"<"}
                    nextLabel={">"}
                    pageCount={countPage}
                    onPageChange={changeSelectPage}
                    containerClassName={'paginationButtons'}
                    activeClassName={'b-s-active'}
                    pageRangeDisplayed={3}
                    marginPagesDisplayed={2}
                />
            </div>
        </div>
    );
};

export default Board;