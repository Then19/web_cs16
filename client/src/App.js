import {ToastContainer} from "react-toastify";
import ServerList from "./components/server/List/ServerList";
import TopPlayersList from "./components/stats/top/TopPlayersList";


function App() {


  return (
    <div className="App">
        <ToastContainer />
        <ServerList/>
        <TopPlayersList/>
    </div>
  );
}

export default App;
