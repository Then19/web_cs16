import {ToastContainer} from "react-toastify";
import ServerList from "./components/server/List/ServerList";
import TopPlayersList from "./components/stats/top/TopPlayersList";
import Navbar from "./components/navfutor/Navbar";
import BannerList from "./components/banner/BannerList";


function App() {

  return (
    <div className="App">
        <Navbar/>
        <ToastContainer />
        <ServerList/>
        <BannerList/>
        <TopPlayersList/>
    </div>
  );
}

export default App;
