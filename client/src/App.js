import {ToastContainer} from "react-toastify";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Navbar from "./components/navfutor/Navbar";
import Main from "./pages/Main";
import NotFound from "./pages/NotFound";
import User from "./pages/User";
import {useEffect, useState} from "react";
import config from "./api/config.json";


function App() {
    const [online, setOnline] = useState(0)
    const [serverOnline, setServerOnline] = useState([])


    useEffect(() => {
        const ws = new WebSocket(config.hostname_ws + 'server/status');
        ws.onopen = (event) => {

        };
        ws.onmessage = function (event) {
            const json = JSON.parse(event.data);
            try {
                setServerOnline(json.servers.data)
                setOnline(json.online)
            } catch (err) {
                console.log(err);
            }
        };

        return () => ws.close();
    }, []);

    return (
        <BrowserRouter>
            <ToastContainer/>
            <div className={'App'}>
                <Navbar online={online}/>
                <Routes>
                    <Route path="/" element={<Main servers={serverOnline}/>}/>
                    <Route exact path="/user/:user_id" element={<User/>}/>
                    <Route path="*" element={<NotFound/>} status={404}/>
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;
