import {ToastContainer} from "react-toastify";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Navbar from "./components/navfutor/Navbar";
import Main from "./pages/Main";
import NotFound from "./pages/NotFound";
import User from "./pages/User";


function App() {

  return (
      <BrowserRouter>
          <ToastContainer/>
          <div className={'App'}>
              <Navbar/>
              <Routes>
                  <Route path="/" element={<Main/>}/>
                  <Route exact path="/user/:user_id" element={<User/>} />
                  <Route path="*" element={<NotFound/>} status={404}/>
              </Routes>
          </div>
      </BrowserRouter>
  );
}

export default App;
