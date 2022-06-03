import {ToastContainer} from "react-toastify";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Navbar from "./components/navfutor/Navbar";
import Main from "./pages/Main";
import NotFound from "./pages/NotFound";
import User from "./pages/User";
import {useEffect, useState} from "react";


function App() {
    const [online, setOnline] = useState(0)


    useEffect(() => {
        const ws = new WebSocket('ws://127.0.0.1:8000/server/status');
        ws.onopen = (event) => {

        };
        ws.onmessage = function (event) {
            const json = JSON.parse(event.data);
            try {
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
                    <Route path="/" element={<Main/>}/>
                    <Route exact path="/user/:user_id" element={<User/>}/>
                    <Route path="*" element={<NotFound/>} status={404}/>
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;
