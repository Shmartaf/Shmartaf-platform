import { Route, Routes } from "react-router-dom";

import Layout from "./components/Layout";
import ParentDashboard from "./pages/ParentDashboard";
import Find from "./pages/Find";
import Contacted from "./pages/Contacted";
import Notifications from "./pages/Notifications";
import Favorites from "./pages/Favorites";
import Profile from "./pages/Profile";
import Settings from "./pages/Settings";
import Reviews from "./pages/Reviews";
import Schedule from "./pages/Schedule";
import { BabysitterContext } from "./context/BabysitterContext";
import { useContext } from "react";
import Login from "./pages/Login";
import BabysitterDashboard from "./pages/BabysitterDashboard";

function App() {
  const { state, dispatch } = useContext(BabysitterContext);

  if (!state?.user?.role) {
    return <Login />;
  } else {
    return (
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route
            path="/"
            element={
              state?.user?.role === "babysitter" ? (
                <BabysitterDashboard />
              ) : (
                <ParentDashboard />
              )
            }
          />
          <Route path="/parentdashboard" element={<ParentDashboard />} />
          <Route
            path="/babysitterdashboard"
            element={<BabysitterDashboard />}
          />
          <Route path="/find" element={<Find />} />
          <Route path="/contacted" element={<Contacted />} />
          <Route path="/notifications" element={<Notifications />} />
          <Route path="/reviews" element={<Reviews />} />
          <Route path="/schedule" element={<Schedule />} />
          <Route path="/favorites" element={<Favorites />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/settings" element={<Settings />} />
        </Route>
        {/* <Route path="/find/:id" element={<Details />} /> */}
      </Routes>
    );
  }
}

export default App;
