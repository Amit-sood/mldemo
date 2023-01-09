import "./App.css";

import Duplicate from "./Duplicate";
import { Home } from "./Home";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/duplicate" element={<Duplicate />} />
      </Routes>
      <Routes>
        <Route path="/" element={<Home />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
