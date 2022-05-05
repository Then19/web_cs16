import {ToastContainer} from "react-toastify";
import ServerList from "./components/server/List/ServerList";

function App() {

  return (
    <div className="App">
        <ToastContainer />
        <ServerList/>
    </div>
  );
}

export default App;
