import { Route, Routes } from "react-router-dom";

import Layout from "./components/Layout";
import Dashboard from "./pages/Dashboard";
import Find from "./pages/Find";
import Contacted from "./pages/Contacted";
import Notifications from "./pages/Notifications";
import Favorites from "./pages/Favorites";
import Profile from "./pages/Profile";
import Settings from "./pages/Settings";
import LogIn from "./pages/LogIn";
import SignUp from "./pages/SignUp";

function App() {
  return (
    // <LogIn />
    <SignUp />
    // <Routes>
    //   <Route path="/" element={<Layout />}>
    //     <Route path="/" element={<Dashboard />} />
    //     <Route path="/dashboard" element={<Dashboard />} />
    //     <Route path="/find" element={<Find />} />
    //     <Route path="/contacted" element={<Contacted />} />
    //     <Route path="/notifications" element={<Notifications />} />
    //     <Route path="/favorites" element={<Favorites />} />
    //     <Route path="/profile" element={<Profile />} />
    //     <Route path="/settings" element={<Settings />} />
    //   </Route>
    //   {/* <Route path="/find/:id" element={<Details />} /> */}
    // </Routes>
  );
}

export default App;
