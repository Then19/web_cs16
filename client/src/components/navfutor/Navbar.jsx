import React, {useEffect, useState} from 'react';
import "./navbar.css"
import {showToast} from "../../tools/toast";
import discordIco from "./image/discord.svg"
import githubIco from "./image/github.svg"
import telegramIco from "./image/telegram.svg"
import vkIco from "./image/vk.svg"
import {Link} from "react-router-dom";

const Navbar = ({online=0, ...props}) => {
    const [show, setShow] = useState("")

    useEffect(() => {
        let lastPosition = window.pageYOffset
        window.onscroll = () => {
            if (window.pageYOffset > lastPosition && window.pageYOffset > 0) {
                setShow("header-hide")
            } else {
                setShow("")
            }
            lastPosition = window.pageYOffset
        }
    }, []);

    return (
        <div className={"header-main " + show}>
            <div className="nav-login-btn-block">
                <Link onClick={() => showToast('error', 'Там же написано, не надо это нажимать!!!')} to={"/"}>САЙТ В РАЗРАБОТКЕ</Link>
            </div>
            <div className={"nav-social"}>
                <a href="https://github.com/Then19/web_cs16"><img className={"social-ico"} loading={"lazy"} src={githubIco} alt=""/></a>
                <a href="https://t.me/then19"><img className={"social-ico"} loading={"lazy"} src={telegramIco} alt=""/></a>
                <a href="#"><img className={"social-ico"} loading={"lazy"} src={discordIco} alt=""/></a>
                <a href="https://vk.com/tol9h4ik"><img className={"social-ico"} loading={"lazy"} src={vkIco} alt=""/></a>
                <div className={'nav-online'}>Online: {online}</div>
            </div>
        </div>
    );
};

export default Navbar;