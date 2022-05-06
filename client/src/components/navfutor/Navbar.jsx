import React, {useEffect, useState} from 'react';
import "./navbar.css"
import {showToast} from "../../tools/toast";
import discordIco from "./image/discord.svg"
import githubIco from "./image/github.svg"
import telegramIco from "./image/telegram.svg"
import vkIco from "./image/vk.svg"

const Navbar = () => {
    const [show, setShow] = useState("")

    useEffect(() => {
        let lastPosition = window.pageYOffset
        window.onscroll = () => {
            if (window.pageYOffset > lastPosition) {
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
                <a onClick={() => showToast('error', 'Там же написано, не надо это нажимать!!!')} href={"#"}>САЙТ В РАЗРАБОТКЕ</a>
            </div>
            <div className={"nav-social"}>
                <a href="https://github.com/Then19/web_cs16"><img className={"social-ico"} loading={"lazy"} src={githubIco} alt=""/></a>
                <a href="https://t.me/then19"><img className={"social-ico"} loading={"lazy"} src={telegramIco} alt=""/></a>
                <a href="#"><img className={"social-ico"} loading={"lazy"} src={discordIco} alt=""/></a>
                <a href="https://vk.com/tol9h4ik"><img className={"social-ico"} loading={"lazy"} src={vkIco} alt=""/></a>
            </div>
        </div>
    );
};

export default Navbar;