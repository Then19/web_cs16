import ServerLabel from "./components/server/Label/ServerLabel";
import {ToastContainer} from "react-toastify";

function App() {
    const example = {
        id: 1,
        host: "92.255.175.170",
        port: 27016,
        name: "[v-cs.ru][1x1]_aim_maps_Server#1",
        map: "mirage_2x2",
        count_players: 0,
        max_players: 2
    }

  return (
    <div className="App">
        <ToastContainer />
        <ServerLabel serverInfo={example}/>
    </div>
  );
}

export default App;
