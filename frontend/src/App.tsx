import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import { ProductProvider } from "./context/ProductContext";
import "./App.css"

import Admin from "./pages/Admin";
import Shop from "./pages/Shop";

function App() {
  return (
    <>
    <ProductProvider>
        <BrowserRouter>
            <Navbar />
            <Routes>
              <Route path="/shop" element={<Shop />} />
              <Route path="/admin" element={<Admin />} />
            </Routes>
        </BrowserRouter>
    </ProductProvider>
    </>
  );
}

export default App;
