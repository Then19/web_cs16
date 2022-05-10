import {ToastContainer} from "react-toastify";
import ServerList from "./components/server/List/ServerList";
import TopPlayersList from "./components/stats/top/TopPlayersList";
import Navbar from "./components/navfutor/Navbar";
import BannerList from "./components/banner/BannerList";
import Board from "./components/stats/board/Board";


function App() {

  return (
    <div className="App">
        <Navbar/>
        <ToastContainer />
        <ServerList/>
        <BannerList/>
        <TopPlayersList/>
        <Board/>
    </div>
  );
}

export default App;
